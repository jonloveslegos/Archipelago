from typing import Dict, List, Set, Tuple, TYPE_CHECKING
from BaseClasses import Region, ItemClassification, Item, Location
from .Locations import advancement_table as location_table
from .er_data import Portal, undertale_er_regions, portal_mapping, dependent_regions, hallway_helper
from .er_rules import set_er_region_rules

if TYPE_CHECKING:
    from . import UndertaleWorld


origin_letter_flip = {
    "A": "B",
    "B": "A",
    "C": "D",
    "D": "C",
    "R": "R",
    "S": "S",
    "T": "T",
    "U": "U",
    "V": "V",
    "W": "W",
    "X": "X",
}


class UndertaleERItem(Item):
    game: str = "Undertale"


class UndertaleERLocation(Location):
    game: str = "Undertale"


def create_er_regions_vanilla(world: "UndertaleWorld") -> Dict[Portal, Portal]:
    portal_pairs: Dict[Portal, Portal] = dict()
    connected_regions: Set[str] = set()
    # make better start region stuff when/if implementing random start
    start_region = "room_area1"
    connected_regions.update(add_dependent_regions(start_region))
    while len(portal_mapping) > 0:

        portal2: Portal = Portal(region="", destination="", origin_letter="")
        for port in portal_mapping:
            if port.region == portal_mapping[0].destination and port.origin_letter == origin_letter_flip[portal_mapping[0].origin_letter]:
                portal2 = port
        if len(portal2.region) == 0:
            portal2 = Portal(region=portal_mapping[0].destination, destination="", origin_letter=origin_letter_flip[portal_mapping[0].origin_letter])
            portal_mapping.append(portal2)
        if len(portal2.region) == 0:
            raise Warning("CANNOT FIND PORTAL OF REGION "+portal_mapping[0].destination+" WITH LETTER OF "+origin_letter_flip[portal_mapping[0].origin_letter])
        connected_regions.update(add_dependent_regions(portal2.region))
        portal_pairs[portal_mapping[0]] = portal2
        portal_mapping.remove(portal2)
        portal_mapping.remove(portal_mapping[0])

    regions: Dict[str, Region] = {}

    for region_name, region_data in undertale_er_regions.items():
        regions[region_name] = Region(region_name, world.player, world.multiworld)

    set_er_region_rules(world, regions)

    for location_name, location_id in location_table.items():
        if regions.__contains__(location_table[location_name].er_region):
            region = regions[location_table[location_name].er_region]
            location = UndertaleERLocation(world.player, location_name, location_id.id, region)
            region.locations.append(location)

    for region in regions.values():
        world.multiworld.regions.append(region)

    undertale_er_add_extra_region_info(world, regions)

    return portal_pairs


def create_er_regions(world: "UndertaleWorld") -> Tuple[Dict[Portal, Portal], Dict[int, str]]:
    regions: Dict[str, Region] = {}
    portal_pairs: Dict[Portal, Portal] = pair_portals(world)

    # create our regions, give them hint text if they're in a spot where it makes sense to
    for region_name, region_data in undertale_er_regions.items():
        hint_text = "error"
        if region_data.hint == 1:
            for portal1, portal2 in portal_pairs.items():
                if portal1.region == region_name:
                    hint_text = hint_helper(portal2, portal_pairs)
                    break
                if portal2.region == region_name:
                    hint_text = hint_helper(portal1, portal_pairs)
                    break
            regions[region_name] = Region(region_name, world.player, world.multiworld, hint_text)
        elif region_data.hint == 2:
            for portal1, portal2 in portal_pairs.items():
                if portal1.scene() == undertale_er_regions[region_name].game_scene:
                    hint_text = hint_helper(portal2, portal_pairs)
                    break
                if portal2.scene() == undertale_er_regions[region_name].game_scene:
                    hint_text = hint_helper(portal1, portal_pairs)
                    break
            regions[region_name] = Region(region_name, world.player, world.multiworld, hint_text)
        else:
            regions[region_name] = Region(region_name, world.player, world.multiworld)

    set_er_region_rules(world, regions)

    er_hint_data: Dict[int, str] = {}
    for location_name, location_id in location_table.items():
        if regions.__contains__(location_table[location_name].er_region):
            region = regions[location_table[location_name].er_region]
            location = UndertaleERLocation(world.player, location_name, location_id.id, region)
            region.locations.append(location)
            if region.name == region.hint_text:
                continue
            er_hint_data[location.address] = region.hint_text
    
    create_randomized_entrances(portal_pairs, regions)

    for region in regions.values():
        world.multiworld.regions.append(region)

    undertale_er_add_extra_region_info(world, regions)

    portals_and_hints = (portal_pairs, er_hint_data)

    return portals_and_hints


def undertale_er_add_extra_region_info(world: "UndertaleWorld", regions: Dict[str, Region]):
    world.multiworld.register_indirect_condition(regions["room_torhouse2"], world.multiworld.get_entrance("Toriel Basement Block", world.player))

    paps_region = regions["room_tundra_paproom"]
    paps_location = UndertaleERLocation(world.player, "Papyrus Date", None, paps_region)
    paps_location.place_locked_item(UndertaleERItem("Papyrus Date", ItemClassification.progression, None, world.player))
    paps_region.locations.append(paps_location)

    undy_region = regions["room_water_undyneyard"]
    undy_location = UndertaleERLocation(world.player, "Undyne Date", None, undy_region)
    undy_location.place_locked_item(UndertaleERItem("Undyne Date", ItemClassification.progression, None, world.player))
    undy_region.locations.append(undy_location)

    undyf_region = regions["room_fire2"]
    undyf_location = UndertaleERLocation(world.player, "Undyne Fight (Event)", None, undyf_region)
    undyf_location.place_locked_item(UndertaleERItem("Undyne Fight (Event)", ItemClassification.progression, None, world.player))
    undyf_region.locations.append(undyf_location)

    papf_region = regions["room_fogroom"]
    papf_location = UndertaleERLocation(world.player, "Papyrus Fight (Event)", None, papf_region)
    papf_location.place_locked_item(UndertaleERItem("Papyrus Fight (Event)", ItemClassification.progression, None, world.player))
    papf_region.locations.append(papf_location)

    world.multiworld.completion_condition[world.player] = lambda state: state.has("Undyne Date", world.player) and state.has("Papyrus Date", world.player)

    return

    throne_region = regions["room_castle_throneroom"]
    throne_location = UndertaleERLocation(world.player, "Throne Room", None, throne_region)
    throne_location.place_locked_item(UndertaleERItem("Throne Room", ItemClassification.progression, None, world.player))
    throne_region.locations.append(throne_location)

    elev_lab_region = regions["room_truelab_castle_elevator"]
    elev_lab_location = UndertaleERLocation(world.player, "True Lab Elevator", None, elev_lab_region)
    elev_lab_location.place_locked_item(UndertaleERItem("True Lab Elevator", ItemClassification.progression, None, world.player))
    elev_lab_region.locations.append(elev_lab_location)

    elev_pow_region = regions["room_truelab_power"]
    elev_pow_location = UndertaleERLocation(world.player, "True Lab Power", None, elev_pow_region)
    elev_pow_location.place_locked_item(UndertaleERItem("True Lab Power", ItemClassification.progression, None, world.player))
    elev_pow_region.locations.append(elev_pow_location)

    if world.multiworld.route_required[world.player].current_key == "neutral":
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Throne Room", world.player)
    elif world.multiworld.route_required[world.player].current_key == "pacifist" or world.multiworld.route_required[world.player].current_key == "all_routes":
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Throne Room", world.player) and state.has("True Lab Power", world.player) and state.has("True Lab Elevator", world.player)
    elif world.multiworld.route_required[world.player].current_key == "genocide":
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Throne Room", world.player)


# pairing off portals, starting with dead ends
def pair_portals(world: "UndertaleWorld") -> Dict[Portal, Portal]:
    # separate the portals into dead ends and non-dead ends
    portal_pairs: Dict[Portal, Portal] = {}
    dead_ends: List[Portal] = []
    two_plus: List[Portal] = []

    # create separate lists for dead ends and non-dead ends
    for portal in portal_mapping:
        if undertale_er_regions[portal.region].dead_end:
            dead_ends.append(portal)
        else:
            two_plus.append(portal)

    portal_region_count = {}
    for portal in portal_mapping:
        if portal_region_count.keys().__contains__(undertale_er_regions[portal.region].game_scene):
            portal_region_count[undertale_er_regions[portal.region].game_scene] += len(add_dependent_regions(portal.region))
        else:
            portal_region_count[undertale_er_regions[portal.region].game_scene] = len(add_dependent_regions(portal.region))
        if portal_region_count.keys().__contains__(undertale_er_regions[portal.destination].game_scene):
            portal_region_count[undertale_er_regions[portal.destination].game_scene] += len(add_dependent_regions(portal.destination))
        else:
            portal_region_count[undertale_er_regions[portal.destination].game_scene] = len(add_dependent_regions(portal.destination))

    for portal in two_plus:
        if portal_region_count.keys().__contains__(undertale_er_regions[portal.region].game_scene):
            if portal_region_count[undertale_er_regions[portal.region].game_scene] <= 2:
                print("TWO_PLUS IS A DEAD END: "+portal.region+" "+portal.origin_letter+ " : "+str(portal_region_count[undertale_er_regions[portal.region].game_scene])+" connections")

    for portal in dead_ends:
        if portal_region_count.keys().__contains__(undertale_er_regions[portal.region].game_scene):
            if portal_region_count[undertale_er_regions[portal.region].game_scene] > 2:
                print("DEAD_END IS A TWO PLUS: "+portal.region+" "+portal.origin_letter+ " : "+str(portal_region_count[undertale_er_regions[portal.region].game_scene])+" connections")

    connected_regions: Set[str] = set()
    # make better start region stuff when/if implementing random start
    start_region = "room_area1"
    connected_regions.update(add_dependent_regions(start_region))

    # we want to start by making sure every region is accessible
    non_dead_end_regions = set()
    for region_name, region_info in undertale_er_regions.items():
        if not region_info.dead_end:
            non_dead_end_regions.add(region_name)

    world.random.shuffle(two_plus)
    check_success = 0
    portal1 = None
    portal2 = None
    names = []
    for item in portal_mapping:
        if Portal(item.destination, item.region, origin_letter_flip[item.origin_letter], item.destination+" "+origin_letter_flip[item.origin_letter]) not in portal_mapping:
            if item.region not in ["Ruins Entrance", "Snowdin Entrance", "Waterfall Entrance"]:
                if item.destination not in ["Ruins Entrance", "Snowdin Entrance", "Waterfall Entrance"]:
                    print("Could not find corresponding location for "+item.region+item.origin_letter)
        names.append(item.name)
    for item in names:
        if names.count(item) > 1:
            print("DUPLICATE PORTAL NAME "+item)
    while len(connected_regions) < len(non_dead_end_regions):
        # find a portal in an inaccessible region
        if check_success == 0:
            for portal in two_plus:
                if portal.region in connected_regions:
                    # if there's risk of self-locking, start over
                    if gate_before_switch(portal, two_plus):
                        world.random.shuffle(two_plus)
                        break
                    portal1 = portal
                    two_plus.remove(portal)
                    check_success = 1
                    break

        # then we find a portal in a connected region
        if check_success == 1:
            for portal in two_plus:
                if portal.region not in connected_regions:
                    # if there's risk of self-locking, shuffle and try again
                    if gate_before_switch(portal, two_plus):
                        world.random.shuffle(two_plus)
                        break
                    portal2 = portal
                    two_plus.remove(portal)
                    check_success = 2
                    break

        # once we have both portals, connect them and add the new region(s) to connected_regions
        if check_success == 2:
            connected_regions.update(add_dependent_regions(portal2.region))
            portal_pairs[portal1] = portal2
            check_success = 0
            world.random.shuffle(two_plus)

    # connect dead ends to random non-dead ends
    # none of the key events are in dead ends, so we don't need to do gate_before_switch
    print(len(dead_ends)-len(two_plus))
    pass
    while len(dead_ends) > 0:

        if len(two_plus) == 0:
            raise Exception("dead ends has more portals than it should")
        portal1 = two_plus.pop()
        portal2 = dead_ends.pop()
        portal_pairs[portal1] = portal2

    # then randomly connect the remaining portals to each other
    # every region is accessible, so gate_before_switch is not necessary
    while len(two_plus) > 1:
        portal1 = two_plus.pop()
        portal2 = two_plus.pop()
        portal_pairs[portal1] = portal2

    if len(two_plus) == 1:
        raise Exception("two plus had an odd number of portals, investigate this")

    for portal1, portal2 in portal_pairs.items():
        world.multiworld.spoiler.set_entrance(portal1.name, portal2.name, "both", world.player)

    return portal_pairs


# loop through our list of paired portals and make two-way connections
def create_randomized_entrances(portal_pairs: Dict[Portal, Portal], regions: Dict[str, Region]) \
        -> None:
    for portal1, portal2 in portal_pairs.items():
        region1 = regions[portal1.region]
        region2 = regions[portal2.region]
        region1.connect(region2, f"{portal1.name} -> {portal2.name}")


# loop through the static connections, return regions you can reach from this region
def add_dependent_regions(region_name: str) -> Set[str]:
    region_set = set()
    for origin_regions, destination_regions in dependent_regions.items():
        if region_name in origin_regions:
            # if you matched something in the first set, you get the regions in its paired set
            region_set.update(destination_regions)
            return region_set
    # if you didn't match anything in the first sets, just gives you the region
    region_set = {region_name}
    return region_set


# we're checking if an event-locked portal is being placed before the regions where its key(s) is/are
# doing this ensures the keys will not be locked behind the event-locked portal
def gate_before_switch(check_portal: Portal, two_plus: List[Portal]) -> bool:
    if check_portal.scene_destination() == "room_tundra_townS":
        i = 0
        for portal in two_plus:
            if portal.scene_destination() == "room_fogroomX":
                i += 1
                break
        if i == 1:
            return True
    if check_portal.scene_destination() == "room_basement1S":
        i = 0
        for portal in two_plus:
            if portal.scene_destination() == "room_torhouse2X":
                i += 1
            elif portal.scene_destination() == "room_torhouse2A":
                i += 1
        if i == 2:
            return True

    # false means you're good to place the portal
    return False


# check if a portal leads to a hallway. if it does, update the hint text accordingly
def hint_helper(portal: Portal, portal_pairs: Dict[Portal, Portal], hint_text: str = "") -> str:
    # start by setting it as the name of the portal, for the case we're not using the hallway helper
    if hint_text == "":
        hint_text = portal.name

    if portal.scene_destination() in hallway_helper:
        # if we have a hallway, we want the region rather than the portal name
        if hint_text == portal.name:
            hint_text = portal.region

        # search through the list for the other end of the hallway
        for portal1, portal2 in portal_pairs.items():
            if portal1.scene_destination() == hallway_helper[portal.scene_destination()]:
                # if we find that we have a chain of hallways, do recursion
                if portal2.scene_destination() in hallway_helper:
                    hint_region = portal2.region
                    hint_text = hint_region + " then " + hint_text
                    hint_text = hint_helper(portal2, portal_pairs, hint_text)
                else:
                    # if we didn't find a chain, get the portal name for the end of the chain
                    hint_text = portal2.name + " then " + hint_text
                    return hint_text
            # and then the same thing for the other portal, since we have to check each separately
            if portal2.scene_destination() == hallway_helper[portal.scene_destination()]:
                if portal1.scene_destination() in hallway_helper:
                    hint_region = portal1.region
                    hint_text = hint_region + " then " + hint_text
                    hint_text = hint_helper(portal1, portal_pairs, hint_text)
                else:
                    hint_text = portal1.name + " then " + hint_text
                    return hint_text
    return hint_text
