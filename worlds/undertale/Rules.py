from worlds.generic.Rules import set_rule, add_rule, add_item_rule
from BaseClasses import MultiWorld, CollectionState


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


def _undertale_has_plot(state: CollectionState, player: int, item: str):
    if item == "Complete Skeleton":
        return state.has("Complete Skeleton", player)
    elif item == "Fish":
        return state.has("Fish", player)
    elif item == "Mettaton Plush":
        return state.has("Mettaton Plush", player)
    elif item == "DT Extractor":
        return state.has("DT Extractor", player)


def _undertale_can_level(state: CollectionState, exp: int, lvl: int):
    if exp >= 10 and lvl == 1:
        return True
    elif exp >= 30 and lvl == 2:
        return True
    elif exp >= 70 and lvl == 3:
        return True
    elif exp >= 120 and lvl == 4:
        return True
    elif exp >= 200 and lvl == 5:
        return True
    elif exp >= 300 and lvl == 6:
        return True
    elif exp >= 500 and lvl == 7:
        return True
    elif exp >= 800 and lvl == 8:
        return True
    elif exp >= 1200 and lvl == 9:
        return True
    elif exp >= 1700 and lvl == 10:
        return True
    elif exp >= 2500 and lvl == 11:
        return True
    elif exp >= 3500 and lvl == 12:
        return True
    elif exp >= 5000 and lvl == 13:
        return True
    elif exp >= 7000 and lvl == 14:
        return True
    elif exp >= 10000 and lvl == 15:
        return True
    elif exp >= 15000 and lvl == 16:
        return True
    elif exp >= 25000 and lvl == 17:
        return True
    elif exp >= 50000 and lvl == 18:
        return True
    elif exp >= 99999 and lvl == 19:
        return True
    return False


# Sets rules on entrances and advancements that are always applied
def set_rules(multiworld: MultiWorld, player: int):
    set_rule(multiworld.get_entrance("Ruins Hub", player), lambda state: state.has("Ruins Key", player))
    set_rule(multiworld.get_entrance("Snowdin Hub", player), lambda state: state.has("Snowdin Key", player))
    set_rule(multiworld.get_entrance("Waterfall Hub", player), lambda state: state.has("Waterfall Key", player))
    set_rule(multiworld.get_entrance("Hotland Hub", player), lambda state: state.has("Hotland Key", player))
    set_rule(multiworld.get_entrance("Core Hub", player), lambda state: state.has("Core Key", player))
    set_rule(multiworld.get_entrance("Core Exit", player),
             lambda state: _undertale_has_plot(state, player, "Mettaton Plush") and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Hotland Encounter", player, 40)))
    set_rule(multiworld.get_entrance("New Home Exit", player),
             lambda state: ((state.has("Left Home Key", player) and
                            state.has("Right Home Key", player)) or
                           state.has("Key Piece", player, state.multiworld.key_pieces[player])) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Hotland Encounter", player, 40)) and (state.has("Jump", player) or not _undertale_is_route(multiworld.state, player, 2)))
    if _undertale_is_route(multiworld.state, player, 1):
        set_rule(multiworld.get_entrance("Papyrus\" Home Entrance", player),
                 lambda state: _undertale_has_plot(state, player, "Complete Skeleton"))
        set_rule(multiworld.get_entrance("Undyne\"s Home Entrance", player),
                 lambda state: _undertale_has_plot(state, player, "Fish") and state.has("Papyrus Date", player))
        set_rule(multiworld.get_entrance("Lab Elevator", player),
                 lambda state: state.has("Alphys Date", player) and _undertale_has_plot(state, player, "DT Extractor") and ((state.has("Left Home Key", player) and
                            state.has("Right Home Key", player)) or
                           state.has("Key Piece", player, state.multiworld.key_pieces[player])))
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
        set_rule(multiworld.get_location("Dog Sale 1", player),
                 lambda state: state.can_reach("Cooking Show", "Region", player))
        set_rule(multiworld.get_location("Cat Sale", player),
                 lambda state: state.can_reach("Cooking Show", "Region", player))
        set_rule(multiworld.get_location("Dog Sale 2", player),
                 lambda state: state.can_reach("Cooking Show", "Region", player))
        set_rule(multiworld.get_location("Dog Sale 3", player),
                 lambda state: state.can_reach("Cooking Show", "Region", player))
        set_rule(multiworld.get_location("Dog Sale 4", player),
                 lambda state: state.can_reach("Cooking Show", "Region", player))
        set_rule(multiworld.get_location("Hush Trade", player),
                 lambda state: state.can_reach("News Show", "Region", player) and state.has("Hot Dog...?", player, 1))
        set_rule(multiworld.get_location("Letter Quest", player),
                 lambda state: state.can_reach("New Home Exit", "Entrance", player) and state.has("Undyne Date", player))
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
    if _undertale_is_route(multiworld.state, player, 2) and multiworld.encounter_sanity[player]:
        set_rule(multiworld.get_location("Toriel Fight", player), lambda state: state.has("Progressive Ruins Encounter", player, 20))
        set_rule(multiworld.get_location("Papyrus Fight", player), lambda state: state.has("Progressive Snowdin Encounter", player, 16))
        set_rule(multiworld.get_location("Undyne Fight", player), lambda state: state.has("Progressive Waterfall Encounter", player, 18))
        for i in range(0, 16):
            set_rule(multiworld.get_location("Ruins Kill "+str(i+1), player), lambda state, i=i: state.has("Progressive Ruins Encounter", player, i+1))
            set_rule(multiworld.get_location("Snowdin Kill "+str(i+1), player), lambda state, i=i: state.has("Progressive Snowdin Encounter", player, i+1))
            set_rule(multiworld.get_location("Waterfall Kill "+str(i+1), player), lambda state, i=i: state.has("Progressive Waterfall Encounter", player, i+1))
            set_rule(multiworld.get_location("Hotland Kill "+str(i+1), player), lambda state, i=i: state.has("Progressive Hotland Encounter", player, i+1))
        for i in range(16, 18):
            set_rule(multiworld.get_location("Ruins Kill "+str(i+1), player), lambda state, i=i: state.has("Progressive Ruins Encounter", player, i+1))
            set_rule(multiworld.get_location("Waterfall Kill "+str(i+1), player), lambda state, i=i: state.has("Progressive Waterfall Encounter", player, i+1))
            set_rule(multiworld.get_location("Hotland Kill "+str(i+1), player), lambda state, i=i: state.has("Progressive Hotland Encounter", player, i+1))
        for i in range(18, 20):
            set_rule(multiworld.get_location("Ruins Kill "+str(i+1), player), lambda state, i=i: state.has("Progressive Ruins Encounter", player, i+1))
            set_rule(multiworld.get_location("Hotland Kill "+str(i+1), player), lambda state, i=i: state.has("Progressive Hotland Encounter", player, i+1))
        for i in range(20, 40):
            set_rule(multiworld.get_location("Hotland Kill "+str(i+1), player), lambda state, i=i: state.has("Progressive Hotland Encounter", player, i+1))
    if _undertale_is_route(multiworld.state, player, 2) and \
            (multiworld.rando_love[player] or multiworld.rando_stats[player]):
        maxlv = 1
        exp = 190
        curarea = "Old Home"

        while maxlv < 20:
            maxlv += 1
            if multiworld.rando_love[player]:
                set_rule(multiworld.get_location(("LOVE " + str(maxlv)), player), lambda state: False)
            if multiworld.rando_stats[player]:
                set_rule(multiworld.get_location(("ATK "+str(maxlv)), player), lambda state: False)
                set_rule(multiworld.get_location(("HP "+str(maxlv)), player), lambda state: False)
                if maxlv in {5, 9, 13, 17}:
                    set_rule(multiworld.get_location(("DEF "+str(maxlv)), player), lambda state: False)
        maxlv = 1
        while maxlv < 20:
            while _undertale_can_level(multiworld.state, exp, maxlv):
                maxlv += 1
                if multiworld.rando_stats[player]:
                    if curarea == "Old Home":
                        add_rule(multiworld.get_location(("ATK "+str(maxlv)), player),
                                 lambda state: (state.can_reach("Old Home", "Region", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Ruins Encounter", player, 20))), combine="or")
                        add_rule(multiworld.get_location(("HP "+str(maxlv)), player),
                                 lambda state: (state.can_reach("Old Home", "Region", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Ruins Encounter", player, 20))), combine="or")
                        if maxlv == 5 or maxlv == 9 or maxlv == 13 or maxlv == 17:
                            add_rule(multiworld.get_location(("DEF "+str(maxlv)), player),
                                     lambda state: (state.can_reach("Old Home", "Region", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Ruins Encounter", player, 20))), combine="or")
                    elif curarea == "Snowdin Town":
                        add_rule(multiworld.get_location(("ATK "+str(maxlv)), player),
                                 lambda state: (state.can_reach("Snowdin Town", "Region", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Snowdin Encounter", player, 16))), combine="or")
                        add_rule(multiworld.get_location(("HP "+str(maxlv)), player),
                                 lambda state: (state.can_reach("Snowdin Town", "Region", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Snowdin Encounter", player, 16))), combine="or")
                        if maxlv == 5 or maxlv == 9 or maxlv == 13 or maxlv == 17:
                            add_rule(multiworld.get_location(("DEF "+str(maxlv)), player),
                                     lambda state: (state.can_reach("Snowdin Town", "Region", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Snowdin Encounter", player, 16))), combine="or")
                    elif curarea == "Waterfall":
                        add_rule(multiworld.get_location(("ATK "+str(maxlv)), player),
                                 lambda state: (state.can_reach("Waterfall", "Region", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Waterfall Encounter", player, 18))), combine="or")
                        add_rule(multiworld.get_location(("HP "+str(maxlv)), player),
                                 lambda state: (state.can_reach("Waterfall", "Region", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Waterfall Encounter", player, 18))), combine="or")
                        if maxlv == 5 or maxlv == 9 or maxlv == 13 or maxlv == 17:
                            add_rule(multiworld.get_location(("DEF "+str(maxlv)), player),
                                     lambda state: (state.can_reach("Waterfall", "Region", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Waterfall Encounter", player, 18))), combine="or")
                    elif curarea == "News Show":
                        add_rule(multiworld.get_location(("ATK "+str(maxlv)), player),
                                 lambda state: (state.can_reach("News Show", "Region", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Hotland Encounter", player, 40))), combine="or")
                        add_rule(multiworld.get_location(("HP "+str(maxlv)), player),
                                 lambda state: (state.can_reach("News Show", "Region", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Hotland Encounter", player, 40))), combine="or")
                        if maxlv == 5 or maxlv == 9 or maxlv == 13 or maxlv == 17:
                            add_rule(multiworld.get_location(("DEF "+str(maxlv)), player),
                                     lambda state: (state.can_reach("News Show", "Region", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Hotland Encounter", player, 40))), combine="or")
                    elif curarea == "Core":
                        add_rule(multiworld.get_location(("ATK "+str(maxlv)), player),
                                 lambda state: (state.can_reach("Core Exit", "Entrance", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Hotland Encounter", player, 40))), combine="or")
                        add_rule(multiworld.get_location(("HP "+str(maxlv)), player),
                                 lambda state: (state.can_reach("Core Exit", "Entrance", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Hotland Encounter", player, 40))), combine="or")
                        if maxlv == 5 or maxlv == 9 or maxlv == 13 or maxlv == 17:
                            add_rule(multiworld.get_location(("DEF "+str(maxlv)), player),
                                     lambda state: (state.can_reach("Core Exit", "Entrance", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Hotland Encounter", player, 40))), combine="or")
                    elif curarea == "Sans":
                        add_rule(multiworld.get_location(("ATK "+str(maxlv)), player),
                                 lambda state: (state.can_reach("New Home Exit", "Entrance", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Hotland Encounter", player, 40))), combine="or")
                        add_rule(multiworld.get_location(("HP "+str(maxlv)), player),
                                 lambda state: (state.can_reach("New Home Exit", "Entrance", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Hotland Encounter", player, 40))), combine="or")
                        if maxlv == 5 or maxlv == 9 or maxlv == 13 or maxlv == 17:
                            add_rule(multiworld.get_location(("DEF "+str(maxlv)), player),
                                     lambda state: (state.can_reach("New Home Exit", "Entrance", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Hotland Encounter", player, 40))), combine="or")
                if multiworld.rando_love[player]:
                    if curarea == "Old Home":
                        add_rule(multiworld.get_location(("LOVE "+str(maxlv)), player),
                                 lambda state: (state.can_reach("Old Home", "Region", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Ruins Encounter", player, 20))), combine="or")
                    elif curarea == "Snowdin Town":
                        add_rule(multiworld.get_location(("LOVE "+str(maxlv)), player),
                                 lambda state: (state.can_reach("Snowdin Town", "Region", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Snowdin Encounter", player, 16))), combine="or")
                    elif curarea == "Waterfall":
                        add_rule(multiworld.get_location(("LOVE "+str(maxlv)), player),
                                 lambda state: (state.can_reach("Waterfall", "Region", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Waterfall Encounter", player, 18))), combine="or")
                    elif curarea == "News Show":
                        add_rule(multiworld.get_location(("LOVE "+str(maxlv)), player),
                                 lambda state: (state.can_reach("News Show", "Region", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Hotland Encounter", player, 40))), combine="or")
                    elif curarea == "Core":
                        add_rule(multiworld.get_location(("LOVE "+str(maxlv)), player),
                                 lambda state: (state.can_reach("Core Exit", "Entrance", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Hotland Encounter", player, 40))), combine="or")
                    elif curarea == "Sans":
                        add_rule(multiworld.get_location(("LOVE "+str(maxlv)), player),
                                 lambda state: (state.can_reach("New Home Exit", "Entrance", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Hotland Encounter", player, 40))), combine="or")
            if curarea == "Old Home":
                curarea = "Snowdin Town"
                maxlv = 1
                exp = 407
            elif curarea == "Snowdin Town":
                curarea = "Waterfall"
                maxlv = 1
                exp = 1643
            elif curarea == "Waterfall":
                curarea = "News Show"
                maxlv = 1
                exp = 3320
            elif curarea == "News Show":
                curarea = "Core"
                maxlv = 1
                exp = 50000
            elif curarea == "Core":
                curarea = "Sans"
                maxlv = 1
                exp = 99999
    set_rule(multiworld.get_location("Snowman", player),
             lambda state: state.can_reach("Snowdin Town", "Region", player))
    set_rule(multiworld.get_location("Mettaton Fight", player),
             lambda state: state.can_reach("Core Exit", "Entrance", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Hotland Encounter", player, 40)))
    set_rule(multiworld.get_location("Bunny 1", player),
             lambda state: state.can_reach("Snowdin Town", "Region", player))
    set_rule(multiworld.get_location("Bunny 2", player),
             lambda state: state.can_reach("Snowdin Town", "Region", player))
    set_rule(multiworld.get_location("Bunny 3", player),
             lambda state: state.can_reach("Snowdin Town", "Region", player))
    set_rule(multiworld.get_location("Bunny 4", player),
             lambda state: state.can_reach("Snowdin Town", "Region", player))
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
             lambda state: state.can_reach("New Home", "Region", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Hotland Encounter", player, 40)))
    set_rule(multiworld.get_location("Present Locket", player),
             lambda state: state.can_reach("New Home", "Region", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Hotland Encounter", player, 40)))
    set_rule(multiworld.get_location("Left New Home Key", player),
             lambda state: state.can_reach("New Home", "Region", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Hotland Encounter", player, 40)))
    set_rule(multiworld.get_location("Right New Home Key", player),
             lambda state: state.can_reach("New Home", "Region", player) and (not state.multiworld.encounter_sanity[player] or state.has("Progressive Hotland Encounter", player, 40)))
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
             lambda state: state.can_reach("News Show", "Region", player))
    set_rule(multiworld.get_location("Bratty Catty 2", player),
             lambda state: state.can_reach("News Show", "Region", player))
    set_rule(multiworld.get_location("Bratty Catty 3", player),
             lambda state: state.can_reach("News Show", "Region", player))
    set_rule(multiworld.get_location("Bratty Catty 4", player),
             lambda state: state.can_reach("News Show", "Region", player))
    set_rule(multiworld.get_location("Burgerpants 1", player),
             lambda state: state.can_reach("News Show", "Region", player))
    set_rule(multiworld.get_location("Burgerpants 2", player),
             lambda state: state.can_reach("News Show", "Region", player))
    set_rule(multiworld.get_location("Burgerpants 3", player),
             lambda state: state.can_reach("News Show", "Region", player))
    set_rule(multiworld.get_location("Burgerpants 4", player),
             lambda state: state.can_reach("News Show", "Region", player))


# Sets rules on completion condition
def set_completion_rules(multiworld: MultiWorld, player: int):
    completion_requirements = lambda state: state.can_reach("New Home Exit", "Entrance", player)
    if _undertale_is_route(multiworld.state, player, 1):
        completion_requirements = lambda state: state.can_reach("True Lab", "Region", player)

    multiworld.completion_condition[player] = lambda state: completion_requirements(state)
