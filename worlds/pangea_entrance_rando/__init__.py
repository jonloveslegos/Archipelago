import BaseClasses
from worlds.generic.Rules import exclusion_rules
from worlds.AutoWorld import World, call_all, WebWorld
from BaseClasses import Tutorial, Item, ItemClassification, Location, Group
from .Options import PangeaOptions
from argparse import Namespace
from worlds.generic.Rules import set_rule
try:
    import custom_worlds.undertale as ut_world
except ModuleNotFoundError:
    import worlds.undertale as ut_world
from worlds.LauncherComponents import Component, components
from multiprocessing import Process
from .entrance_rando import *
from typing import NamedTuple, List, Type


def run_client():
    print('running Pangea client')
    from .PangeaClient import main  # lazy import
    p = Process(target=main)
    p.start()


class PangeaLocation(Location):
    game: str = "Pangea"


class PangeaItem(Item):
    game: str = "Pangea"


class Portal(NamedTuple):
    mod_string: str


# components.append(Component("Pangea Client", "PangeaClient"))
components.append(Component("Pangea Client", func=run_client))


class PangeaWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Archipelago Pangea software on your computer. This guide covers "
        "single-player, multiworld, and related software.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Mewlif"]
    )]


class PangeaWorld(World):
    """
    Undertale is an RPG where every choice you make matters. You could choose to hurt all the enemies, eventually
    causing genocide of the monster species. Or you can spare all the enemies, befriending them and freeing them
    from their underground prison.
    """
    game = "Pangea"
    options_dataclass = PangeaOptions
    options: PangeaOptions
    web = PangeaWeb()
    multiworld_pangea: MultiWorld

    portal_pairs: List[Tuple[str, str]]

    item_name_to_id = {name: data for name, data in ut_world.UndertaleWorld.item_name_to_id.items()}
    location_name_to_id = {name: data for name, data in ut_world.UndertaleWorld.location_name_to_id.items()}

    topology_present = True

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)

    def _get_pangea_data(self):
        return {
            "world_seed": self.random.getrandbits(32),
            "seed_name": self.multiworld.seed_name,
            "player_name": self.multiworld.get_player_name(self.player),
            "player_id": self.player,
            "client_version": self.required_client_version,
            "Entrance Rando": self.portal_pairs,
            "race": self.multiworld.is_race,
            "include_undertale": bool(self.options.include_undertale.value),
        }

    def get_filler_item_name(self):
        possible_filler = []
        for plr in self.multiworld_pangea.player_ids:
            possible_filler += self.multiworld_pangea.worlds[plr].get_filler_item_name()

        return self.random.choice(possible_filler)

    def pre_fill(self):
        for plr in self.multiworld_pangea.player_ids:
            if self.multiworld_pangea.worlds[plr].game == "Undertale":
                if self.multiworld_pangea.worlds[plr].options.entrance_rando:
                    portal_mapping_temp = [item.destination_string() for item in ut_world.er_scripts.portal_mapping]
                    for item in portal_mapping_temp:
                        temp = self.multiworld.get_entrance(item, self.player)
                        temp.name = "Undertale: "+temp.name
                        disconnect_entrance_for_randomization(temp)

        self.portal_pairs = randomize_entrances(self, True, {0: [0]}).pairings

    def generate_early(self):
        multiworld = MultiWorld(1)
        multiworld.set_seed()
        worlds: List[Type[World]] = [ut_world.UndertaleWorld]
        multiworld.game = {player: world_type.game for player, world_type in enumerate(worlds, 1)}
        multiworld.player_name = {player: f"Tester{player}" for player in multiworld.player_ids}
        multiworld.state = CollectionState(multiworld)
        args = Namespace()
        for player, world_type in enumerate(worlds, 1):
            for key, option in world_type.options_dataclass.type_hints.items():
                updated_options = getattr(args, key, {})
                updated_options[player] = option.from_any(option.default)
                for item in self.options_dataclass.type_hints:
                    if item == key:
                        updated_options[player] = getattr(self.options, item)
                setattr(args, key, updated_options)
        multiworld.set_options(args)
        self.multiworld_pangea = multiworld
        call_all(self.multiworld_pangea, "generate_early")

    def create_items(self):
        # Generate item pool
        itempool = []
        call_all(self.multiworld_pangea, "create_items")
        for plr, itms in self.multiworld_pangea.precollected_items.items():
            for item in itms:
                item.player = self.player
                self.multiworld.push_precollected(item)
        for item in self.multiworld_pangea.itempool:
            item.player = self.player
            itempool += [item]
        # Choose locations to automatically exclude based on settings
        exclusion_checks = set()
        for ply in range(self.multiworld_pangea.players):
            for item in self.multiworld_pangea.get_locations(ply+1):
                if item.progress_type == BaseClasses.LocationProgressType.EXCLUDED:
                    exclusion_checks.update([item.name])

        exclusion_rules(self.multiworld, self.player, exclusion_checks)

        # Fill remaining items with randomly generated junk
        while len(itempool) < len(self.multiworld.get_unfilled_locations(self.player)):
            itempool.append(self.create_filler())

        self.multiworld.itempool += itempool

    def set_rules(self) -> None:
        call_all(self.multiworld_pangea, "set_rules")
        for plr in self.multiworld_pangea.player_ids:
            for loc in self.multiworld_pangea.get_locations(plr):
                set_rule(self.get_location(loc.name), loc.access_rule)

            for ent in self.multiworld_pangea.get_entrances(plr):
                set_rule(self.get_entrance(ent.name), ent.access_rule)

            self.multiworld.completion_condition[self.player] = lambda state, pangea_rule=self.multiworld_pangea.completion_condition[plr], completion_condition=self.multiworld.completion_condition[self.player]: completion_condition(state) and pangea_rule(state)

    def create_regions(self):
        call_all(self.multiworld_pangea, "create_regions")
        for plr in self.multiworld_pangea.player_ids:
            portal_mapping_temp = [item for item in self.multiworld_pangea.get_regions(plr)]

            for item in portal_mapping_temp:
                new_item: Region = Region(item.name, self.player, self.multiworld)
                for loc in item.locations:
                    temp = PangeaLocation(self.player, loc.name, loc.address, new_item)
                    if loc.locked:
                        if loc.item.code is None:
                            temp.place_locked_item(PangeaItem(loc.item.name, ItemClassification.progression, None, self.player))
                        else:
                            temp.place_locked_item(self.create_item(loc.item.name))
                    new_item.locations.append(temp)
                self.multiworld.regions.append(new_item)
            for item in portal_mapping_temp:
                for ent in item.exits:
                    self.get_region(item.name).add_exits({ent.connected_region.name: ent.name})

    def fill_slot_data(self):
        return self._get_pangea_data()

    def create_item(self, name: str) -> Item:
        for plr in self.multiworld_pangea.player_ids:
            if name in self.multiworld_pangea.worlds[plr].item_names:
                item_data = self.multiworld_pangea.worlds[plr].create_item(name)
                item = PangeaItem(name, item_data.classification, item_data.code, self.player)
                return item

        return PangeaItem("None", ItemClassification.filler, 9999999999, self.player)
