import string
from typing import TYPE_CHECKING
from BaseClasses import ItemClassification, Item, Location
from .Locations import exclusion_table
from .Locations import advancement_table as location_table
from .er_data import undertale_er_regions, portal_mapping, Portal
from .er_rules import set_er_region_rules
import Utils
from .entrance_rando import *

if TYPE_CHECKING:
    from . import UndertaleWorld


class UndertaleERItem(Item):
    game: str = "Undertale"


class UndertaleERLocation(Location):
    game: str = "Undertale"


def create_er_regions_vanilla(world: "UndertaleWorld"):
    temp_portal_mapping = portal_mapping.copy()

    regions: Dict[str, Region] = {}

    for region_name, region_data in undertale_er_regions.items():
        if region_name != "room_fire_labelevator" or world.options.route_required == "all_routes" \
                or world.options.route_required == "pacifist":
            regions[region_name] = Region(region_name, world.player, world.multiworld)

    for location_name, location_id in location_table.items():
        if regions.__contains__(location_table[location_name].er_region) and (
                location_name not in exclusion_table["NoKills"] or (world.options.kill_sanity and (
                world.options.route_required == "genocide" or world.options.route_required == "all_routes"))) and (
                location_name not in exclusion_table["NoStats"] or (world.options.rando_stats and (
                world.options.route_required == "genocide" or world.options.route_required == "all_routes"))) and (
                location_name not in exclusion_table["NoLove"] or (world.options.rando_love and (
                world.options.route_required == "genocide" or world.options.route_required == "all_routes"))) and (
                location_name not in exclusion_table["NoSpare"]) and \
                location_name not in exclusion_table[world.options.route_required.current_key]:
            region = regions[location_table[location_name].er_region]
            location = UndertaleERLocation(world.player, location_name, location_id.id, region)
            region.locations.append(location)

    for region_name, region_data in undertale_er_regions.items():
        if world.options.spare_sanity and world.options.route_required != "genocide":
            if region_name == "Ruins Grind Rooms":
                regions[region_name].locations += [
                    UndertaleERLocation(world.player, "Ruins Spare " + str(i + 1), 78013 + i, regions[region_name])
                    for i in range(world.options.spare_sanity_max.value)]
            elif region_name == "Snowdin Grind Rooms":
                regions[region_name].locations += [
                    UndertaleERLocation(world.player, "Snowdin Spare " + str(i + 1), 78113 + i,
                                        regions[region_name]) for i in
                    range(world.options.spare_sanity_max.value)]
            elif region_name == "Waterfall Grind Rooms":
                regions[region_name].locations += [
                    UndertaleERLocation(world.player, "Waterfall Spare " + str(i + 1), 78213 + i,
                                        regions[region_name]) for i in
                    range(world.options.spare_sanity_max.value)]
            elif region_name == "Hotland Grind Rooms":
                regions[region_name].locations += [
                    UndertaleERLocation(world.player, "Hotland Spare " + str(i + 1), 78313 + i,
                                        regions[region_name]) for i in
                    range(world.options.spare_sanity_max.value)]

    for region in regions.values():
        world.multiworld.regions.append(region)

    set_er_region_rules(world)

    while len(temp_portal_mapping) > 0:
        world.get_region(temp_portal_mapping[0].region).add_exits({temp_portal_mapping[0].destination: temp_portal_mapping[0].destination_string()})
        temp_portal_mapping.remove(temp_portal_mapping[0])

    undertale_er_add_extra_region_info(world, regions)


def assemble_er(world: "UndertaleWorld") -> List[Tuple[str, str]]:
        for item in portal_mapping:
            disconnect_entrance_for_randomization(world.get_entrance(item.destination_string()))

        place_state = randomize_entrances(world, True, {0: [0]}).pairings

        # state = world.multiworld.get_all_state(False)
        # state.update_reachable_regions(world.player)
        # Utils.visualize_regions(world.multiworld.get_region("Menu", world.player), "undertale_check_player_" +
        #                         str(world.multiworld.player_name[world.player]) + ".puml", show_entrance_names=True)

        return place_state


def undertale_er_add_extra_region_info(world: "UndertaleWorld", regions: Dict[str, Region]):
    world.multiworld.register_indirect_condition(regions["room_sanscorridor"],
                                                 world.multiworld.get_entrance("Lab Elevator Entrance", world.player))

    world.multiworld.register_indirect_condition(regions["room_fire_shootguy_2"],
                                                 world.multiworld.get_entrance("Fire Door 1 Block", world.player))
    world.multiworld.register_indirect_condition(regions["room_fire_shootguy_1"],
                                                 world.multiworld.get_entrance("Fire Door 1 Block", world.player))

    world.multiworld.register_indirect_condition(regions["room_fire_shootguy_3"],
                                                 world.multiworld.get_entrance("Fire Door 2 Block", world.player))
    world.multiworld.register_indirect_condition(regions["room_fire_shootguy_4"],
                                                 world.multiworld.get_entrance("Fire Door 2 Block", world.player))

    if world.options.route_required.current_key == "pacifist" or \
            world.options.route_required.current_key == "all_routes":
        paps_region = regions["room_tundra_paproom"]
        paps_location = UndertaleERLocation(world.player, "Papyrus Date (Event)", None, paps_region)
        paps_location.place_locked_item(UndertaleERItem("Papyrus Date (Event)", ItemClassification.progression, None,
                                                        world.player))
        paps_region.locations.append(paps_location)

        undy_region = regions["room_water_undyneyard"]
        undy_location = UndertaleERLocation(world.player, "Undyne Date (Event)", None, undy_region)
        undy_location.place_locked_item(UndertaleERItem("Undyne Date (Event)", ItemClassification.progression, None,
                                                        world.player))
        undy_region.locations.append(undy_location)

        alph_region = regions["room_fire_prelab"]
        alph_location = UndertaleERLocation(world.player, "Alphys Date (Event)", None, alph_region)
        alph_location.place_locked_item(UndertaleERItem("Alphys Date (Event)", ItemClassification.progression, None,
                                                        world.player))
        alph_region.locations.append(alph_location)

        lab_region = regions["room_fire_labelevator"]
        lab_location = UndertaleERLocation(world.player, "True Lab Entrance (Event)", None, lab_region)
        lab_location.place_locked_item(UndertaleERItem("True Lab Entrance (Event)", ItemClassification.progression, None,
                                                       world.player))
        lab_region.locations.append(lab_location)

    undyf_region = regions["room_fire2"]
    undyf_location = UndertaleERLocation(world.player, "Undyne Fight (Event)", None, undyf_region)
    undyf_location.place_locked_item(UndertaleERItem("Undyne Fight (Event)", ItemClassification.progression, None,
                                                     world.player))
    undyf_region.locations.append(undyf_location)

    papf_region = regions["room_fogroom"]
    papf_location = UndertaleERLocation(world.player, "Papyrus Fight (Event)", None, papf_region)
    papf_location.place_locked_item(UndertaleERItem("Papyrus Fight (Event)", ItemClassification.progression, None,
                                                    world.player))
    papf_region.locations.append(papf_location)

    throne_region = regions["room_castle_throneroom"]
    throne_location = UndertaleERLocation(world.player, "Throne Room (Event)", None, throne_region)
    throne_location.place_locked_item(UndertaleERItem("Throne Room (Event)", ItemClassification.progression, None,
                                                      world.player))
    throne_region.locations.append(throne_location)

    if world.options.route_required.current_key == "neutral":
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Throne Room (Event)", world.player)
    elif world.options.route_required.current_key == "pacifist" or \
            world.options.route_required.current_key == "all_routes":
        world.multiworld.completion_condition[world.player] = lambda state: \
            state.has("Throne Room (Event)", world.player) and state.has("True Lab Entrance (Event)", world.player)
    elif world.options.route_required.current_key == "genocide":
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Throne Room (Event)", world.player)
