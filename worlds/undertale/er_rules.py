from typing import Dict, TYPE_CHECKING
from worlds.generic.Rules import set_rule
from .Rules import _undertale_is_route, _undertale_exp_available, _undertale_return_reachable_level, _undertale_has_keys
from BaseClasses import Region
import math

if TYPE_CHECKING:
    from . import UndertaleWorld


def set_er_region_rules(world: "UndertaleWorld", regions: Dict[str, Region]) -> None:
    player = world.player

    regions["Menu"].connect(
        connecting_region=regions["room_area1"])

    regions["room_water_undynebridge"].connect(
        connecting_region=regions["room_water_undynebridgeend"])

    regions["Trash Zone Fall"].connect(
        connecting_region=regions["room_water_undynebridgeend"])

    regions["room_water_undynebridgeend"].connect(
        connecting_region=regions["Trash Zone Fall"])

    regions["room_water20"].connect(
        connecting_region=regions["room_water21"])

    regions["room_water21"].connect(
        connecting_region=regions["room_water20"])

    regions["room_water21"].connect(
        connecting_region=regions["room_water_undynefinal"])

    regions["room_water_undynefinal"].connect(
        connecting_region=regions["room_water21"])

    regions["room_water_undynefinal"].connect(
        connecting_region=regions["room_fire2"])

    regions["room_fire2"].connect(
        connecting_region=regions["room_water_undynefinal"])

    regions["Ruins Exit"].connect(
        connecting_region=regions["room_area1"])

    regions["Hotland Exit"].connect(
        connecting_region=regions["room_area1"])

    regions["Snowdin Exit"].connect(
        connecting_region=regions["room_area1"])

    regions["Waterfall Exit"].connect(
        connecting_region=regions["room_area1"])

    regions["room_water_waterfall4"].connect(
        connecting_region=regions["Monster Kid Raised Ledge"])

    regions["room_water7"].connect(
        connecting_region=regions["Room Water 7 One Way"])

    regions["room_tundra_sanshouse"].connect(
        connecting_region=regions["Papyrus Rocks"],
        rule=lambda state: state.has("Complete Skeleton", player) or not (_undertale_is_route(world, 1)))

    regions["Papyrus Rocks"].connect(
        connecting_region=regions["room_tundra_sanshouse"],
        rule=lambda state: state.has("Complete Skeleton", player) or not (_undertale_is_route(world, 1)))

    regions["room_water_friendlyhub"].connect(
        connecting_region=regions["Undyne Rocks"],
        rule=lambda state: state.has("Fish", player) or not (_undertale_is_route(world, 1)))

    regions["Undyne Rocks"].connect(
        connecting_region=regions["room_water_friendlyhub"],
        rule=lambda state: state.has("Fish", player) or not (_undertale_is_route(world, 1)))

    regions["room_area1"].connect(
        connecting_region=regions["Ruins Entrance"],
        rule=lambda state: state.has("Ruins Key", player))

    regions["Ruins Entrance"].connect(
        connecting_region=regions["room_area1"])

    regions["room_area1"].connect(
        connecting_region=regions["Snowdin Entrance"],
        rule=lambda state: state.has("Snowdin Key", player))

    regions["Snowdin Entrance"].connect(
        connecting_region=regions["room_area1"])

    regions["room_area1"].connect(
        connecting_region=regions["Waterfall Entrance"],
        rule=lambda state: state.has("Waterfall Key", player))

    regions["Waterfall Entrance"].connect(
        connecting_region=regions["room_area1"])

    regions["room_area1"].connect(
        connecting_region=regions["Hotland Entrance"],
        rule=lambda state: state.has("Hotland Key", player))

    regions["Hotland Entrance"].connect(
        connecting_region=regions["room_area1"])

    regions["room_area1"].connect(
        connecting_region=regions["New Home Entrance"])

    regions["New Home Entrance"].connect(
        connecting_region=regions["room_area1"])

    regions["Trash Zone Fall"].connect(
        connecting_region=regions["room_water_trashzone1"])

    regions["Menu"].connect(
        connecting_region=regions["???"])

    regions["Ruins Pit Circle B"].connect(
        connecting_region=regions["room_ruins15E"])

    regions["Ruins Pit Circle C"].connect(
        connecting_region=regions["room_ruins15E"])

    regions["Ruins Pit Circle D"].connect(
        connecting_region=regions["room_ruins15E"])

    regions["Fire Door 1"].connect(
        connecting_region=regions["room_fire7"])

    regions["Fire Door 2"].connect(
        connecting_region=regions["room_fire_walkandbranch2"])

    regions["room_fire_turn"].connect(
        connecting_region=regions["Fire Turn Part 2"])

    regions["room_fire_elevator"].connect(
        connecting_region=regions["room_fire_elevator_l1"])

    regions["room_fire_elevator"].connect(
        connecting_region=regions["room_fire_elevator_l2"])

    regions["room_fire_elevator"].connect(
        connecting_region=regions["room_fire_elevator_l3"])

    regions["room_fire_elevator"].connect(
        connecting_region=regions["room_fire_elevator_r1"])

    regions["room_fire_elevator"].connect(
        connecting_region=regions["room_fire_elevator_r2"])

    regions["room_fire_elevator"].connect(
        connecting_region=regions["room_fire_elevator_r3"])

    regions["room_fire_elevator_l1"].connect(
        connecting_region=regions["room_fire_elevator"])

    regions["room_fire_elevator_l2"].connect(
        connecting_region=regions["room_fire_elevator"])

    regions["room_fire_elevator_l3"].connect(
        connecting_region=regions["room_fire_elevator"])

    regions["room_fire_elevator_r1"].connect(
        connecting_region=regions["room_fire_elevator"])

    regions["room_fire_elevator_r2"].connect(
        connecting_region=regions["room_fire_elevator"])

    regions["room_fire_elevator_r3"].connect(
        connecting_region=regions["room_fire_elevator"])

    regions["room_water5"].connect(
        connecting_region=regions["water bridge puzzle 2 after"])

    regions["room_water_bridgepuzz1"].connect(
        connecting_region=regions["water bridge puzzle after"])

    regions["room_tundra_snowpuzz"].connect(
        connecting_region=regions["Snow Puzz After Puzzle"])

    regions["room_ruins15B"].connect(
        connecting_region=regions["Ruins 15B Past Puzzles"])

    regions["room_ruins15C"].connect(
        connecting_region=regions["Ruins 15C Past Puzzles"])

    regions["room_ruins15D"].connect(
        connecting_region=regions["Ruins 15D Past Puzzles"])

    regions["room_tundra_xoxosmall"].connect(
        connecting_region=regions["small xoxo after puzzle"])

    regions["room_tundra_xoxopuzz"].connect(
        connecting_region=regions["xoxo puzz after puzzle"])

    regions["room_fire_core_metttest"].connect(
        connecting_region=regions["room_fire_core_final"],
        rule=lambda state: (not bool(world.options.kill_sanity.value) or not _undertale_is_route(world, 2) or state.has(
            "Hotland Population Pack", player, math.ceil(40 / world.options.kill_sanity_pack_size.value))))

    regions["Metta Entrance"].connect(
        connecting_region=regions["room_fire_core_premett"],
        rule=lambda state: state.has("Mettaton Plush", player))

    regions["room_water_blookyard"].connect(
        connecting_region=regions["hapsta door"],
        rule=lambda state: state.has("Mystery Key", player))

    regions["hapsta door"].connect(
        connecting_region=regions["room_water_blookyard"])

    regions["room_fire_core_premett"].connect(
        connecting_region=regions["Metta Entrance"],
        rule=lambda state: state.has("Mettaton Plush", player))

    regions["room_water8"].connect(
        connecting_region=regions["room_water9"])

    regions["room_water9"].connect(
        connecting_region=regions["room_water8"])

    regions["Metta Entrance"].connect(
        connecting_region=regions["room_fire_core_metttest"])

    regions["room_fire_core_metttest"].connect(
        connecting_region=regions["Metta Entrance"])

    regions["room_fire_core_final"].connect(
        connecting_region=regions["room_fire_core_metttest"])

    regions["room_fire_core_final"].connect(
        connecting_region=regions["Hotland Exit"])

    regions["Hotland Exit"].connect(
        connecting_region=regions["room_fire_core_final"])

    regions["room_asghouse1"].connect(
        connecting_region=regions["room_basement1_final"],
        rule=lambda state: _undertale_has_keys(state, world, player) and (
                                   not bool(world.options.kill_sanity.value) or not _undertale_is_route(world, 2)
                                   or state.has("Hotland Population Pack", player,
                                                math.ceil(40 / world.options.kill_sanity_pack_size.value))
                           ))

    regions["room_basement1_final"].connect(
        connecting_region=regions["room_asghouse1"])

    regions["room_basement1_final"].connect(
        connecting_region=regions["room_basement2_final"])

    regions["room_basement2_final"].connect(
        connecting_region=regions["room_basement1_final"])

    regions["room_basement2_final"].connect(
        connecting_region=regions["room_basement3_final"])

    regions["room_basement3_final"].connect(
        connecting_region=regions["room_basement2_final"])

    regions["room_ruins3"].connect(
        connecting_region=regions["Ruins 3 Past Puzzles"])

    regions["room_ruins14"].connect(
        connecting_region=regions["Ruins 14 Past Puzzles"])

    regions["room_ruins15A"].connect(
        connecting_region=regions["Ruins 15A Past Puzzles"])

    regions["room_ruins9"].connect(
        connecting_region=regions["Ruins 9 Past Puzzles"])

    regions["room_ruins11"].connect(
        connecting_region=regions["Ruins 11 Past Puzzles"])

    regions["room_basement3_final"].connect(
        connecting_region=regions["room_basement4_final"])

    regions["room_basement4_final"].connect(
        connecting_region=regions["room_basement3_final"])

    regions["room_basement4_final"].connect(
        connecting_region=regions["room_lastruins_corridor"])

    regions["room_lastruins_corridor"].connect(
        connecting_region=regions["room_basement4_final"])

    regions["room_lastruins_corridor"].connect(
        connecting_region=regions["room_sanscorridor"])

    regions["room_sanscorridor"].connect(
        connecting_region=regions["room_lastruins_corridor"])

    regions["room_fire_lab1"].connect(
        connecting_region=regions["room_fire_labelevator"],
        rule=lambda state: (state.has("Alphys Date (Event)", player) and _undertale_has_keys(state, world,
                                                                                     player) and state.has(
            "DT Extractor", player)) or _undertale_is_route(world, 2),
        name="Lab Elevator Entrance")

    regions["room_sanscorridor"].connect(
        connecting_region=regions["room_castle_finalshoehorn"],
        rule=lambda state: (state.has("Jump", player) or not _undertale_is_route(world, 2)))

    regions["room_castle_finalshoehorn"].connect(
        connecting_region=regions["room_sanscorridor"])

    regions["room_fire10"].connect(
        connecting_region=regions["Fire 10 One Way"])

    regions["room_castle_finalshoehorn"].connect(
        connecting_region=regions["room_castle_coffins1"])

    regions["room_castle_finalshoehorn"].connect(
        connecting_region=regions["room_castle_throneroom"])

    regions["room_castle_throneroom"].connect(
        connecting_region=regions["room_castle_finalshoehorn"])

    regions["room_castle_coffins1"].connect(
        connecting_region=regions["room_castle_finalshoehorn"])

    regions["room_castle_coffins1"].connect(
        connecting_region=regions["room_castle_coffins2"])

    regions["room_castle_coffins2"].connect(
        connecting_region=regions["room_castle_coffins1"])

    regions["Bed Door One-way"].connect(
        connecting_region=regions["room_fire_hoteldoors"])

    regions["room_fire_hotellobby"].connect(
        connecting_region=regions["room_fire_hotelbed"])

    regions["room_fire_core_bottomleft"].connect(
        connecting_region=regions["Hotland Grind Rooms"])
    regions["room_fire_core_topleft"].connect(
        connecting_region=regions["Hotland Grind Rooms"])
    regions["room_fire_core_topright"].connect(
        connecting_region=regions["Hotland Grind Rooms"])
    regions["room_fire_core_bottomright"].connect(
        connecting_region=regions["Hotland Grind Rooms"])
    regions["room_fire_core_center"].connect(
        connecting_region=regions["Hotland Grind Rooms"])
    regions["room_fire_core_bridge"].connect(
        connecting_region=regions["Hotland Grind Rooms"])
    regions["room_fire5"].connect(
        connecting_region=regions["Hotland Grind Rooms"])
    regions["room_fire6"].connect(
        connecting_region=regions["Hotland Grind Rooms"])
    regions["room_fire_walkandbranch"].connect(
        connecting_region=regions["Hotland Grind Rooms"])
    regions["room_fire_preshootguy4"].connect(
        connecting_region=regions["Hotland Grind Rooms"])
    regions["room_water5"].connect(
        connecting_region=regions["Waterfall Grind Rooms"])
    regions["room_water6"].connect(
        connecting_region=regions["Waterfall Grind Rooms"])
    regions["room_water12"].connect(
        connecting_region=regions["Waterfall Grind Rooms"])
    regions["room_water15"].connect(
        connecting_region=regions["Waterfall Grind Rooms"])
    regions["room_water16"].connect(
        connecting_region=regions["Waterfall Grind Rooms"])
    regions["room_water17"].connect(
        connecting_region=regions["Waterfall Grind Rooms"])
    regions["room_tundra3"].connect(
        connecting_region=regions["Snowdin Grind Rooms"])
    regions["room_tundra4"].connect(
        connecting_region=regions["Snowdin Grind Rooms"])
    regions["room_tundra6"].connect(
        connecting_region=regions["Snowdin Grind Rooms"])
    regions["room_tundra_snowpuzz"].connect(
        connecting_region=regions["Snowdin Grind Rooms"])
    regions["room_tundra_dangerbridge"].connect(
        connecting_region=regions["Snowdin Grind Rooms"])
    regions["room_ruins7"].connect(
        connecting_region=regions["Ruins Grind Rooms"])
    regions["room_ruins9"].connect(
        connecting_region=regions["Ruins Grind Rooms"])
    regions["room_ruins8"].connect(
        connecting_region=regions["Ruins Grind Rooms"])
    regions["room_ruins15A"].connect(
        connecting_region=regions["Ruins Grind Rooms"])
    regions["room_ruins10"].connect(
        connecting_region=regions["Ruins Grind Rooms"])
    regions["room_ruins11"].connect(
        connecting_region=regions["Ruins Grind Rooms"])
    regions["room_ruins15B"].connect(
        connecting_region=regions["Ruins Grind Rooms"])
    regions["room_ruins15C"].connect(
        connecting_region=regions["Ruins Grind Rooms"])
    regions["room_ruins15D"].connect(
        connecting_region=regions["Ruins Grind Rooms"])
    regions["room_ruins14"].connect(
        connecting_region=regions["Ruins Grind Rooms"])
    regions["room_ruins13"].connect(
        connecting_region=regions["Ruins Grind Rooms"])

    regions["room_fogroom"].connect(
        connecting_region=regions["Snowdin Exit"])

    regions["Snowdin Exit"].connect(
        connecting_region=regions["room_fogroom"])

    regions["room_fire2"].connect(
        connecting_region=regions["Waterfall Exit"])

    regions["Waterfall Exit"].connect(
        connecting_region=regions["room_fire2"])

    regions["room_ruinsexit"].connect(
        connecting_region=regions["Ruins Exit"])

    regions["Ruins Exit"].connect(
        connecting_region=regions["room_ruinsexit"])

    regions["room_fire7"].connect(
        connecting_region=regions["Fire Door 1"],
        name="Fire Door 1 Block",
        rule=lambda state: state.can_reach(regions["room_fire_shootguy_2"]) and state.can_reach(
            regions["room_fire_shootguy_1"]))

    regions["room_fire_walkandbranch2"].connect(
        connecting_region=regions["Fire Door 2"],
        name="Fire Door 2 Block",
        rule=lambda state: state.can_reach(regions["room_fire_shootguy_3"]) and state.can_reach(
            regions["room_fire_shootguy_4"]))


def set_er_location_rules(world: "UndertaleWorld") -> None:
    player = world.player
    multiworld = world.multiworld
    if bool(world.options.spare_sanity.value) and (_undertale_is_route(world, 0) or _undertale_is_route(world, 1)):
        for i in range(world.options.spare_sanity_max.value):
            set_rule(multiworld.get_location("Ruins Spare " + str(i + 1), player),
                     lambda state, i=i: state.has("Ruins Spare", player,
                                                  math.ceil((i + 1) / world.options.spare_sanity_pack_size.value)))
            set_rule(multiworld.get_location("Snowdin Spare " + str(i + 1), player),
                     lambda state, i=i: state.has("Snowdin Spare", player,
                                                  math.ceil((i + 1) / world.options.spare_sanity_pack_size.value)))
            set_rule(multiworld.get_location("Waterfall Spare " + str(i + 1), player),
                     lambda state, i=i: state.has("Waterfall Spare", player,
                                                  math.ceil((i + 1) / world.options.spare_sanity_pack_size.value)))
            set_rule(multiworld.get_location("Hotland Spare " + str(i + 1), player),
                     lambda state, i=i: state.has("Hotland Spare", player,
                                                  math.ceil((i + 1) / world.options.spare_sanity_pack_size.value)) and (
                                            state.can_reach("Hotland Grind Rooms", "Region", player)))
    if _undertale_is_route(world, 1):
        set_rule(multiworld.get_location("Undyne Date (Event)", player),
                 lambda state: state.has("Papyrus Date (Event)", player) and state.has("Undyne Fight (Event)", player))
        set_rule(multiworld.get_location("Alphys Date (Event)", player),
                 lambda state: state.can_reach("room_water_trashzone1", "Region", player) and state.can_reach(
                     "room_fire_core_final", "Region", player) and state.has("Undyne Letter EX", player) and state.has(
                     "Undyne Date (Event)", player))
        set_rule(multiworld.get_location("Undyne Cook-off", player),
                 lambda state: state.has("Papyrus Date (Event)", player) and state.has("Undyne Fight (Event)", player))
        set_rule(multiworld.get_location("Alphys Date", player),
                 lambda state: state.has("Alphys Date (Event)", player))
        set_rule(multiworld.get_location("Right Spider Bake Sale", player),
                 lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5",
                                                                                                         "Region",
                                                                                                         player))
        set_rule(multiworld.get_location("Left Spider Bake Sale", player),
                 lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5",
                                                                                                         "Region",
                                                                                                         player))
        set_rule(multiworld.get_location("Sans Hot Dog Sale 1", player),
                 lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5",
                                                                                                         "Region",
                                                                                                         player))
        set_rule(multiworld.get_location("Sans Hot Cat Sale", player),
                 lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5",
                                                                                                         "Region",
                                                                                                         player))
        set_rule(multiworld.get_location("Sans Hot Dog Sale 2", player),
                 lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5",
                                                                                                         "Region",
                                                                                                         player))
        set_rule(multiworld.get_location("Sans Hot Dog Sale 3", player),
                 lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5",
                                                                                                         "Region",
                                                                                                         player))
        set_rule(multiworld.get_location("Sans Hot Dog Sale 4", player),
                 lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5",
                                                                                                         "Region",
                                                                                                         player))
        set_rule(multiworld.get_location("Hotel Door Hush Puppy", player),
                 lambda state: state.has("Hot Dog...?", player, 1))
        set_rule(multiworld.get_location("Undyne Letter", player),
                 lambda state: state.can_reach("room_fire_core_final", "Region", player) and state.has("Undyne Date (Event)",
                                                                                                       player))
    if (not _undertale_is_route(world, 2)) or _undertale_is_route(world, 3):
        set_rule(multiworld.get_location("Nicecream Punch Card Trade", player),
                 lambda state: state.has("Punch Card", player, 3))
        set_rule(multiworld.get_location("Nicecream Snowdin", player),
                 lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5",
                                                                                                         "Region",
                                                                                                         player))
        set_rule(multiworld.get_location("Nicecream Waterfall", player),
                 lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5",
                                                                                                         "Region",
                                                                                                         player))
        set_rule(multiworld.get_location("Punch Card", player),
                 lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5",
                                                                                                         "Region",
                                                                                                         player))
    if _undertale_is_route(world, 2) and (not _undertale_is_route(world, 3)) and bool(world.options.kill_sanity.value):
        set_rule(multiworld.get_location("Toriel Fight", player),
                 lambda state: state.has("Ruins Population Pack", player,
                                         math.ceil(20 / world.options.kill_sanity_pack_size.value)))
        set_rule(multiworld.get_location("Papyrus Fight", player),
                 lambda state: state.has("Jump", player) and state.has("Snowdin Population Pack", player, math.ceil(
                     16 / world.options.kill_sanity_pack_size.value)))
        set_rule(multiworld.get_location("Papyrus Fight (Event)", player),
                 lambda state: state.has("Jump", player) and state.has("Snowdin Population Pack", player, math.ceil(
                     16 / world.options.kill_sanity_pack_size.value)))
        set_rule(multiworld.get_location("Undyne Fight", player),
                 lambda state: state.has("Waterfall Population Pack", player,
                                         math.ceil(18 / world.options.kill_sanity_pack_size.value)))
        set_rule(multiworld.get_location("Undyne Fight (Event)", player),
                 lambda state: state.has("Waterfall Population Pack", player,
                                         math.ceil(18 / world.options.kill_sanity_pack_size.value)))
    if _undertale_is_route(world, 2) and bool(world.options.kill_sanity.value):
        for i in range(0, 16):
            set_rule(multiworld.get_location("Ruins Kill " + str(i + 1), player),
                     lambda state, i=i: state.has("Ruins Population Pack", player,
                                                  math.ceil((i + 1) / world.options.kill_sanity_pack_size.value)))
            set_rule(multiworld.get_location("Snowdin Kill " + str(i + 1), player),
                     lambda state, i=i: state.has("Snowdin Population Pack", player,
                                                  math.ceil((i + 1) / world.options.kill_sanity_pack_size.value)))
            set_rule(multiworld.get_location("Waterfall Kill " + str(i + 1), player),
                     lambda state, i=i: state.has("Waterfall Population Pack", player,
                                                  math.ceil((i + 1) / world.options.kill_sanity_pack_size.value)))
            set_rule(multiworld.get_location("Hotland Kill " + str(i + 1), player),
                     lambda state, i=i: state.has("Hotland Population Pack", player,
                                                  math.ceil((i + 1) / world.options.kill_sanity_pack_size.value)) and (
                                            state.can_reach("Hotland Grind Rooms", "Region", player)))
        for i in range(16, 18):
            set_rule(multiworld.get_location("Ruins Kill " + str(i + 1), player),
                     lambda state, i=i: state.has("Ruins Population Pack", player,
                                                  math.ceil((i + 1) / world.options.kill_sanity_pack_size.value)))
            set_rule(multiworld.get_location("Waterfall Kill " + str(i + 1), player),
                     lambda state, i=i: state.has("Waterfall Population Pack", player,
                                                  math.ceil((i + 1) / world.options.kill_sanity_pack_size.value)))
            set_rule(multiworld.get_location("Hotland Kill " + str(i + 1), player),
                     lambda state, i=i: state.has("Hotland Population Pack", player,
                                                  math.ceil((i + 1) / world.options.kill_sanity_pack_size.value)) and (
                                            state.can_reach("Hotland Grind Rooms", "Region", player)))
        for i in range(18, 20):
            set_rule(multiworld.get_location("Ruins Kill " + str(i + 1), player),
                     lambda state, i=i: state.has("Ruins Population Pack", player,
                                                  math.ceil((i + 1) / world.options.kill_sanity_pack_size.value)))
            set_rule(multiworld.get_location("Hotland Kill " + str(i + 1), player),
                     lambda state, i=i: state.has("Hotland Population Pack", player,
                                                  math.ceil((i + 1) / world.options.kill_sanity_pack_size.value)) and (
                                            state.can_reach("Hotland Grind Rooms", "Region", player)))
        for i in range(20, 40):
            set_rule(multiworld.get_location("Hotland Kill " + str(i + 1), player),
                     lambda state, i=i: state.has("Hotland Population Pack", player,
                                                  math.ceil((i + 1) / world.options.kill_sanity_pack_size.value)) and (
                                            state.can_reach("Hotland Grind Rooms", "Region", player)))
    if _undertale_is_route(world, 2) and \
            (bool(world.options.rando_love.value) or bool(world.options.rando_stats.value)):
        maxlv = 1
        while maxlv < 20:
            maxlv += 1
            if world.options.rando_stats:
                set_rule(multiworld.get_location(("ATK " + str(maxlv)), player),
                         lambda state, maxlv=maxlv:
                         _undertale_return_reachable_level(_undertale_exp_available(state, world, player)) >= maxlv)
                set_rule(multiworld.get_location(("HP " + str(maxlv)), player),
                         lambda state, maxlv=maxlv:
                         _undertale_return_reachable_level(_undertale_exp_available(state, world, player)) >= maxlv)
                if maxlv == 5 or maxlv == 9 or maxlv == 13 or maxlv == 17:
                    set_rule(multiworld.get_location(("DEF " + str(maxlv)), player),
                             lambda state, maxlv=maxlv:
                             _undertale_return_reachable_level(_undertale_exp_available(state, world, player)) >= maxlv)
            if world.options.rando_love:
                set_rule(multiworld.get_location(("LOVE " + str(maxlv)), player),
                         lambda state, maxlv=maxlv:
                         _undertale_return_reachable_level(_undertale_exp_available(state, world, player)) >= maxlv)
    set_rule(multiworld.get_location("Mettaton Fight", player),
             lambda state: state.can_reach("room_fire_core_metttest", "Region", player) and
                           (not bool(world.options.kill_sanity.value) or not _undertale_is_route(world, 2) or
                            state.has("Hotland Population Pack", player,
                                      math.ceil(40 / world.options.kill_sanity_pack_size.value))))
    set_rule(multiworld.get_location("Snowdin Shop 1", player),
             lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5",
                                                                                                     "Region", player))
    set_rule(multiworld.get_location("Snowdin Shop 2", player),
             lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5",
                                                                                                     "Region", player))
    set_rule(multiworld.get_location("Snowdin Shop 3", player),
             lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5",
                                                                                                     "Region", player))
    set_rule(multiworld.get_location("Snowdin Shop 4", player),
             lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5",
                                                                                                     "Region", player))
    set_rule(multiworld.get_location("Gerson Shop 1", player),
             lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5",
                                                                                                     "Region", player))
    set_rule(multiworld.get_location("Gerson Shop 2", player),
             lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5",
                                                                                                     "Region", player))
    set_rule(multiworld.get_location("Gerson Shop 3", player),
             lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5",
                                                                                                     "Region", player))
    set_rule(multiworld.get_location("Gerson Shop 4", player),
             lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5",
                                                                                                     "Region", player))
    set_rule(multiworld.get_location("Temmie Shop 1", player),
             lambda state: state.can_reach("room_water_piano", "Region", player))
    set_rule(multiworld.get_location("Temmie Shop 2", player),
             lambda state: state.can_reach("room_water_piano", "Region", player))
    set_rule(multiworld.get_location("Temmie Shop 3", player),
             lambda state: state.can_reach("room_water_piano", "Region", player))
    set_rule(multiworld.get_location("Temmie Shop 4", player),
             lambda state: state.can_reach("room_water_piano", "Region", player) and state.has("1000G", player, 2))
    set_rule(multiworld.get_location("Bratty Catty Shop 1", player),
             lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5",
                                                                                                     "Region", player))
    set_rule(multiworld.get_location("Bratty Catty Shop 2", player),
             lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5",
                                                                                                     "Region", player))
    set_rule(multiworld.get_location("Bratty Catty Shop 3", player),
             lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5",
                                                                                                     "Region", player))
    set_rule(multiworld.get_location("Bratty Catty Shop 4", player),
             lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5",
                                                                                                     "Region", player))
    set_rule(multiworld.get_location("Burgerpants Shop 1", player),
             lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5",
                                                                                                     "Region", player))
    set_rule(multiworld.get_location("Burgerpants Shop 2", player),
             lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5",
                                                                                                     "Region", player))
    set_rule(multiworld.get_location("Burgerpants Shop 3", player),
             lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5",
                                                                                                     "Region", player))
    set_rule(multiworld.get_location("Burgerpants Shop 4", player),
             lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5",
                                                                                                     "Region", player))
