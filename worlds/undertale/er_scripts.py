from typing import Dict, List, Set, Tuple, TYPE_CHECKING
from BaseClasses import Region, ItemClassification, Item, Location
from .Locations import exclusion_table
from .Locations import advancement_table as location_table
from .er_data import Portal, undertale_er_regions, portal_mapping, dependent_regions, hallway_helper
from .er_rules import set_er_region_rules
import Utils

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
    temp_portal_mapping = portal_mapping.copy()
    for item in temp_portal_mapping:
        if Portal(item.destination, item.region, origin_letter_flip[item.origin_letter], item.destination+" "+origin_letter_flip[item.origin_letter]) not in temp_portal_mapping:
            if item.region not in ["Ruins Entrance", "Snowdin Entrance", "Waterfall Entrance",
                                            "Hotland Entrance", "New Home Entrance"]:
                if item.destination not in ["Ruins Entrance", "Snowdin Entrance", "Waterfall Entrance",
                                            "Hotland Entrance", "New Home Entrance"]:
                    print("Could not find corresponding location for "+item.region+item.origin_letter)
    while len(temp_portal_mapping) > 0:

        portal2: Portal = Portal(region="", destination="", origin_letter="")
        if temp_portal_mapping[0].region not in ["Ruins Entrance", "Snowdin Entrance", "Waterfall Entrance",
                                            "Hotland Entrance", "New Home Entrance"]:
            if temp_portal_mapping[0].destination not in ["Ruins Entrance", "Snowdin Entrance", "Waterfall Entrance",
                                                     "Hotland Entrance", "New Home Entrance"]:
                for port in temp_portal_mapping:
                    if port.region == temp_portal_mapping[0].destination and port.origin_letter == origin_letter_flip[temp_portal_mapping[0].origin_letter]:
                        portal2 = port
        if len(portal2.region) == 0:
            if temp_portal_mapping[0].region not in ["Ruins Entrance", "Snowdin Entrance", "Waterfall Entrance", "Hotland Entrance", "New Home Entrance"]:
                if temp_portal_mapping[0].destination not in ["Ruins Entrance", "Snowdin Entrance", "Waterfall Entrance", "Hotland Entrance", "New Home Entrance"]:
                    raise Warning("CANNOT FIND PORTAL OF REGION "+temp_portal_mapping[0].destination+" WITH LETTER OF "+origin_letter_flip[temp_portal_mapping[0].origin_letter])
                else:
                    for port in temp_portal_mapping:
                        if port.region == temp_portal_mapping[0].destination:
                            portal2 = port
            else:
                for port in temp_portal_mapping:
                    if port.destination == temp_portal_mapping[0].region:
                        portal2 = port

        # print(temp_portal_mapping[0].name+" <-> "+portal2.name)
        connected_regions.update(add_dependent_regions(portal2.region))
        portal_pairs[temp_portal_mapping[0]] = portal2
        temp_portal_mapping.remove(portal2)
        temp_portal_mapping.remove(temp_portal_mapping[0])

    regions: Dict[str, Region] = {}

    for region_name, region_data in undertale_er_regions.items():
        regions[region_name] = Region(region_name, world.player, world.multiworld)

    set_er_region_rules(world, regions)

    for location_name, location_id in location_table.items():
        if regions.__contains__(location_table[location_name].er_region) and (location_name not in exclusion_table["NoKills"] or (world.multiworld.kill_sanity[world.player] and (world.multiworld.route_required[world.player] == "genocide" or world.multiworld.route_required[world.player] == "all_routes"))) and (location_name not in exclusion_table["NoStats"] or (world.multiworld.rando_stats[world.player] and (world.multiworld.route_required[world.player] == "genocide" or world.multiworld.route_required[world.player] == "all_routes"))) and (location_name not in exclusion_table["NoLove"] or (world.multiworld.rando_love[world.player] and (world.multiworld.route_required[world.player] == "genocide" or world.multiworld.route_required[world.player] == "all_routes"))) and (location_name not in exclusion_table["NoSpare"]) and location_name not in exclusion_table[world.multiworld.route_required[world.player].current_key]:
            region = regions[location_table[location_name].er_region]
            location = UndertaleERLocation(world.player, location_name, location_id.id, region)
            region.locations.append(location)

    for region_name, region_data in undertale_er_regions.items():
        if world.multiworld.spare_sanity[world.player] and world.multiworld.route_required[world.player] != "genocide":
            if region_name == "Ruins Grind Rooms":
                regions[region_name].locations += [
                    UndertaleERLocation(world.player, "Ruins Spare " + str(i + 1), 78013 + i, regions[region_name])
                    for i in range(world.multiworld.spare_sanity_max[world.player].value)]
            elif region_name == "Snowdin Grind Rooms":
                regions[region_name].locations += [
                    UndertaleERLocation(world.player, "Snowdin Spare " + str(i + 1), 78113 + i,
                                        regions[region_name]) for i in
                    range(world.multiworld.spare_sanity_max[world.player].value)]
            elif region_name == "Waterfall Grind Rooms":
                regions[region_name].locations += [
                        UndertaleERLocation(world.player, "Waterfall Spare " + str(i + 1), 78213 + i,
                                            regions[region_name]) for i in
                        range(world.multiworld.spare_sanity_max[world.player].value)]
            elif region_name == "Hotland Grind Rooms":
                regions[region_name].locations += [
                        UndertaleERLocation(world.player, "Hotland Spare " + str(i + 1), 78313 + i,
                                            regions[region_name]) for i in
                        range(world.multiworld.spare_sanity_max[world.player].value)]

    create_randomized_entrances(portal_pairs, regions)

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
        if regions.__contains__(location_table[location_name].er_region) and (location_name not in exclusion_table["NoKills"] or (world.multiworld.kill_sanity[world.player] and (world.multiworld.route_required[world.player] == "genocide" or world.multiworld.route_required[world.player] == "all_routes"))) and (location_name not in exclusion_table["NoStats"] or (world.multiworld.rando_stats[world.player] and (world.multiworld.route_required[world.player] == "genocide" or world.multiworld.route_required[world.player] == "all_routes"))) and (location_name not in exclusion_table["NoLove"] or (world.multiworld.rando_love[world.player] and (world.multiworld.route_required[world.player] == "genocide" or world.multiworld.route_required[world.player] == "all_routes"))) and (location_name not in exclusion_table["NoSpare"]) and location_name not in exclusion_table[world.multiworld.route_required[world.player].current_key]:
            region = regions[location_table[location_name].er_region]
            location = UndertaleERLocation(world.player, location_name, location_id.id, region)
            region.locations.append(location)
            if region.name == region.hint_text:
                continue
            er_hint_data[location.address] = region.hint_text

    for region_name, region_data in undertale_er_regions.items():
        if world.multiworld.spare_sanity[world.player] and world.multiworld.route_required[world.player] != "genocide":
            if region_name == "Ruins Grind Rooms":
                regions[region_name].locations += [UndertaleERLocation(world.player, "Ruins Spare "+str(i+1), 78013+i, regions[region_name]) for i in range(world.multiworld.spare_sanity_max[world.player].value)]
            elif region_name == "Snowdin Grind Rooms":
                regions[region_name].locations += [UndertaleERLocation(world.player, "Snowdin Spare "+str(i+1), 78113+i, regions[region_name]) for i in range(world.multiworld.spare_sanity_max[world.player].value)]
            elif region_name == "Waterfall Grind Rooms":
                regions[region_name].locations += [UndertaleERLocation(world.player, "Waterfall Spare "+str(i+1), 78213+i, regions[region_name]) for i in range(world.multiworld.spare_sanity_max[world.player].value)]
            elif region_name == "Hotland Grind Rooms":
                regions[region_name].locations += [UndertaleERLocation(world.player, "Hotland Spare "+str(i+1), 78313+i, regions[region_name]) for i in range(world.multiworld.spare_sanity_max[world.player].value)]
    
    create_randomized_entrances(portal_pairs, regions)

    for region in regions.values():
        world.multiworld.regions.append(region)

    undertale_er_add_extra_region_info(world, regions)

    portals_and_hints = (portal_pairs, er_hint_data)

    return portals_and_hints


def undertale_er_add_extra_region_info(world: "UndertaleWorld", regions: Dict[str, Region]):
    world.multiworld.register_indirect_condition(regions["room_fire_shootguy_2"], world.multiworld.get_entrance("Fire Door 1 Block", world.player))
    world.multiworld.register_indirect_condition(regions["room_fire_shootguy_1"], world.multiworld.get_entrance("Fire Door 1 Block", world.player))

    world.multiworld.register_indirect_condition(regions["room_fire_shootguy_3"], world.multiworld.get_entrance("Fire Door 2 Block", world.player))
    world.multiworld.register_indirect_condition(regions["room_fire_shootguy_4"], world.multiworld.get_entrance("Fire Door 2 Block", world.player))

    if world.multiworld.route_required[world.player].current_key == "pacifist" or world.multiworld.route_required[world.player].current_key == "all_routes":

        paps_region = regions["room_tundra_paproom"]
        paps_location = UndertaleERLocation(world.player, "Papyrus Date", None, paps_region)
        paps_location.place_locked_item(UndertaleERItem("Papyrus Date", ItemClassification.progression, None, world.player))
        paps_region.locations.append(paps_location)

        undy_region = regions["room_water_undyneyard"]
        undy_location = UndertaleERLocation(world.player, "Undyne Date", None, undy_region)
        undy_location.place_locked_item(UndertaleERItem("Undyne Date", ItemClassification.progression, None, world.player))
        undy_region.locations.append(undy_location)

        alph_region = regions["room_fire_prelab"]
        alph_location = UndertaleERLocation(world.player, "Alphys Date", None, alph_region)
        alph_location.place_locked_item(UndertaleERItem("Alphys Date", ItemClassification.progression, None, world.player))
        alph_region.locations.append(alph_location)

        lab_region = regions["room_fire_labelevator"]
        lab_location = UndertaleERLocation(world.player, "True Lab Entrance", None, lab_region)
        lab_location.place_locked_item(UndertaleERItem("True Lab Entrance", ItemClassification.progression, None, world.player))
        lab_region.locations.append(lab_location)

    undyf_region = regions["room_fire2"]
    undyf_location = UndertaleERLocation(world.player, "Undyne Fight (Event)", None, undyf_region)
    undyf_location.place_locked_item(UndertaleERItem("Undyne Fight (Event)", ItemClassification.progression, None, world.player))
    undyf_region.locations.append(undyf_location)

    papf_region = regions["room_fogroom"]
    papf_location = UndertaleERLocation(world.player, "Papyrus Fight (Event)", None, papf_region)
    papf_location.place_locked_item(UndertaleERItem("Papyrus Fight (Event)", ItemClassification.progression, None, world.player))
    papf_region.locations.append(papf_location)

    throne_region = regions["room_castle_throneroom"]
    throne_location = UndertaleERLocation(world.player, "Throne Room", None, throne_region)
    throne_location.place_locked_item(UndertaleERItem("Throne Room", ItemClassification.progression, None, world.player))
    throne_region.locations.append(throne_location)

    if world.multiworld.route_required[world.player].current_key == "neutral":
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Throne Room", world.player)
    elif world.multiworld.route_required[world.player].current_key == "pacifist" or world.multiworld.route_required[world.player].current_key == "all_routes":
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Throne Room", world.player) and state.has("True Lab Entrance", world.player)
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
            portal_region_count[undertale_er_regions[portal.region].game_scene] += 1
        else:
            portal_region_count[undertale_er_regions[portal.region].game_scene] = 1

    for portal in portal_mapping:
        if portal_region_count.keys().__contains__(undertale_er_regions[portal.region].game_scene):
            if portal_region_count[undertale_er_regions[portal.region].game_scene] > 0:
                if portal_region_count[undertale_er_regions[portal.region].game_scene] <= 1 and portal in two_plus and not undertale_er_regions[portal.region].dead_end_override:
                    pass
                    # print("TWO_PLUS IS A DEAD END: "+portal.region+" "+portal.origin_letter+" : "+str(portal_region_count[undertale_er_regions[portal.region].game_scene])+" connections")
                if portal_region_count[undertale_er_regions[portal.region].game_scene] > 1 and portal in dead_ends and not undertale_er_regions[portal.region].dead_end_override:
                    pass
                    # print("DEAD_END IS A TWO PLUS: "+portal.region+" "+portal.origin_letter + " : "+str(portal_region_count[undertale_er_regions[portal.region].game_scene])+" connections")

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
            if item.region not in ["Ruins Entrance", "Snowdin Entrance", "Waterfall Entrance",
                                            "Hotland Entrance", "New Home Entrance"]:
                if item.destination not in ["Ruins Entrance", "Snowdin Entrance", "Waterfall Entrance",
                                            "Hotland Entrance", "New Home Entrance"]:
                    print("Could not find corresponding location for "+item.region+item.origin_letter)
        names.append(item.name)
    for item in names:
        if names.count(item) > 1:
            print("DUPLICATE PORTAL NAME "+item)
    while len(connected_regions) < len(non_dead_end_regions):
        # then we find a portal in a connected region
        if check_success == 0:
            for portal in two_plus:
                if portal.region in connected_regions:
                    # if there's risk of self-locking, start over
                    if gate_before_switch(portal, two_plus, dead_ends):
                        world.random.shuffle(two_plus)
                        break
                    portal1 = portal
                    two_plus.remove(portal)
                    check_success = 1
                    break

        # find a portal in an inaccessible region
        if check_success == 1:
            for portal in two_plus:
                if portal.region not in connected_regions:
                    # if there's risk of self-locking, shuffle and try again
                    if gate_before_switch(portal, two_plus, dead_ends):
                        world.random.shuffle(two_plus)
                        break
                    portal2 = portal
                    two_plus.remove(portal)
                    check_success = 2
                    break

        if check_success == 1:
            print(non_dead_end_regions.difference(connected_regions).__str__())

        # once we have both portals, connect them and add the new region(s) to connected_regions
        if check_success == 2:
            connected_regions.update(add_dependent_regions(portal2.region))
            portal_pairs[portal1] = portal2
            check_success = 0
            for portal in dead_ends:
                if portal.region in connected_regions:
                    two_plus.append(portal)
                    dead_ends.remove(portal)
            for regi in connected_regions:
                if regi not in non_dead_end_regions:
                    non_dead_end_regions.add(regi)
            world.random.shuffle(two_plus)

    # connect dead ends to random non-dead ends
    # print(len(dead_ends)-len(two_plus))
    if len(dead_ends)-len(two_plus) > 0:
        pass
    while len(dead_ends) > 0:
        if gate_before_switch(two_plus[-1], two_plus, dead_ends):
            world.random.shuffle(two_plus)
            continue
        if gate_before_switch(dead_ends[-1], two_plus, dead_ends):
            world.random.shuffle(dead_ends)
            continue

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
        region2.connect(region1, f"{portal2.name} -> {portal1.name}")


# loop through the static connections, return regions you can reach from this region
def add_dependent_regions(region_name: str) -> Set[str]:
    region_set = set()
    for origin_regions, destination_regions in dependent_regions.items():
        if region_name in origin_regions:
            # if you matched something in the first set, you get the regions in its paired set
            # print(region_name+": "+destination_regions.__str__())
            region_set.update(destination_regions)
            return region_set
    # if you didn't match anything in the first sets, just gives you the region
    region_set = {region_name}
    return region_set


# we're checking if an event-locked portal is being placed before the regions where its key(s) is/are
# doing this ensures the keys will not be locked behind the event-locked portal
def gate_before_switch(check_portal: Portal, two_plus: List[Portal], dead_ends: List[Portal]) -> bool:
    if check_portal.region == "Fire Door 1":
        i = j = 0
        for portal in two_plus+dead_ends:
            if portal.region == "room_fire_shootguy_2":
                i += 1
            if portal.region == "room_fire_shootguy_1":
                j += 1
        if i == 1 and j == 1:
            return True
    if check_portal.region == "Fire Door 2":
        i = j = 0
        for portal in two_plus+dead_ends:
            if portal.region == "room_fire_shootguy_3":
                i += 1
            if portal.region == "room_fire_shootguy_4":
                j += 1
        if i == 1 and j == 1:
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
