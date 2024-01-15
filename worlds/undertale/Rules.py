from BaseClasses import CollectionState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import UndertaleWorld


def _undertale_is_route(world: "UndertaleWorld", route: int):
    if route == 3:
        return world.options.route_required.current_key == "all_routes"
    if world.options.route_required.current_key == "all_routes":
        return True
    if route == 0:
        return world.options.route_required.current_key == "neutral"
    if route == 1:
        return world.options.route_required.current_key == "pacifist"
    if route == 2:
        return world.options.route_required.current_key == "genocide"
    return False


def _undertale_has_keys(state: CollectionState, world: "UndertaleWorld", player: int):
    return ((state.has("Left Home Key", player) and state.has("Right Home Key", player)) or
            state.has("Key Piece", player, world.options.key_pieces.value))


def _undertale_exp_available(state: CollectionState, world: "UndertaleWorld", player: int):
    exp = 0
    pack_size = world.options.kill_sanity_pack_size.value
    if state.can_reach("Ruins Grind Rooms", "Region", player):
        exp += (min(20, state.count("Ruins Population Pack", player) * pack_size) * 2)
        if state.can_reach("room_basement4", "Region", player) and state.count("Ruins Population Pack", player) * \
                pack_size >= 20:
            exp += 150
    if state.can_reach("Snowdin Grind Rooms", "Region", player):
        exp += (min(15, state.count("Snowdin Population Pack", player) * pack_size) * 1)
        exp += 170
        if state.can_reach("room_fogroom", "Region", player) and state.count("Snowdin Population Pack", player) * \
                pack_size >= 16:
            exp += 222
    if state.can_reach("Waterfall Grind Rooms", "Region", player):
        exp += (min(18, state.count("Waterfall Population Pack", player) * pack_size) * 3)
        exp += 52
        if state.can_reach("room_water20", "Region", player) and state.count("Waterfall Population Pack", player) * \
                pack_size >= 18:
            exp += 1500
    if state.can_reach("room_fire_turn", "Region", player):
        exp += 220
    if state.can_reach("room_fire_spider", "Region", player):
        exp += 300
    if state.can_reach("Hotland/Core Grind Rooms", "Region", player):
        exp += (min(40, state.count("Hotland Population Pack", player) * pack_size) * 70)
        if state.can_reach("room_fire_core_metttest", "Region", player) and \
                state.count("Hotland Population Pack", player) * pack_size >= 40:
            exp = 50000
    if state.can_reach("room_castle_finalshoehorn", "Region", player):
        exp = 99999
    return exp


def _undertale_return_reachable_level(exp: int):
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
