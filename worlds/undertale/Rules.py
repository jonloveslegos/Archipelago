from worlds.generic.Rules import set_rule, add_rule, add_item_rule
from BaseClasses import MultiWorld, CollectionState
import math


def _undertale_is_route(state: CollectionState, player: int, route: int):
    if route == 3:
        return state.multiworld.route_required[player].current_key == "all_routes"
    if state.multiworld.route_required[player].current_key == "all_routes":
        return True
    if route == 0:
        return state.multiworld.route_required[player].current_key == "neutral"
    if route == 1:
        return state.multiworld.route_required[player].current_key == "pacifist"
    if route == 2:
        return state.multiworld.route_required[player].current_key == "genocide"
    return False


def _undertale_exp_available(state: CollectionState, player: int):
    exp = 0
    pack_size = state.multiworld.kill_sanity_pack_size[player].value
    if state.has("Ruins Key", player):
        exp += (min(20, state.count("Ruins Population Pack", player) * pack_size) * 2)
        if state.count("Ruins Population Pack", player) * pack_size >= 20:
            exp += 150
    if state.has("Snowdin Key", player):
        exp += (min(15, state.count("Snowdin Population Pack", player) * pack_size) * 1)
        exp += 170
        if state.count("Snowdin Population Pack", player) * pack_size >= 16:
            exp += 222
    if state.has("Waterfall Key", player):
        exp += (min(18, state.count("Waterfall Population Pack", player) * pack_size) * 3)
        exp += 52
        if state.count("Waterfall Population Pack", player) * pack_size >= 18:
            exp += 1500
    if state.has("Hotland Key", player) or state.has("Core Key", player):
        exp += (min(40, state.count("Hotland Population Pack", player) * pack_size) * 70)
    if state.has("Hotland Key", player):
        exp += 520
    if state.has("Core Key", player):
        exp += 1100
        if state.count("Hotland Population Pack", player) * pack_size >= 40 and state.has("Mettaton Plush", player):
            exp = 50000
        if state.count("Hotland Population Pack", player) * pack_size >= 40 and state.can_reach("Last Corridor Exit", "Entrance", player):
            exp = 99999
    return exp


def _undertale_return_reachable_level(state: CollectionState, exp: int):
    lvl = 1
    if exp >= 10 and lvl == 1:
        lvl += 1
    if exp >= 30 and lvl == 2:
        lvl += 1
    if exp >= 70 and lvl == 3:
        lvl += 1
    if exp >= 120 and lvl == 4:
        lvl += 1
    if exp >= 200 and lvl == 5:
        lvl += 1
    if exp >= 300 and lvl == 6:
        lvl += 1
    if exp >= 500 and lvl == 7:
        lvl += 1
    if exp >= 800 and lvl == 8:
        lvl += 1
    if exp >= 1200 and lvl == 9:
        lvl += 1
    if exp >= 1700 and lvl == 10:
        lvl += 1
    if exp >= 2500 and lvl == 11:
        lvl += 1
    if exp >= 3500 and lvl == 12:
        lvl += 1
    if exp >= 5000 and lvl == 13:
        lvl += 1
    if exp >= 7000 and lvl == 14:
        lvl += 1
    if exp >= 10000 and lvl == 15:
        lvl += 1
    if exp >= 15000 and lvl == 16:
        lvl += 1
    if exp >= 25000 and lvl == 17:
        lvl += 1
    if exp >= 50000 and lvl == 18:
        lvl += 1
    if exp >= 99999 and lvl == 19:
        lvl += 1
    return lvl


# Sets rules on entrances and advancements that are always applied
def set_rules(multiworld: MultiWorld, player: int):
    set_rule(multiworld.get_entrance("Ruins Hub", player), lambda state: state.has("Ruins Key", player))
    set_rule(multiworld.get_entrance("Snowdin Hub", player), lambda state: state.has("Snowdin Key", player))
    set_rule(multiworld.get_entrance("Waterfall Hub", player), lambda state: state.has("Waterfall Key", player))
    set_rule(multiworld.get_entrance("Hotland Hub", player), lambda state: state.has("Hotland Key", player))
    set_rule(multiworld.get_entrance("Core Hub", player), lambda state: state.has("Core Key", player))
    if bool(multiworld.spare_sanity[player].value) and (_undertale_is_route(multiworld.state, player, 0) or _undertale_is_route(multiworld.state, player, 1)):
        for i in range(multiworld.spare_sanity_max[player].value):
            set_rule(multiworld.get_location("Ruins Spare "+str(i+1), player), lambda state, i=i: state.has("Ruins Spare", player, math.ceil((i+1)/state.multiworld.spare_sanity_pack_size[player].value)))
            set_rule(multiworld.get_location("Snowdin Spare "+str(i+1), player), lambda state, i=i: state.has("Snowdin Spare", player, math.ceil((i+1)/state.multiworld.spare_sanity_pack_size[player].value)))
            set_rule(multiworld.get_location("Waterfall Spare "+str(i+1), player), lambda state, i=i: state.has("Waterfall Spare", player, math.ceil((i+1)/state.multiworld.spare_sanity_pack_size[player].value)))
            set_rule(multiworld.get_location("Hotland Spare "+str(i+1), player), lambda state, i=i: state.has("Hotland Spare", player, math.ceil((i+1)/state.multiworld.spare_sanity_pack_size[player].value)) and (state.can_reach("Hotland", "Region", player) or state.can_reach("Core", "Region", player)))
    set_rule(multiworld.get_entrance("Core Exit", player),
             lambda state: state.has("Mettaton Plush", player) and (not bool(state.multiworld.kill_sanity[player].value) or not _undertale_is_route(state, player, 2) or state.has("Hotland Population Pack", player, math.ceil(40/state.multiworld.kill_sanity_pack_size[player].value))))
    set_rule(multiworld.get_entrance("New Home Exit", player),
             lambda state: ((state.has("Left Home Key", player) and
                            state.has("Right Home Key", player)) or
                           state.has("Key Piece", player, state.multiworld.key_pieces[player].value))
                           and (
                                   not bool(state.multiworld.kill_sanity[player].value) or not _undertale_is_route(state, player, 2) or state.has("Hotland Population Pack", player, math.ceil(40/state.multiworld.kill_sanity_pack_size[player].value))
                           )
                           and (state.has("Jump", player) or not _undertale_is_route(state, player, 2)))
    if _undertale_is_route(multiworld.state, player, 1):
        set_rule(multiworld.get_entrance("Papyrus\" Home Entrance", player),
                 lambda state: state.has("Complete Skeleton", player))
        set_rule(multiworld.get_entrance("Undyne\"s Home Entrance", player),
                 lambda state: state.has("Fish", player) and state.has("Papyrus Date", player))
        set_rule(multiworld.get_entrance("Lab Elevator", player),
                 lambda state: state.has("Alphys Date", player) and state.has("DT Extractor", player) and ((state.has("Left Home Key", player) and
                            state.has("Right Home Key", player)) or
                           state.has("Key Piece", player, state.multiworld.key_pieces[player].value)))
        set_rule(multiworld.get_location("Alphys Date", player),
                 lambda state: state.has("Undyne Letter EX", player) and state.has("Undyne Date", player))
        set_rule(multiworld.get_location("Papyrus Hangout", player),
                 lambda state: state.can_reach("Snowdin Town", "Region", player))
        set_rule(multiworld.get_location("Undyne Cook-off", player),
                 lambda state: state.can_reach("Waterfall", "Region", player))
        set_rule(multiworld.get_location("Diary 1", player),
                 lambda state: state.can_reach("Waterfall", "Region", player) and state.has("Mystery Key", player, 1))
        set_rule(multiworld.get_location("Diary 2", player),
                 lambda state: state.can_reach("Waterfall", "Region", player) and state.has("Mystery Key", player, 1))
        set_rule(multiworld.get_location("Diary 3", player),
                 lambda state: state.can_reach("Waterfall", "Region", player) and state.has("Mystery Key", player, 1))
        set_rule(multiworld.get_location("Diary 4", player),
                 lambda state: state.can_reach("Waterfall", "Region", player) and state.has("Mystery Key", player, 1))
        set_rule(multiworld.get_location("Diary 5", player),
                 lambda state: state.can_reach("Waterfall", "Region", player) and state.has("Mystery Key", player, 1))
        set_rule(multiworld.get_location("Diary 6", player),
                 lambda state: state.can_reach("Waterfall", "Region", player) and state.has("Mystery Key", player, 1))
        set_rule(multiworld.get_location("True Lab Key", player),
                 lambda state: state.can_reach("New Home", "Region", player)
                               and state.can_reach("Letter Quest", "Location", player))
        set_rule(multiworld.get_location("Chisps Machine", player),
                 lambda state: state.can_reach("True Lab", "Region", player))
        set_rule(multiworld.get_location("Donut Sale", player),
                 lambda state: state.can_reach("Ruins", "Region", player) and state.can_reach("Waterfall", "Region", player))
        set_rule(multiworld.get_location("Cider Sale", player),
                 lambda state: state.can_reach("Ruins", "Region", player) and state.can_reach("Waterfall", "Region", player))
        set_rule(multiworld.get_location("Dog Sale 1", player),
                 lambda state: state.can_reach("Cooking Show", "Region", player) and state.can_reach("Waterfall", "Region", player))
        set_rule(multiworld.get_location("Cat Sale", player),
                 lambda state: state.can_reach("Cooking Show", "Region", player) and state.can_reach("Waterfall", "Region", player))
        set_rule(multiworld.get_location("Dog Sale 2", player),
                 lambda state: state.can_reach("Cooking Show", "Region", player) and state.can_reach("Waterfall", "Region", player))
        set_rule(multiworld.get_location("Dog Sale 3", player),
                 lambda state: state.can_reach("Cooking Show", "Region", player) and state.can_reach("Waterfall", "Region", player))
        set_rule(multiworld.get_location("Dog Sale 4", player),
                 lambda state: state.can_reach("Cooking Show", "Region", player) and state.can_reach("Waterfall", "Region", player))
        set_rule(multiworld.get_location("Hush Trade", player),
                 lambda state: state.can_reach("News Show", "Region", player) and state.has("Hot Dog...?", player, 1))
        set_rule(multiworld.get_location("Letter Quest", player),
                 lambda state: state.can_reach("Last Corridor", "Region", player) and state.has("Undyne Date", player))
    if (not _undertale_is_route(multiworld.state, player, 2)) or _undertale_is_route(multiworld.state, player, 3):
        set_rule(multiworld.get_location("Nicecream Punch Card", player),
                 lambda state: state.has("Punch Card", player, 3) and state.can_reach("Waterfall", "Region", player))
        set_rule(multiworld.get_location("Nicecream Snowdin", player),
                 lambda state: state.can_reach("Snowdin Town", "Region", player))
        set_rule(multiworld.get_location("Nicecream Waterfall", player),
                 lambda state: state.can_reach("Waterfall", "Region", player))
        set_rule(multiworld.get_location("Card Reward", player),
                 lambda state: state.can_reach("Waterfall", "Region", player))
        set_rule(multiworld.get_location("Apron Hidden", player),
                 lambda state: state.can_reach("Cooking Show", "Region", player))
    if _undertale_is_route(multiworld.state, player, 2) and bool(multiworld.kill_sanity[player].value):
        set_rule(multiworld.get_location("Toriel Fight", player), lambda state: state.has("Ruins Population Pack", player, math.ceil(20/state.multiworld.kill_sanity_pack_size[player].value)))
        set_rule(multiworld.get_location("Papyrus Fight", player), lambda state: state.has("Snowdin Population Pack", player, math.ceil(16/state.multiworld.kill_sanity_pack_size[player].value)))
        set_rule(multiworld.get_location("Undyne Fight", player), lambda state: state.has("Waterfall Population Pack", player, math.ceil(18/state.multiworld.kill_sanity_pack_size[player].value)))
        for i in range(0, 16):
            set_rule(multiworld.get_location("Ruins Kill "+str(i+1), player), lambda state, i=i: state.has("Ruins Population Pack", player, math.ceil((i+1)/state.multiworld.kill_sanity_pack_size[player].value)))
            set_rule(multiworld.get_location("Snowdin Kill "+str(i+1), player), lambda state, i=i: state.has("Snowdin Population Pack", player, math.ceil((i+1)/state.multiworld.kill_sanity_pack_size[player].value)))
            set_rule(multiworld.get_location("Waterfall Kill "+str(i+1), player), lambda state, i=i: state.has("Waterfall Population Pack", player, math.ceil((i+1)/state.multiworld.kill_sanity_pack_size[player].value)))
            set_rule(multiworld.get_location("Hotland Kill "+str(i+1), player), lambda state, i=i: state.has("Hotland Population Pack", player, math.ceil((i+1)/state.multiworld.kill_sanity_pack_size[player].value)) and (state.can_reach("Hotland", "Region", player) or state.can_reach("Core", "Region", player)))
        for i in range(16, 18):
            set_rule(multiworld.get_location("Ruins Kill "+str(i+1), player), lambda state, i=i: state.has("Ruins Population Pack", player, math.ceil((i+1)/state.multiworld.kill_sanity_pack_size[player].value)))
            set_rule(multiworld.get_location("Waterfall Kill "+str(i+1), player), lambda state, i=i: state.has("Waterfall Population Pack", player, math.ceil((i+1)/state.multiworld.kill_sanity_pack_size[player].value)))
            set_rule(multiworld.get_location("Hotland Kill "+str(i+1), player), lambda state, i=i: state.has("Hotland Population Pack", player, math.ceil((i+1)/state.multiworld.kill_sanity_pack_size[player].value)) and (state.can_reach("Hotland", "Region", player) or state.can_reach("Core", "Region", player)))
        for i in range(18, 20):
            set_rule(multiworld.get_location("Ruins Kill "+str(i+1), player), lambda state, i=i: state.has("Ruins Population Pack", player, math.ceil((i+1)/state.multiworld.kill_sanity_pack_size[player].value)))
            set_rule(multiworld.get_location("Hotland Kill "+str(i+1), player), lambda state, i=i: state.has("Hotland Population Pack", player, math.ceil((i+1)/state.multiworld.kill_sanity_pack_size[player].value)) and (state.can_reach("Hotland", "Region", player) or state.can_reach("Core", "Region", player)))
        for i in range(20, 40):
            set_rule(multiworld.get_location("Hotland Kill "+str(i+1), player), lambda state, i=i: state.has("Hotland Population Pack", player, math.ceil((i+1)/state.multiworld.kill_sanity_pack_size[player].value)) and (state.can_reach("Hotland", "Region", player) or state.can_reach("Core", "Region", player)))
    if _undertale_is_route(multiworld.state, player, 2) and \
            (bool(multiworld.rando_love[player].value) or bool(multiworld.rando_stats[player].value)):
        maxlv = 1
        while maxlv < 20:
            maxlv += 1
            if multiworld.rando_stats[player]:
                set_rule(multiworld.get_location(("ATK "+str(maxlv)), player),
                                 lambda state, maxlv=maxlv: _undertale_return_reachable_level(state, _undertale_exp_available(state, player)) >= maxlv)
                set_rule(multiworld.get_location(("HP "+str(maxlv)), player),
                                 lambda state, maxlv=maxlv: _undertale_return_reachable_level(state, _undertale_exp_available(state, player)) >= maxlv)
                if maxlv == 5 or maxlv == 9 or maxlv == 13 or maxlv == 17:
                    set_rule(multiworld.get_location(("DEF "+str(maxlv)), player),
                                     lambda state, maxlv=maxlv: _undertale_return_reachable_level(state, _undertale_exp_available(state, player)) >= maxlv)
            if multiworld.rando_love[player]:
                add_rule(multiworld.get_location(("LOVE "+str(maxlv)), player),
                                 lambda state, maxlv=maxlv: _undertale_return_reachable_level(state, _undertale_exp_available(state, player)) >= maxlv)
    set_rule(multiworld.get_location("Snowman", player),
             lambda state: state.can_reach("Snowdin Town", "Region", player))
    set_rule(multiworld.get_location("Mettaton Fight", player),
             lambda state: state.can_reach("Core Exit", "Entrance", player) and (not bool(state.multiworld.kill_sanity[player].value) or not _undertale_is_route(state, player, 2) or state.has("Hotland Population Pack", player, math.ceil(40/state.multiworld.kill_sanity_pack_size[player].value))))
    set_rule(multiworld.get_location("Bunny 1", player),
             lambda state: state.can_reach("Snowdin Town", "Region", player) and state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Bunny 2", player),
             lambda state: state.can_reach("Snowdin Town", "Region", player) and state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Bunny 3", player),
             lambda state: state.can_reach("Snowdin Town", "Region", player) and state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Bunny 4", player),
             lambda state: state.can_reach("Snowdin Town", "Region", player) and state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Astro 1", player),
             lambda state: state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Astro 2", player),
             lambda state: state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Gerson 1", player),
             lambda state: state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Gerson 2", player),
             lambda state: state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Gerson 3", player),
             lambda state: state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Gerson 4", player),
             lambda state: state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Present Knife", player),
             lambda state: state.can_reach("New Home", "Region", player) and (not bool(state.multiworld.kill_sanity[player].value) or not _undertale_is_route(state, player, 2) or state.has("Hotland Population Pack", player, math.ceil(40/state.multiworld.kill_sanity_pack_size[player].value))))
    set_rule(multiworld.get_location("Present Locket", player),
             lambda state: state.can_reach("New Home", "Region", player) and (not bool(state.multiworld.kill_sanity[player].value) or not _undertale_is_route(state, player, 2) or state.has("Hotland Population Pack", player, math.ceil(40/state.multiworld.kill_sanity_pack_size[player].value))))
    set_rule(multiworld.get_location("Left New Home Key", player),
             lambda state: state.can_reach("New Home", "Region", player) and (not bool(state.multiworld.kill_sanity[player].value) or not _undertale_is_route(state, player, 2) or state.has("Hotland Population Pack", player, math.ceil(40/state.multiworld.kill_sanity_pack_size[player].value))))
    set_rule(multiworld.get_location("Right New Home Key", player),
             lambda state: state.can_reach("New Home", "Region", player) and (not bool(state.multiworld.kill_sanity[player].value) or not _undertale_is_route(state, player, 2) or state.has("Hotland Population Pack", player, math.ceil(40/state.multiworld.kill_sanity_pack_size[player].value))))
    set_rule(multiworld.get_location("Trash Burger", player),
             lambda state: state.can_reach("Core", "Region", player))
    set_rule(multiworld.get_location("Quiche Bench", player),
             lambda state: state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Tutu Hidden", player),
             lambda state: state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Grass Shoes", player),
             lambda state: state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("TemmieShop 1", player),
             lambda state: state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("TemmieShop 2", player),
             lambda state: state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("TemmieShop 3", player),
             lambda state: state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("TemmieShop 4", player),
             lambda state: state.can_reach("Waterfall", "Region", player) and state.has("1000G", player, 2))
    set_rule(multiworld.get_location("Noodles Fridge", player),
             lambda state: state.can_reach("Hotland", "Region", player))
    set_rule(multiworld.get_location("Pan Hidden", player),
             lambda state: state.can_reach("Hotland", "Region", player))
    set_rule(multiworld.get_location("Bratty Catty 1", player),
             lambda state: state.can_reach("News Show", "Region", player) and state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Bratty Catty 2", player),
             lambda state: state.can_reach("News Show", "Region", player) and state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Bratty Catty 3", player),
             lambda state: state.can_reach("News Show", "Region", player) and state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Bratty Catty 4", player),
             lambda state: state.can_reach("News Show", "Region", player) and state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Burgerpants 1", player),
             lambda state: state.can_reach("News Show", "Region", player) and state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Burgerpants 2", player),
             lambda state: state.can_reach("News Show", "Region", player) and state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Burgerpants 3", player),
             lambda state: state.can_reach("News Show", "Region", player) and state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Burgerpants 4", player),
             lambda state: state.can_reach("News Show", "Region", player) and state.can_reach("Waterfall", "Region", player))


# Sets rules on completion condition
def set_completion_rules(multiworld: MultiWorld, player: int):
    completion_requirements = lambda state: state.can_reach("Barrier", "Region", player)
    if _undertale_is_route(multiworld.state, player, 1):
        completion_requirements = lambda state: state.can_reach("True Lab", "Region", player)

    multiworld.completion_condition[player] = lambda state: completion_requirements(state)
