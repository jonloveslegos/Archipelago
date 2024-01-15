from ..generic.Rules import set_rule
from BaseClasses import MultiWorld, CollectionState


def _fnaf_world_can_access_chara_area(state: CollectionState, player: int, name: str):
    result = False
    temp_name = name
    if temp_name == "Fazbear Hills":
        result = True
    if temp_name == "Choppy's Woods":
        result = True
    if temp_name == "Dusting Fields":
        result = result or _fnaf_world_can_access(state, player, "Choppy's Woods")
        result = result or _fnaf_world_can_access(state, player, "Dusting Fields")
        temp_name = "Lilygear Lake"
    if temp_name == "Lilygear Lake":
        result = result or _fnaf_world_can_access(state, player, "Lilygear Lake")
        temp_name = "Mysterious Mine"
    if temp_name == "Mysterious Mine":
        result = result or _fnaf_world_can_access(state, player, "Lilygear Lake")
        result = result or _fnaf_world_can_access(state, player, "Dusting Fields")
        result = result or _fnaf_world_can_access(state, player, "Choppy's Woods")
        temp_name = "Blacktomb Yard"
    if temp_name == "Blacktomb Yard":
        result = result or _fnaf_world_can_access(state, player, "Lilygear Lake")
        result = result or _fnaf_world_can_access(state, player, "Blacktomb Yard")
        temp_name = "Deep-Metal Mine"
    if temp_name == "Deep-Metal Mine":
        result = result or _fnaf_world_can_access(state, player, "Lilygear Lake")
        result = result or _fnaf_world_can_access(state, player, "Blacktomb Yard")
        temp_name = "Pinwheel Circus"
    if temp_name == "Pinwheel Circus":
        result = result or _fnaf_world_can_access(state, player, "Lilygear Lake")
        result = result or _fnaf_world_can_access(state, player, "Blacktomb Yard")
        result = result or _fnaf_world_can_access(state, player, "Pinwheel Circus")
        temp_name = "Top Layer"
    if temp_name == "Top Layer":
        result = result or (_fnaf_world_can_access(state, player, "Lilygear Lake") and state.multiworld.worlds[player].options.hard_logic)
        result = result or (_fnaf_world_can_access(state, player, "Dusting Fields") and state.multiworld.worlds[player].options.hard_logic)
        result = result or (_fnaf_world_can_access(state, player, "Choppy's Woods") and state.multiworld.worlds[player].options.hard_logic)
        result = result or _fnaf_world_can_access(state, player, "Blacktomb Yard")
        temp_name = "Pinwheel Funhouse"
    if temp_name == "Pinwheel Funhouse":
        result = result or _fnaf_world_can_access(state, player, "Pinwheel Funhouse")
    result = result and (not state.multiworld.worlds[player].options.require_find_char or state.has("Find Characters", player))
    return result


def _fnaf_world_can_access(state: CollectionState, player: int, name: str):
    result = False
    if (state.multiworld.worlds[player].options.area_warping.current_key == "warp_item" and state.has("Warp Access", player)) or state.multiworld.worlds[player].options.area_warping.current_key == "always":
        if name == "Choppy's Woods":
            result = state.has("Choppy's Woods Access Switch", player) or state.has("Dusting Fields Access", player)
        elif name == "Lilygear Lake":
            result = state.has("Pinwheel Circus Access Switch", player) or state.has("Lilygear Lake Access Switch", player) or state.has("Blacktomb Yard Access Switch", player)
        elif name == "Dusting Fields":
            result = state.has("Dusting Fields Access", player)
        elif name == "Blacktomb Yard":
            result = state.has("Blacktomb Yard Access Switch", player)
        elif name == "Pinwheel Funhouse":
            result = state.has("Pinwheel Circus Access Switch", player)
        elif name == "Pinwheel Circus":
            result = state.has("Pinwheel Circus Access Switch", player)
    if not result:
        if name == "Choppy's Woods":
            result = state.has("Choppy's Woods Access Switch", player)
        elif name == "Lilygear Lake":
            result = state.has("Lilygear Lake Access Switch", player)
        elif name == "Dusting Fields":
            result = _fnaf_world_can_access(state, player, "Choppy's Woods") and state.has("Dusting Fields Access", player)
        elif name == "Blacktomb Yard":
            result = state.has("Blacktomb Yard Access Switch", player) and _fnaf_world_can_access(state, player, "Lilygear Lake")
        elif name == "Pinwheel Funhouse":
            result = _fnaf_world_can_access(state, player, "Blacktomb Yard") or (state.has("Pinwheel Circus Access Switch", player) and _fnaf_world_can_access(state, player, "Lilygear Lake"))
        elif name == "Pinwheel Circus":
            result = _fnaf_world_can_access(state, player, "Lilygear Lake")
    return result


def _fnaf_world_has_chip(state: CollectionState, player: int, name: str):
    return state.has(name, player)


# Sets rules on entrances and advancements that are always applied
def set_rules(world: MultiWorld, player: int):

    # Start with
    set_rule(world.get_location("Freddy", player), lambda state: True)
    set_rule(world.get_location("Bonnie", player), lambda state: True)
    set_rule(world.get_location("Chica", player), lambda state: True)
    set_rule(world.get_location("Foxy", player), lambda state: True)
    set_rule(world.get_location("Toy Bonnie", player), lambda state: True)
    set_rule(world.get_location("Toy Chica", player), lambda state: True)
    set_rule(world.get_location("Toy Freddy", player), lambda state: True)
    set_rule(world.get_location("Mangle", player), lambda state: True)

    # Always available
    set_rule(world.get_location("Balloon Boy", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Fazbear Hills"))
    set_rule(world.get_location("JJ", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Fazbear Hills"))
    set_rule(world.get_location("Phantom Freddy", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Fazbear Hills"))
    set_rule(world.get_location("Phantom Chica", player), lambda state:  _fnaf_world_can_access_chara_area(state, player, "Fazbear Hills"))
    set_rule(world.get_location("Phantom BB", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Fazbear Hills"))
    set_rule(world.get_location("Fazbear Hills: Endo Shop 1", player), lambda state: True)
    set_rule(world.get_location("Fazbear Hills: Auto Chipper Chest 1", player), lambda state: True)
    set_rule(world.get_location("Fazbear Hills: Auto Chipper Chest 2", player), lambda state: True)
    set_rule(world.get_location("Choppy's Woods: Near Lolbit South Chest", player), lambda state: True)
    set_rule(world.get_location("Fazbear Hills: Lolbit Shop 1", player), lambda state: True)
    set_rule(world.get_location("Choppy's Woods: Switch", player), lambda state: True)
    set_rule(world.get_location("Choppy's Woods: Lolbit Shop 1", player), lambda state: True)
    set_rule(world.get_location("Fazbear Hills: Pearl", player), lambda state: True)
    set_rule(world.get_location("Withered Bonnie", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Choppy's Woods"))
    set_rule(world.get_location("Phantom Foxy", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Choppy's Woods"))
    set_rule(world.get_location("Phantom Mangle", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Choppy's Woods"))
    set_rule(world.get_location("Fazbear Hills: Endo Shop 2", player), lambda state: world.worlds[player].options.hard_logic or _fnaf_world_can_access(state, player, "Choppy's Woods") or _fnaf_world_can_access(state, player, "Lilygear Lake"))
    set_rule(world.get_location("Fazbear Hills: Endo Shop 3", player), lambda state: world.worlds[player].options.hard_logic or _fnaf_world_can_access(state, player, "Blacktomb Yard"))
    set_rule(world.get_location("Fazbear Hills: Lolbit Shop 2", player), lambda state: world.worlds[player].options.hard_logic or _fnaf_world_can_access(state, player, "Choppy's Woods") or _fnaf_world_can_access(state, player, "Lilygear Lake"))
    set_rule(world.get_location("Fazbear Hills: Lolbit Shop 3", player), lambda state: world.worlds[player].options.hard_logic or _fnaf_world_can_access(state, player, "Blacktomb Yard"))
    set_rule(world.get_location("Choppy's Woods: Lolbit Shop 2", player), lambda state: world.worlds[player].options.hard_logic or _fnaf_world_can_access(state, player, "Choppy's Woods") or _fnaf_world_can_access(state, player, "Lilygear Lake"))
    set_rule(world.get_location("Choppy's Woods: Lolbit Shop 3", player), lambda state: world.worlds[player].options.hard_logic or _fnaf_world_can_access(state, player, "Blacktomb Yard"))

    # Update 2 secret path stuff
    set_rule(world.get_location("Jack-O-Bonnie", player), lambda state: True)
    set_rule(world.get_location("Jack-O-Chica", player), lambda state: True)
    set_rule(world.get_location("Animdude", player), lambda state: True)
    set_rule(world.get_location("Mr. Chipper", player), lambda state: True)
    set_rule(world.get_location("Nightmare BB", player), lambda state: True)
    set_rule(world.get_location("Nightmarionne", player), lambda state: True)
    set_rule(world.get_location("Coffee", player), lambda state: True)
    set_rule(world.get_location("Purpleguy", player), lambda state: True)

    # Requires "Choppy's Woods Access Switch"
    set_rule(world.get_location("Choppy's Woods: Auto Chipper Chest", player), lambda state: _fnaf_world_can_access(state, player, "Choppy's Woods"))
    set_rule(world.get_location("Dusting Fields: False Tree Chest", player), lambda state: _fnaf_world_can_access(state, player, "Dusting Fields"))
    set_rule(world.get_location("Dusting Fields: Warp Unlock", player), lambda state: _fnaf_world_can_access(state, player, "Choppy's Woods"))
    set_rule(world.get_location("Mysterious Mine: Warp 2 Chest", player), lambda state: _fnaf_world_can_access(state, player, "Dusting Fields"))
    set_rule(world.get_location("Mysterious Mine: Dusting Fields Cave Entrance Bottom Chest", player), lambda state: _fnaf_world_can_access(state, player, "Dusting Fields"))
    set_rule(world.get_location("Mysterious Mine: Dusting Fields Cave Entrance Top Chest", player), lambda state: _fnaf_world_can_access(state, player, "Dusting Fields"))
    set_rule(world.get_location("Dusting Fields: Lolbit Shop 1", player), lambda state: _fnaf_world_can_access(state, player, "Dusting Fields"))
    set_rule(world.get_location("Dusting Fields: Lolbit Shop 2", player), lambda state: _fnaf_world_can_access(state, player, "Dusting Fields"))
    set_rule(world.get_location("Dusting Fields: Lolbit Shop 3", player), lambda state: _fnaf_world_can_access(state, player, "Dusting Fields") and (world.worlds[player].options.hard_logic or _fnaf_world_can_access(state, player, "Blacktomb Yard")))
    set_rule(world.get_location("Lilygear Lake: Switch", player), lambda state: _fnaf_world_can_access(state, player, "Lilygear Lake") or _fnaf_world_can_access(state, player, "Dusting Fields"))
    set_rule(world.get_location("Choppy's Woods: Near Lolbit North Chest", player), lambda state: _fnaf_world_can_access(state, player, "Lilygear Lake"))
    set_rule(world.get_location("Lilygear Lake: Clip From Choppy's Woods Chest", player), lambda state: _fnaf_world_can_access(state, player, "Choppy's Woods"))
    set_rule(world.get_location("Fazbear Hills: Clip From Dusting Fields Chest", player), lambda state: _fnaf_world_can_access(state, player, "Dusting Fields"))
    set_rule(world.get_location("Withered Foxy", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Dusting Fields"))
    set_rule(world.get_location("Withered Chica", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Dusting Fields"))
    set_rule(world.get_location("Withered Freddy", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Dusting Fields"))
    set_rule(world.get_location("Golden Freddy", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Mysterious Mine"))
    set_rule(world.get_location("Paperpals", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Mysterious Mine"))
    set_rule(world.get_location("Nightmare Freddy", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Mysterious Mine"))
    set_rule(world.get_location("Shadow Freddy", player),
             lambda state: _fnaf_world_can_access_chara_area(state, player, "Lilygear Lake"))
    set_rule(world.get_location("Marionette", player),
             lambda state: _fnaf_world_can_access_chara_area(state, player, "Lilygear Lake"))
    set_rule(world.get_location("Phantom Marionette", player),
             lambda state: _fnaf_world_can_access_chara_area(state, player, "Lilygear Lake"))
    set_rule(world.get_location("Crying Child", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Top Layer"))
    set_rule(world.get_location("Funtime Foxy", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Top Layer"))
    set_rule(world.get_location("Nightmare Fredbear", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Top Layer"))

    # Requires "Lilygear Lake Access Switch"
    set_rule(world.get_location("Mysterious Mine: Topmost Cave Entrance Chest 1", player), lambda state: _fnaf_world_can_access(state, player, "Lilygear Lake"))
    set_rule(world.get_location("Mysterious Mine: Topmost Cave Entrance Chest 2", player), lambda state: _fnaf_world_can_access(state, player, "Lilygear Lake"))
    set_rule(world.get_location("Mysterious Mine: Lolbit Shop 1", player), lambda state: _fnaf_world_can_access(state, player, "Lilygear Lake"))
    set_rule(world.get_location("Mysterious Mine: Lolbit Shop 2", player), lambda state: _fnaf_world_can_access(state, player, "Lilygear Lake"))
    set_rule(world.get_location("Mysterious Mine: Lolbit Shop 3", player), lambda state: _fnaf_world_can_access(state, player, "Lilygear Lake") and (world.worlds[player].options.hard_logic or _fnaf_world_can_access(state, player, "Blacktomb Yard")))
    set_rule(world.get_location("Pinwheel Circus: Lolbit Shop 1", player), lambda state: _fnaf_world_can_access(state, player, "Lilygear Lake"))
    set_rule(world.get_location("Pinwheel Circus: Lolbit Shop 2", player), lambda state: _fnaf_world_can_access(state, player, "Lilygear Lake"))
    set_rule(world.get_location("Pinwheel Circus: Lolbit Shop 3", player), lambda state: _fnaf_world_can_access(state, player, "Lilygear Lake") and (world.worlds[player].options.hard_logic or _fnaf_world_can_access(state, player, "Blacktomb Yard")))
    set_rule(world.get_location("Choppy's Woods: False Trees Near Tent Chest", player), lambda state: _fnaf_world_can_access(state, player, "Lilygear Lake"))
    set_rule(world.get_location("Deep-Metal Mine: Lilygear Lake False Wall To Blacktomb Yard Chest", player), lambda state: _fnaf_world_can_access(state, player, "Lilygear Lake"))
    set_rule(world.get_location("Nightmare Bonnie", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Blacktomb Yard"))
    set_rule(world.get_location("Nightmare Chica", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Blacktomb Yard"))
    set_rule(world.get_location("Nightmare Foxy", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Deep-Metal Mine"))
    set_rule(world.get_location("Endo 01", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Deep-Metal Mine"))
    set_rule(world.get_location("Endo 02", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Deep-Metal Mine"))
    set_rule(world.get_location("Plushtrap", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Deep-Metal Mine"))
    set_rule(world.get_location("Endoplush", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Pinwheel Circus"))
    set_rule(world.get_location("Springtrap", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Pinwheel Circus"))
    set_rule(world.get_location("RWQFSFASXC", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Pinwheel Circus"))
    set_rule(world.get_location("Blacktomb Yard: Switch", player), lambda state: _fnaf_world_can_access(state, player, "Blacktomb Yard") or _fnaf_world_can_access(state, player, "Lilygear Lake"))

    # Requires "Blacktomb Yard Access Switch"
    set_rule(world.get_location("Blacktomb Yard: Near Bottom Chest", player), lambda state: _fnaf_world_can_access(state, player, "Blacktomb Yard"))
    set_rule(world.get_location("Blacktomb Yard: Lolbit Shop 1", player), lambda state: _fnaf_world_can_access(state, player, "Blacktomb Yard"))
    set_rule(world.get_location("Blacktomb Yard: Lolbit Shop 2", player), lambda state: _fnaf_world_can_access(state, player, "Blacktomb Yard"))
    set_rule(world.get_location("Blacktomb Yard: Lolbit Shop 3", player), lambda state: _fnaf_world_can_access(state, player, "Blacktomb Yard"))
    set_rule(world.get_location("Deep-Metal Mine: Lolbit Shop 1", player), lambda state: _fnaf_world_can_access(state, player, "Blacktomb Yard"))
    set_rule(world.get_location("Deep-Metal Mine: Lolbit Shop 2", player), lambda state: _fnaf_world_can_access(state, player, "Blacktomb Yard"))
    set_rule(world.get_location("Deep-Metal Mine: Lolbit Shop 3", player), lambda state: _fnaf_world_can_access(state, player, "Blacktomb Yard"))
    set_rule(world.get_location("Deep-Metal Mine: Near Lolbit Chest", player), lambda state: _fnaf_world_can_access(state, player, "Blacktomb Yard"))
    set_rule(world.get_location("Mysterious Mine: Clip From Blacktomb Yard Chest", player), lambda state: _fnaf_world_can_access(state, player, "Blacktomb Yard"))
    set_rule(world.get_location("Pinwheel Circus: Switch", player), lambda state: _fnaf_world_can_access(state, player, "Blacktomb Yard"))
    set_rule(world.get_location("Deep-Metal Mine: Tent Entrance before Browboy Chest", player), lambda state: _fnaf_world_can_access(state, player, "Blacktomb Yard"))
    set_rule(world.get_location("Pinwheel Circus: Past Browboy Chest", player), lambda state: _fnaf_world_can_access(state, player, "Blacktomb Yard"))
    set_rule(world.get_location("Pinwheel Funhouse: False Wall After Bubba Chest", player), lambda state: _fnaf_world_can_access(state, player, "Blacktomb Yard"))
    set_rule(world.get_location("Lilygear Lake: Key Switch", player), lambda state: _fnaf_world_can_access(state, player, "Lilygear Lake") and (_fnaf_world_can_access(state, player, "Blacktomb Yard") or state.has("Key Shortcut Switch", player)))
    set_rule(world.get_location("Lilygear Lake: Key", player), lambda state: _fnaf_world_can_access(state, player, "Lilygear Lake") and (_fnaf_world_can_access(state, player, "Blacktomb Yard") or state.has("Key Shortcut Switch", player)))
    set_rule(world.get_location("Nightmare", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Pinwheel Funhouse"))
    set_rule(world.get_location("Fredbear", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Pinwheel Funhouse"))
    set_rule(world.get_location("Spring Bonnie", player), lambda state: _fnaf_world_can_access_chara_area(state, player, "Pinwheel Funhouse"))

    # Requires "Key"
    set_rule(world.get_location("Dusting Fields: Laser Switch", player), lambda state: _fnaf_world_can_access(state, player, "Dusting Fields") and state.has("Key", player))
    set_rule(world.get_location("Fazbear Hills: Laser Switch", player), lambda state: state.has("Key", player))
    set_rule(world.get_location("Lilygear Lake: Laser Switch", player), lambda state: _fnaf_world_can_access(state, player, "Lilygear Lake") and state.has("Key", player))
    set_rule(world.get_location("Deep-Metal Mine: Laser Switch", player), lambda state: _fnaf_world_can_access(state, player, "Blacktomb Yard") and state.has("Key", player))

    for i in range(3):
        set_rule(world.get_location("Fazbear Hills: Fazcoin Chest " + str(i + 1), player), lambda state: True)
        set_rule(world.get_location("Choppy's Woods: Fazcoin Chest " + str(i + 1), player), lambda state: _fnaf_world_can_access(state, player, "Choppy's Woods"))
        set_rule(world.get_location("Dusting Fields: Fazcoin Chest " + str(i + 1), player), lambda state: _fnaf_world_can_access(state, player, "Dusting Fields"))
        set_rule(world.get_location("Lilygear Lake: Fazcoin Chest " + str(i + 1), player), lambda state: _fnaf_world_can_access(state, player, "Lilygear Lake"))
        set_rule(world.get_location("Mysterious Mine: Fazcoin Chest " + str(i + 1), player), lambda state: _fnaf_world_can_access(state, player, "Dusting Fields") or _fnaf_world_can_access(state, player, "Lilygear Lake"))
        set_rule(world.get_location("Blacktomb Yard: Fazcoin Chest " + str(i + 1), player), lambda state: _fnaf_world_can_access(state, player, "Blacktomb Yard"))
        set_rule(world.get_location("Deep-Metal Mine: Fazcoin Chest " + str(i + 1), player), lambda state: _fnaf_world_can_access(state, player, "Blacktomb Yard"))
        set_rule(world.get_location("Pinwheel Circus: Fazcoin Chest " + str(i + 1), player), lambda state: _fnaf_world_can_access(state, player, "Pinwheel Circus"))
        set_rule(world.get_location("Pinwheel Funhouse: Fazcoin Chest " + str(i + 1), player), lambda state: _fnaf_world_can_access(state, player, "Pinwheel Funhouse"))


# Sets rules on completion condition
def set_completion_rules(world: MultiWorld, player: int):
    completion_requirements = lambda state: True
    if world.worlds[player].options.ending_goal.current_key == "scott":
        completion_requirements = lambda state: _fnaf_world_can_access(state, player, "Pinwheel Circus")\
                                                and state.has("Laser Switch 1", player)\
                                                and state.has("Laser Switch 2", player)\
                                                and state.has("Laser Switch 3", player)\
                                                and state.has("Laser Switch 4", player)
    elif world.worlds[player].options.ending_goal.current_key == "clock":
        completion_requirements = lambda state: _fnaf_world_can_access(state, player, "Blacktomb Yard")\
                                                and _fnaf_world_can_access(state, player, "Dusting Fields")\
                                                and _fnaf_world_can_access(state, player, "Pinwheel Funhouse")\
                                                and state.has("Key", player)
    elif world.worlds[player].options.ending_goal.current_key == "fourth_glitch":
        completion_requirements = lambda state: _fnaf_world_can_access(state, player, "Pinwheel Funhouse")
    elif world.worlds[player].options.ending_goal.current_key == "universe_end":
        completion_requirements = lambda state: state.has("Fredbear", player)
    elif world.worlds[player].options.ending_goal.current_key == "chipper":
        completion_requirements = lambda state: _fnaf_world_can_access(state, player, "Lilygear Lake")\
                                                and state.has("Key", player)
    elif world.worlds[player].options.ending_goal.current_key == "magic_rainbow":
        completion_requirements = lambda state: True
    else:
        print(world.worlds[player].options.ending_goal.current_key)
        completion_requirements = lambda state: False

    world.completion_condition[player] = lambda state: completion_requirements(state)
