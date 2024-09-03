import itertools
import logging
import random
import copy
import time
from collections import deque
from collections.abc import Hashable
from typing import Callable, Dict, Iterable, List, Tuple, Set, Optional

from BaseClasses import CollectionState, Entrance, Region, IntEnum, MultiWorld
from Options import Accessibility
from worlds.AutoWorld import World


class EntranceType(IntEnum):
    ONE_WAY = 1
    TWO_WAY = 2


class EntranceRandomizationError(RuntimeError):
    pass


def can_reach(ent: Entrance, state: CollectionState) -> bool:
    if ent.parent_region.can_reach(state) and ent.access_rule(state):
        if not ent.hide_path and ent not in state.path:
            state.path[ent] = (ent.name, state.path.get(ent.parent_region, (ent.parent_region.name, None)))
        return True

    return False


def is_valid_source_transition(ent: Entrance, state: "ERPlacementState") -> bool:
    return ent.can_reach(state.collection_state)


def can_connect_to(ent: Entrance, other: "Entrance", state: "ERPlacementState") -> bool:
    # the implementation of coupled causes issues for self-loops since the reverse entrance will be the
    # same as the forward entrance. In uncoupled they are ok.
    return not state.coupled or ent.name != other.name


def create_er_target(reg: Region, name: str) -> Entrance:
    entrance = reg.entrance_type(reg.player, name)
    entrance.connect(reg)
    return entrance


class EntranceLookup:
    class GroupLookup:
        _lookup: Dict[Hashable, List[Entrance]]

        def __init__(self):
            self._lookup = {}

        def __len__(self):
            return sum(map(len, self._lookup.values()))

        def __bool__(self):
            return bool(self._lookup)

        def __getitem__(self, item: Hashable) -> List[Entrance]:
            return self._lookup.get(item, [])

        def __iter__(self):
            return itertools.chain.from_iterable(self._lookup.values())

        def __str__(self):
            return str(self._lookup)

        def __repr__(self):
            return self.__str__()

        def add(self, entrance: Entrance) -> None:
            self._lookup.setdefault(0, []).append(entrance)

        def remove(self, entrance: Entrance) -> None:
            group = self._lookup[0]
            group.remove(entrance)
            if not group:
                del self._lookup[0]

    dead_ends: GroupLookup
    others: GroupLookup
    _random: random.Random
    _leads_to_exits_cache: Dict[Entrance, bool]
    _coupled: bool

    def __init__(self, rng: random.Random, coupled: bool):
        self.dead_ends = EntranceLookup.GroupLookup()
        self.others = EntranceLookup.GroupLookup()
        self._random = rng
        self._leads_to_exits_cache = {}
        self._coupled = coupled

    def _can_lead_to_randomizable_exits(self, entrance: Entrance) -> bool:
        """
        Checks whether an entrance is able to lead to another randomizable exit
        with some combination of items

        :param entrance: A randomizable (no parent) region entrance
        """
        # we've seen this, return cached result
        if entrance in self._leads_to_exits_cache:
            return self._leads_to_exits_cache[entrance]

        visited = set()
        q = deque()
        q.append(entrance.connected_region)

        while q:
            region = q.popleft()
            visited.add(region)

            for exit_ in region.exits:
                # randomizable exits which are not reverse of the incoming entrance.
                # uncoupled mode is an exception because in this case going back in the door you just came in could
                # actually lead somewhere new
                if not exit_.connected_region and (not self._coupled or exit_.name != entrance.name):
                    self._leads_to_exits_cache[entrance] = True
                    return True
                elif exit_.connected_region and exit_.connected_region not in visited:
                    q.append(exit_.connected_region)

        self._leads_to_exits_cache[entrance] = False
        return False

    def add(self, entrance: Entrance) -> None:
        lookup = self.others if self._can_lead_to_randomizable_exits(entrance) else self.dead_ends
        lookup.add(entrance)

    def remove(self, entrance: Entrance) -> None:
        lookup = self.others if self._can_lead_to_randomizable_exits(entrance) else self.dead_ends
        lookup.remove(entrance)

    def get_targets(
            self,
            groups: Iterable[Hashable],
            dead_end: bool,
            preserve_group_order: bool
    ) -> Iterable[Entrance]:

        lookup = self.dead_ends if dead_end else self.others
        if preserve_group_order:
            for group in groups:
                self._random.shuffle(lookup[group])
            ret = [entrance for group in groups for entrance in lookup[group]]
        else:
            ret = [entrance for group in groups for entrance in lookup[group]]
            self._random.shuffle(ret)
        return ret

    def __len__(self):
        return len(self.dead_ends) + len(self.others)


class UndertaleCollectionState(CollectionState):
    allow_partial_entrances: bool

    def __init__(self, parent: MultiWorld, allow_partial_entrances: bool = False):
        super().__init__(parent)
        self.allow_partial_entrances = allow_partial_entrances

    def update_reachable_regions(self, player: int):
        self.stale[player] = False
        reachable_regions = self.reachable_regions[player]
        blocked_connections = self.blocked_connections[player]
        queue = deque(self.blocked_connections[player])
        start = self.multiworld.get_region("Menu", player)
        # init on first call - this can't be done on construction since the regions don't exist yet
        if start not in reachable_regions:
            reachable_regions.add(start)
            blocked_connections.update(start.exits)
            queue.extend(start.exits)
        # run BFS on all connections, and keep track of those blocked by missing items
        while queue:
            connection = queue.popleft()
            new_region = connection.connected_region
            if new_region in reachable_regions:
                blocked_connections.remove(connection)
            elif connection.can_reach(self):
                if self.allow_partial_entrances and not new_region:
                    continue
                assert new_region, f"tried to search through an Entrance \"{connection}\" with no Region"
                reachable_regions.add(new_region)
                blocked_connections.remove(connection)
                blocked_connections.update(new_region.exits)
                queue.extend(new_region.exits)
                self.path[new_region] = (new_region.name, self.path.get(connection, None))
                # Retry connections if the new region can unblock them
                for new_entrance in self.multiworld.indirect_connections.get(new_region, set()):
                    if new_entrance in blocked_connections and new_entrance not in queue:
                        queue.append(new_entrance)

    def copy(self) -> CollectionState:
        ret = CollectionState(self.multiworld)
        ret.prog_items = copy.deepcopy(self.prog_items)
        ret.reachable_regions = {player: copy.copy(self.reachable_regions[player]) for player in
                                 self.reachable_regions}
        ret.blocked_connections = {player: copy.copy(self.blocked_connections[player]) for player in
                                   self.blocked_connections}
        ret.events = copy.copy(self.events)
        ret.path = copy.copy(self.path)
        ret.locations_checked = copy.copy(self.locations_checked)
        ret.allow_partial_entrances = self.allow_partial_entrances
        for function in self.additional_copy_functions:
            ret = function(self, ret)
        return ret


def get_all_state(self: MultiWorld, use_cache: bool, allow_partial_entrances: bool = False) -> UndertaleCollectionState:
    cached = getattr(self, "_all_state", None)
    if use_cache and cached:
        return cached.copy()

    ret = UndertaleCollectionState(self, allow_partial_entrances)

    for item in self.itempool:
        self.worlds[item.player].collect(ret, item)
    for player in self.player_ids:
        subworld = self.worlds[player]
        for item in subworld.get_pre_fill_items():
            subworld.collect(ret, item)
    ret.sweep_for_advancements()

    if use_cache:
        self._all_state = ret
    return ret


class ERPlacementState:
    """The state of an ongoing or completed entrance randomization"""
    placements: List[Entrance]
    """The list of randomized Entrance objects which have been connected successfully"""
    pairings: List[Tuple[str, str]]
    """A list of pairings of connected entrance names, of the form (source_exit, target_entrance)"""
    world: World
    """The world which is having its entrances randomized"""
    collection_state: CollectionState
    """The CollectionState backing the entrance randomization logic"""
    coupled: bool
    """Whether entrance randomization is operating in coupled mode"""

    def __init__(self, world: World, coupled: bool):
        self.placements = []
        self.pairings = []
        self.world = world
        self.coupled = coupled
        self.collection_state = get_all_state(world.multiworld, False, True)

    @property
    def placed_regions(self) -> Set[Region]:
        return set(item for item in self.collection_state.reachable_regions[self.world.player])

    def find_placeable_exits(self, check_validity: bool) -> List[Entrance]:
        if check_validity:
            blocked_connections = self.collection_state.blocked_connections[self.world.player]
            blocked_connections = sorted(blocked_connections, key=lambda x: x.name)
            placeable_randomized_exits = [connection for connection in blocked_connections
                                          if not connection.connected_region
                                          and is_valid_source_transition(connection, self)]
        else:
            # this is on a beaten minimal attempt, so any exit anywhere is fair game
            placeable_randomized_exits = [ex for region in self.world.multiworld.get_regions(self.world.player)
                                          for ex in region.exits if not ex.connected_region]
        self.world.random.shuffle(placeable_randomized_exits)
        return placeable_randomized_exits

    def _connect_one_way(self, source_exit: Entrance, target_entrance: Entrance) -> None:
        target_region = target_entrance.connected_region

        target_region.entrances.remove(target_entrance)
        source_exit.connect(target_region)

        self.collection_state.stale[self.world.player] = True
        self.placements.append(source_exit)
        self.pairings.append((source_exit.name, target_entrance.name))

    def connect(
            self,
            source_exit: Entrance,
            target_entrance: Entrance
    ) -> Tuple[List[Entrance], List[Entrance]]:
        """
        Connects a source exit to a target entrance in the graph, accounting for coupling

        :returns: The newly placed exits and the dummy entrance(s) which were removed from the graph
        """
        source_region = source_exit.parent_region
        target_region = target_entrance.connected_region

        self._connect_one_way(source_exit, target_entrance)
        # if we're doing coupled randomization place the reverse transition as well.
        if self.coupled:
            for reverse_entrance in source_region.entrances:
                if reverse_entrance.name == source_exit.name:
                    if reverse_entrance.parent_region:
                        raise EntranceRandomizationError(
                            f"Could not perform coupling on {source_exit.name} -> {target_entrance.name} "
                            f"because the reverse entrance is already parented to "
                            f"{reverse_entrance.parent_region.name}.")
                    break
            else:
                raise EntranceRandomizationError(f"Two way exit {source_exit.name} had no corresponding entrance in "
                                                 f"{source_exit.parent_region.name}")
            for reverse_exit in target_region.exits:
                if reverse_exit.name == target_entrance.name:
                    if reverse_exit.connected_region:
                        raise EntranceRandomizationError(
                            f"Could not perform coupling on {source_exit.name} -> {target_entrance.name} "
                            f"because the reverse exit is already connected to "
                            f"{reverse_exit.connected_region.name}.")
                    break
            else:
                raise EntranceRandomizationError(f"Two way entrance {target_entrance.name} had no corresponding exit "
                                                 f"in {target_region.name}.")
            self._connect_one_way(reverse_exit, reverse_entrance)
            return [source_exit, reverse_exit], [target_entrance, reverse_entrance]
        return [source_exit], [target_entrance]


def disconnect_entrance_for_randomization(entrance: Entrance, randomization_type: EntranceType = EntranceType.TWO_WAY):
    """
    Given an entrance in a "vanilla" region graph, splits that entrance to prepare it for randomization
    in randomize_entrances. This should be done after setting the type and group of the entrance.

    :param entrance: The entrance which will be disconnected in preparation for randomization.
    :param randomization_type: TO DOCUMENT.
    """
    child_region = entrance.connected_region
    parent_region = entrance.parent_region

    # disconnect the edge
    child_region.entrances.remove(entrance)
    entrance.connected_region = None

    # create the needed ER target
    create_er_target(parent_region, entrance.name)


def randomize_entrances(
        world: World,
        coupled: bool,
        target_group_lookup: Dict[Hashable, List[Hashable]],
        preserve_group_order: bool = False,
        on_connect: Optional[Callable[[ERPlacementState, List[Entrance]], None]] = None
) -> ERPlacementState:
    """
    Randomizes Entrances for a single world in the multiworld.

    :param world: Your World instance
    :param coupled: Whether connected entrances should be coupled to go in both directions
    :param target_group_lookup: Map from each group to a list of the groups that it can be connected to. Every group
                                used on an exit must be provided and must map to at least one other group. The default
                                group is 0.
    :param preserve_group_order: Whether the order of groupings should be preserved for the returned target_groups
    :param on_connect: A callback function which allows specifying side effects after a placement is completed
                       successfully and the underlying collection state has been updated.
    """
    start_time = time.perf_counter()
    er_state = ERPlacementState(world, coupled)
    entrance_lookup = EntranceLookup(world.random, coupled)
    # similar to fill, skip validity checks on entrances if the game is beatable on minimal accessibility
    perform_validity_check = True

    def do_placement(source_exit: Entrance, target_entrance: Entrance) -> None:
        placed_exits, removed_entrances = er_state.connect(source_exit, target_entrance)
        # remove the placed targets from consideration
        for entrance in removed_entrances:
            entrance_lookup.remove(entrance)
        # propagate new connections
        er_state.collection_state.update_reachable_regions(world.player)
        if on_connect:
            on_connect(er_state, placed_exits)

    def find_pairing(dead_end: bool, require_new_regions: bool) -> bool:
        nonlocal perform_validity_check
        placeable_exits = er_state.find_placeable_exits(perform_validity_check)
        for source_exit in placeable_exits:
            target_groups = target_group_lookup[0]
            for target_entrance in entrance_lookup.get_targets(target_groups, dead_end, preserve_group_order):
                # requiring a new region is a proxy for enforcing new entrances are added, thus growing the search
                # space. this is not quite a full fidelity conversion, but doesn't seem to cause issues enough
                # to do more complex checks.
                # the new region requirement can be ignored on a beaten minimal, islands are no issue there
                region_requirement_satisfied = (not perform_validity_check or not require_new_regions
                                                or target_entrance.connected_region not in er_state.placed_regions)
                if region_requirement_satisfied and can_connect_to(source_exit, target_entrance, er_state):
                    do_placement(source_exit, target_entrance)
                    return True
        else:
            # no source exits had any valid target so this stage is deadlocked. retries may be implemented if early
            # deadlocking is a frequent issue.
            lookup = entrance_lookup.dead_ends if dead_end else entrance_lookup.others

            # if we're in a stage where we're trying to get to new regions, we could also enter this
            # branch in a success state (when all regions of the preferred type have been placed, but there are still
            # additional unplaced entrances into those regions)
            if require_new_regions:
                if all(e.connected_region in er_state.placed_regions for e in lookup):
                    return False

            # if we're on minimal accessibility and can guarantee the game is beatable,
            # we can prevent a failure by bypassing future validity checks. this check may be
            # expensive; fortunately we only have to do it once
            if perform_validity_check and world.options.accessibility == Accessibility.option_minimal \
                    and world.multiworld.has_beaten_game(er_state.collection_state, world.player):
                # ensure that we have enough locations to place our progression
                accessible_location_count = 0
                prog_item_count = len(er_state.collection_state.prog_items[world.player])
                # short-circuit location checking in this case
                if prog_item_count == 0:
                    return True
                for region in er_state.placed_regions:
                    for loc in region.locations:
                        if loc.can_reach(er_state.collection_state):
                            accessible_location_count += 1
                            if accessible_location_count >= prog_item_count:
                                perform_validity_check = False
                                # pretend that this was successful to retry the current stage
                                return True

            unplaced_entrances = [entrance for region in world.multiworld.get_regions(world.player)
                                  for entrance in region.entrances if not entrance.parent_region]
            unplaced_exits = [exit_ for region in world.multiworld.get_regions(world.player)
                              for exit_ in region.exits if not exit_.connected_region]
            entrance_kind = "dead ends" if dead_end else "non-dead ends"
            region_access_requirement = "requires" if require_new_regions else "does not require"
            raise EntranceRandomizationError(
                f"None of the available entrances are valid targets for the available exits.\n"
                f"Randomization stage is placing {entrance_kind} and {region_access_requirement} "
                f"new region access by default\n"
                f"Placeable entrances: {lookup}\n"
                f"Placeable exits: {placeable_exits}\n"
                f"All unplaced entrances: {unplaced_entrances}\n"
                f"All unplaced exits: {unplaced_exits}")

    er_targets = [entrance for region in world.multiworld.get_regions(world.player)
                  for entrance in region.entrances if not entrance.parent_region]
    exits = [ex for region in world.multiworld.get_regions(world.player)
             for ex in region.exits if not ex.connected_region]
    if len(er_targets) != len(exits):
        raise EntranceRandomizationError(f"Unable to randomize entrances due to a mismatched count of "
                                         f"entrances ({len(er_targets)}) and exits ({len(exits)}.")
    for entrance in er_targets:
        entrance_lookup.add(entrance)

    # place the menu region and connected start region(s)
    er_state.collection_state.update_reachable_regions(world.player)

    # stage 1 - try to place all the non-dead-end entrances
    while entrance_lookup.others:
        if not find_pairing(dead_end=False, require_new_regions=True):
            break
    # stage 2 - try to place all the dead-end entrances
    while entrance_lookup.dead_ends:
        if not find_pairing(dead_end=True, require_new_regions=True):
            break
    # stage 3 - connect any dangling entrances that remain
    while entrance_lookup.others:
        find_pairing(dead_end=False, require_new_regions=False)
    # stage 4 - last chance for dead ends
    while entrance_lookup.dead_ends:
        find_pairing(dead_end=True, require_new_regions=False)

    running_time = time.perf_counter() - start_time
    if running_time > 1.0:
        logging.info(f"Took {running_time:.4f} seconds during entrance randomization for player {world.player},"
                     f"named {world.multiworld.player_name[world.player]}")

    return er_state
