from typing import Dict, TYPE_CHECKING
from worlds.generic.Rules import set_rule, forbid_item, add_rule
from .Rules import _undertale_is_route, _undertale_exp_available, _undertale_return_reachable_level
from BaseClasses import Region, CollectionState
import math

if TYPE_CHECKING:
    from . import UndertaleWorld


def set_er_region_rules(world: "UndertaleWorld", regions: Dict[str, Region]) -> None:
    player = world.player
    multiworld = world.multiworld

    regions["Menu"].connect(
        connecting_region=regions["room_area1"])

    regions["room_water_undynebridge"].connect(
        connecting_region=regions["room_water_undynebridgeend"])

    regions["room_water_undynebridgeend"].connect(
        connecting_region=regions["room_water_undynebridge"])

    regions["room_water_undynefinal"].connect(
        connecting_region=regions["room_water_undynefinal2"])

    regions["room_water_undynefinal2"].connect(
        connecting_region=regions["room_water_undynefinal"])

    regions["room_water_undynefinal2"].connect(
        connecting_region=regions["room_water_undynefinal3"])

    regions["room_water_undynefinal3"].connect(
        connecting_region=regions["room_water_undynefinal2"])

    regions["room_water_undynefinal3"].connect(
        connecting_region=regions["room_fire1"])

    regions["room_fire1"].connect(
        connecting_region=regions["room_water_undynefinal3"])

    regions["room_fire1"].connect(
        connecting_region=regions["room_fire2"])

    regions["room_fire2"].connect(
        connecting_region=regions["room_fire1"])

    regions["Ruins Exit"].connect(
        connecting_region=regions["room_area1"])

    regions["Snowdin Exit"].connect(
        connecting_region=regions["room_area1"])

    regions["Waterfall Exit"].connect(
        connecting_region=regions["room_area1"])

    regions["room_water_waterfall4"].connect(
        connecting_region=regions["Monster Kid Raised Ledge"])

    regions["room_tundra_sanshouse"].connect(
        connecting_region=regions["Papyrus Rocks"],
        rule=lambda state: state.has("Complete Skeleton", player))

    regions["Papyrus Rocks"].connect(
        connecting_region=regions["room_tundra_sanshouse"],
        rule=lambda state: state.has("Complete Skeleton", player))

    regions["room_water_friendlyhub"].connect(
        connecting_region=regions["Undyne Rocks"],
        rule=lambda state: state.has("Fish", player))

    regions["Undyne Rocks"].connect(
        connecting_region=regions["room_water_friendlyhub"],
        rule=lambda state: state.has("Fish", player))

    regions["room_area1"].connect(
        connecting_region=regions["Ruins Entrance"],
        rule=lambda state: state.has("Ruins Key", player))

    regions["Ruins Entrance"].connect(
        connecting_region=regions["room_area1"])

    # regions["room_fire_labelevator"].connect(
    #     connecting_region=regions["room_castle_elevatorout"])

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

    # regions["room_area1"].connect(
    #     connecting_region=regions["Hotland Entrance"],
    #     rule=lambda state: state.has("Hotland Key", player))

    # regions["Hotland Entrance"].connect(
    #     connecting_region=regions["room_area1"])

    # regions["room_area1"].connect(
    #     connecting_region=regions["Core Entrance"],
    #     rule=lambda state: state.has("Core Key", player))

    # regions["Core Entrance"].connect(
    #     connecting_region=regions["room_area1"])

    regions["room_water_undynebridgeend"].connect(
        connecting_region=regions["Trash Zone Fall"])

    regions["Trash Zone Fall"].connect(
        connecting_region=regions["room_water_trashzone1"])

    regions["Ice Hole Fall"].connect(
        connecting_region=regions["room_tundra_icehole"])

    regions["Garage One Way"].connect(
        connecting_region=regions["room_tundra_town"])

    regions["Ruins Pit Circle B"].connect(
        connecting_region=regions["room_ruins15E"])

    regions["Ruins Pit Circle C"].connect(
        connecting_region=regions["room_ruins15E"])

    regions["Ruins Pit Circle D"].connect(
        connecting_region=regions["room_ruins15E"])

    regions["Toriel Basement 2"].connect(
        connecting_region=regions["room_basement1"])
    regions["room_basement1"].connect(
        connecting_region=regions["Toriel Basement 2"],
        name="Toriel Basement Block")


def set_er_location_rules(world: "UndertaleWorld") -> None:
    player = world.player
    multiworld = world.multiworld
    # if bool(multiworld.spare_sanity[player].value) and (_undertale_is_route(multiworld.state, player, 0) or _undertale_is_route(multiworld.state, player, 1)):
    #     for i in range(multiworld.spare_sanity_max[player].value):
    #         set_rule(multiworld.get_location("Ruins Spare "+str(i+1), player), lambda state, i=i: state.has("Ruins Spare", player, math.ceil((i+1)/state.multiworld.spare_sanity_pack_size[player].value)))
    #         set_rule(multiworld.get_location("Snowdin Spare "+str(i+1), player), lambda state, i=i: state.has("Snowdin Spare", player, math.ceil((i+1)/state.multiworld.spare_sanity_pack_size[player].value)))
    #         set_rule(multiworld.get_location("Waterfall Spare "+str(i+1), player), lambda state, i=i: state.has("Waterfall Spare", player, math.ceil((i+1)/state.multiworld.spare_sanity_pack_size[player].value)))
    #         set_rule(multiworld.get_location("Hotland Spare "+str(i+1), player), lambda state, i=i: state.has("Hotland Spare", player, math.ceil((i+1)/state.multiworld.spare_sanity_pack_size[player].value)) and (state.can_reach("Hotland", "Region", player) or state.can_reach("Core", "Region", player)))
    # set_rule(multiworld.get_entrance("Core Exit", player),
    #          lambda state: state.has("Mettaton Plush", player) and (not bool(state.multiworld.kill_sanity[player].value) or not _undertale_is_route(state, player, 2) or state.has("Hotland Population Pack", player, math.ceil(40/state.multiworld.kill_sanity_pack_size[player].value))))
    # set_rule(multiworld.get_entrance("New Home Exit", player),
    #          lambda state: ((state.has("Left Home Key", player) and
    #                         state.has("Right Home Key", player)) or
    #                        state.has("Key Piece", player, state.multiworld.key_pieces[player].value))
    #                        and (
    #                                not bool(state.multiworld.kill_sanity[player].value) or not _undertale_is_route(state, player, 2) or state.has("Hotland Population Pack", player, math.ceil(40/state.multiworld.kill_sanity_pack_size[player].value))
    #                        )
    #                        and (state.has("Jump", player) or not _undertale_is_route(state, player, 2)))
    set_rule(multiworld.get_location("Undyne Date", player),
            lambda state: state.has("Papyrus Date", player) and state.has("Undyne Fight (Event)", player))
    # set_rule(multiworld.get_location("Papyrus Date", player),
    #         lambda state: state.has("Papyrus Fight (Event)", player))
    set_rule(multiworld.get_location("Diary 1", player),
                 lambda state: state.has("Mystery Key", player, 1))
    set_rule(multiworld.get_location("Diary 2", player),
                 lambda state: state.has("Mystery Key", player, 1))
    set_rule(multiworld.get_location("Diary 3", player),
                 lambda state: state.has("Mystery Key", player, 1))
    set_rule(multiworld.get_location("Diary 4", player),
                 lambda state: state.has("Mystery Key", player, 1))
    set_rule(multiworld.get_location("Diary 5", player),
                 lambda state: state.has("Mystery Key", player, 1))
    set_rule(multiworld.get_location("Diary 6", player),
                 lambda state: state.has("Mystery Key", player, 1))
    if _undertale_is_route(multiworld.state, player, 1):
        # set_rule(multiworld.get_entrance("Lab Elevator", player),
        #          lambda state: state.has("Alphys Date", player) and state.has("DT Extractor", player) and ((state.has("Left Home Key", player) and
        #                     state.has("Right Home Key", player)) or
        #                    state.has("Key Piece", player, state.multiworld.key_pieces[player].value)))
        # set_rule(multiworld.get_location("Alphys Date", player),
        #          lambda state: state.can_reach("room_fire_core_final", "Region", player) and state.has("Undyne Letter EX", player) and state.has("Undyne Date", player))
        set_rule(multiworld.get_location("Undyne Cook-off", player),
                 lambda state: state.has("Papyrus Date", player) and state.has("Undyne Fight (Event)", player))
        # set_rule(multiworld.get_location("Papyrus Hangout", player),
        #          lambda state: state.has("Papyrus Fight (Event)", player))
        # set_rule(multiworld.get_location("True Lab Key", player),
        #          lambda state: state.has("Alphys Date", player))
        set_rule(multiworld.get_location("Donut Sale", player),
                 lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5", "Region", player))
        set_rule(multiworld.get_location("Cider Sale", player),
                 lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5", "Region", player))
        # set_rule(multiworld.get_location("Dog Sale 1", player),
        #          lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5", "Region", player))
        # set_rule(multiworld.get_location("Cat Sale", player),
        #          lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5", "Region", player))
        # set_rule(multiworld.get_location("Dog Sale 2", player),
        #          lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5", "Region", player))
        # set_rule(multiworld.get_location("Dog Sale 3", player),
        #          lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5", "Region", player))
        # set_rule(multiworld.get_location("Dog Sale 4", player),
        #          lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5", "Region", player))
        # set_rule(multiworld.get_location("Hush Trade", player),
        #          lambda state: state.has("Hot Dog...?", player, 1))
        # set_rule(multiworld.get_location("Letter Quest", player),
        #          lambda state: state.can_reach("room_fire_core_final", "Region", player) and state.has("Undyne Date", player))
        # set_rule(multiworld.get_location("True Lab Plot", player),
        #          lambda state: state.can_reach("New Home", "Region", player)
        #                        and state.can_reach("Letter Quest", "Location", player)
        #                        and state.can_reach("Alphys Date", "Location", player))
    if (not _undertale_is_route(multiworld.state, player, 2)) or _undertale_is_route(multiworld.state, player, 3):
        set_rule(multiworld.get_location("Nicecream Punch Card", player),
                 lambda state: state.has("Punch Card", player, 3))
        set_rule(multiworld.get_location("Nicecream Snowdin", player),
                 lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5", "Region", player))
        set_rule(multiworld.get_location("Nicecream Waterfall", player),
                 lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5", "Region", player))
        set_rule(multiworld.get_location("Card Reward", player),
                 lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5", "Region", player))
    if _undertale_is_route(multiworld.state, player, 2) and (not _undertale_is_route(multiworld.state, player, 3)) and bool(multiworld.kill_sanity[player].value):
        set_rule(multiworld.get_location("Toriel Fight", player), lambda state: state.has("Ruins Population Pack", player, math.ceil(20/state.multiworld.kill_sanity_pack_size[player].value)))
        set_rule(multiworld.get_location("Papyrus Fight", player), lambda state: state.has("Snowdin Population Pack", player, math.ceil(16/state.multiworld.kill_sanity_pack_size[player].value)))
        set_rule(multiworld.get_location("Undyne Fight", player), lambda state: state.has("Waterfall Population Pack", player, math.ceil(18/state.multiworld.kill_sanity_pack_size[player].value)))
    # if _undertale_is_route(multiworld.state, player, 2) and bool(multiworld.kill_sanity[player].value):
        # for i in range(0, 16):
        #     set_rule(multiworld.get_location("Ruins Kill "+str(i+1), player), lambda state, i=i: state.has("Ruins Population Pack", player, math.ceil((i+1)/state.multiworld.kill_sanity_pack_size[player].value)))
        #     set_rule(multiworld.get_location("Snowdin Kill "+str(i+1), player), lambda state, i=i: state.has("Snowdin Population Pack", player, math.ceil((i+1)/state.multiworld.kill_sanity_pack_size[player].value)))
        #     set_rule(multiworld.get_location("Waterfall Kill "+str(i+1), player), lambda state, i=i: state.has("Waterfall Population Pack", player, math.ceil((i+1)/state.multiworld.kill_sanity_pack_size[player].value)))
        #     set_rule(multiworld.get_location("Hotland Kill "+str(i+1), player), lambda state, i=i: state.has("Hotland Population Pack", player, math.ceil((i+1)/state.multiworld.kill_sanity_pack_size[player].value)) and (state.can_reach("Hotland", "Region", player) or state.can_reach("Core", "Region", player)))
        # for i in range(16, 18):
        #     set_rule(multiworld.get_location("Ruins Kill "+str(i+1), player), lambda state, i=i: state.has("Ruins Population Pack", player, math.ceil((i+1)/state.multiworld.kill_sanity_pack_size[player].value)))
        #     set_rule(multiworld.get_location("Waterfall Kill "+str(i+1), player), lambda state, i=i: state.has("Waterfall Population Pack", player, math.ceil((i+1)/state.multiworld.kill_sanity_pack_size[player].value)))
        #     set_rule(multiworld.get_location("Hotland Kill "+str(i+1), player), lambda state, i=i: state.has("Hotland Population Pack", player, math.ceil((i+1)/state.multiworld.kill_sanity_pack_size[player].value)) and (state.can_reach("Hotland", "Region", player) or state.can_reach("Core", "Region", player)))
        # for i in range(18, 20):
        #     set_rule(multiworld.get_location("Ruins Kill "+str(i+1), player), lambda state, i=i: state.has("Ruins Population Pack", player, math.ceil((i+1)/state.multiworld.kill_sanity_pack_size[player].value)))
        #     set_rule(multiworld.get_location("Hotland Kill "+str(i+1), player), lambda state, i=i: state.has("Hotland Population Pack", player, math.ceil((i+1)/state.multiworld.kill_sanity_pack_size[player].value)) and (state.can_reach("Hotland", "Region", player) or state.can_reach("Core", "Region", player)))
        # for i in range(20, 40):
    #         set_rule(multiworld.get_location("Hotland Kill "+str(i+1), player), lambda state, i=i: state.has("Hotland Population Pack", player, math.ceil((i+1)/state.multiworld.kill_sanity_pack_size[player].value)) and (state.can_reach("Hotland", "Region", player) or state.can_reach("Core", "Region", player)))
    # if _undertale_is_route(multiworld.state, player, 2) and \
        #         (bool(multiworld.rando_love[player].value) or bool(multiworld.rando_stats[player].value)):
        #     maxlv = 1
        #     while maxlv < 20:
        #         maxlv += 1
        #         if multiworld.rando_stats[player]:
        #             set_rule(multiworld.get_location(("ATK "+str(maxlv)), player),
        #                              lambda state, maxlv=maxlv: _undertale_return_reachable_level(state, _undertale_exp_available(state, player)) >= maxlv)
        #             set_rule(multiworld.get_location(("HP "+str(maxlv)), player),
        #                              lambda state, maxlv=maxlv: _undertale_return_reachable_level(state, _undertale_exp_available(state, player)) >= maxlv)
        #             if maxlv == 5 or maxlv == 9 or maxlv == 13 or maxlv == 17:
        #                 set_rule(multiworld.get_location(("DEF "+str(maxlv)), player),
        #                                  lambda state, maxlv=maxlv: _undertale_return_reachable_level(state, _undertale_exp_available(state, player)) >= maxlv)
        #         if multiworld.rando_love[player]:
        #             add_rule(multiworld.get_location(("LOVE "+str(maxlv)), player),
    #                              lambda state, maxlv=maxlv: _undertale_return_reachable_level(state, _undertale_exp_available(state, player)) >= maxlv)
    # set_rule(multiworld.get_location("Mettaton Fight", player),
    #          lambda state: state.can_reach("room_fire_core_metttest", "Region", player) and (not bool(state.multiworld.kill_sanity[player].value) or not _undertale_is_route(state, player, 2) or state.has("Hotland Population Pack", player, math.ceil(40/state.multiworld.kill_sanity_pack_size[player].value))))
    set_rule(multiworld.get_location("Bunny 1", player),
             lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5", "Region", player))
    set_rule(multiworld.get_location("Bunny 2", player),
             lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5", "Region", player))
    set_rule(multiworld.get_location("Bunny 3", player),
             lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5", "Region", player))
    set_rule(multiworld.get_location("Bunny 4", player),
             lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5", "Region", player))
    set_rule(multiworld.get_location("Gerson 1", player),
             lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5", "Region", player))
    set_rule(multiworld.get_location("Gerson 2", player),
             lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5", "Region", player))
    set_rule(multiworld.get_location("Gerson 3", player),
             lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5", "Region", player))
    set_rule(multiworld.get_location("Gerson 4", player),
             lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5", "Region", player))
    # set_rule(multiworld.get_location("Present Knife", player),
    #          lambda state: (not bool(state.multiworld.kill_sanity[player].value) or not _undertale_is_route(state, player, 2) or state.has("Hotland Population Pack", player, math.ceil(40/state.multiworld.kill_sanity_pack_size[player].value))))
    # set_rule(multiworld.get_location("Present Locket", player),
    #          lambda state: (not bool(state.multiworld.kill_sanity[player].value) or not _undertale_is_route(state, player, 2) or state.has("Hotland Population Pack", player, math.ceil(40/state.multiworld.kill_sanity_pack_size[player].value))))
    # set_rule(multiworld.get_location("Left New Home Key", player),
    #          lambda state: (not bool(state.multiworld.kill_sanity[player].value) or not _undertale_is_route(state, player, 2) or state.has("Hotland Population Pack", player, math.ceil(40/state.multiworld.kill_sanity_pack_size[player].value))))
    # set_rule(multiworld.get_location("Right New Home Key", player),
    #          lambda state: (not bool(state.multiworld.kill_sanity[player].value) or not _undertale_is_route(state, player, 2) or state.has("Hotland Population Pack", player, math.ceil(40/state.multiworld.kill_sanity_pack_size[player].value))))
    set_rule(multiworld.get_location("TemmieShop 1", player),
             lambda state: state.can_reach("room_water_piano", "Region", player))
    set_rule(multiworld.get_location("TemmieShop 2", player),
             lambda state: state.can_reach("room_water_piano", "Region", player))
    set_rule(multiworld.get_location("TemmieShop 3", player),
             lambda state: state.can_reach("room_water_piano", "Region", player))
    set_rule(multiworld.get_location("TemmieShop 4", player),
             lambda state: state.can_reach("room_water_piano", "Region", player) and state.has("1000G", player, 2))
    # set_rule(multiworld.get_location("Bratty Catty 1", player),
    #          lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5", "Region", player))
    # set_rule(multiworld.get_location("Bratty Catty 2", player),
    #          lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5", "Region", player))
    # set_rule(multiworld.get_location("Bratty Catty 3", player),
    #          lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5", "Region", player))
    # set_rule(multiworld.get_location("Bratty Catty 4", player),
    #          lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5", "Region", player))
    # set_rule(multiworld.get_location("Burgerpants 1", player),
    #          lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5", "Region", player))
    # set_rule(multiworld.get_location("Burgerpants 2", player),
    #          lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5", "Region", player))
    # set_rule(multiworld.get_location("Burgerpants 3", player),
    #          lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5", "Region", player))
    # set_rule(multiworld.get_location("Burgerpants 4", player),
    #          lambda state: state.can_reach("room_water_piano", "Region", player) and state.can_reach("room_shop5", "Region", player))
