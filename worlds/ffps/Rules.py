from ..generic.Rules import set_rule
from BaseClasses import MultiWorld, CollectionState
from typing import TYPE_CHECKING
from .Locations import money_table

if TYPE_CHECKING:
    from . import FFPSWorld


def _ffps_can_get_points(state: CollectionState, player: int):
    return state.has_any(["Ladder Tower Decor", "Fruit Maze Decor", "Midnight Motorist Decor", "Ballpit Decor",
                          "Duck Pond Decor", "Deluxe Ballpit Decor", "Balloon Barrel Decor", "Candy Cadet Decor",
                          "Carnival Hoops Decor", "Roller Coaster Decor", "Ballpit Tower Decor", "Balloon Cart Decor",
                          "Gravity Vortex Decor", "Security Puppet Decor", "Lemonade Clown Decor", "Punch Clown Decor"],
                         player)


def _ffps_has_money(state: CollectionState, world: "FFPSWorld", mon: int, player: int):
    if not world.options.wallet_sanity:
        return _ffps_can_get_points(state, player)
    maximum = 25
    for i in range(state.count("Wallet Capacity Increase", player)):
        maximum = maximum * 2
    return maximum >= mon and _ffps_can_get_points(state, player)


def _ffps_can_spend_total(state: CollectionState, world: "FFPSWorld", mon: int, player: int):
    maximum = 0
    if _ffps_has_money(state, world, 30, player):
        maximum += 30 * 2
    if _ffps_has_money(state, world, 5, player):
        maximum += 5
    if _ffps_has_money(state, world, 25, player):
        maximum += 25
    if _ffps_has_money(state, world, 100, player):
        maximum += 100
    if _ffps_has_money(state, world, 45, player):
        maximum += 45
    if _ffps_has_money(state, world, 10, player):
        maximum += 10 * 4
    if _ffps_has_money(state, world, 15, player):
        maximum += 15
    if state.has("Catalogue 2 Unlock", player):
        if _ffps_has_money(state, world, 125, player):
            maximum += 125
        if _ffps_has_money(state, world, 250, player):
            maximum += 250
        if _ffps_has_money(state, world, 150, player):
            maximum += 150
        if _ffps_has_money(state, world, 170, player):
            maximum += 170
        if _ffps_has_money(state, world, 90, player):
            maximum += 90
        if _ffps_has_money(state, world, 200, player):
            maximum += 200
        if _ffps_has_money(state, world, 80, player):
            maximum += 80
        if _ffps_has_money(state, world, 310, player):
            maximum += 310
        if _ffps_has_money(state, world, 190, player):
            maximum += 190
        if _ffps_has_money(state, world, 260, player):
            maximum += 260
        if _ffps_has_money(state, world, 230, player):
            maximum += 230
    if state.has("Catalogue 3 Unlock", player):
        if _ffps_has_money(state, world, 1000, player):
            maximum += 500
        if _ffps_has_money(state, world, 810, player):
            maximum += 810
        if _ffps_has_money(state, world, 750, player):
            maximum += 750
        if _ffps_has_money(state, world, 900, player):
            maximum += 900
        if _ffps_has_money(state, world, 550, player):
            maximum += 550
        if _ffps_has_money(state, world, 450, player):
            maximum += 450
        if _ffps_has_money(state, world, 390, player):
            maximum += 390
        if _ffps_has_money(state, world, 490, player):
            maximum += 490
        if _ffps_has_money(state, world, 1000, player):
            maximum += 1000
        if _ffps_has_money(state, world, 600, player):
            maximum += 600
        if _ffps_has_money(state, world, 1200, player):
            maximum += 1200
        if _ffps_has_money(state, world, 2000, player):
            maximum += 2000 * 3
        if _ffps_has_money(state, world, 2500, player):
            maximum += 2500
    if state.has("Catalogue 4 Unlock", player):
        if _ffps_has_money(state, world, 3500, player):
            maximum += 3500
        if _ffps_has_money(state, world, 5000, player):
            maximum += 5000
        if _ffps_has_money(state, world, 4400, player):
            maximum += 4400
        if _ffps_has_money(state, world, 3900, player):
            maximum += 3900
        if _ffps_has_money(state, world, 6000, player):
            maximum += 6000
        if _ffps_has_money(state, world, 3100, player):
            maximum += 3100
        if _ffps_has_money(state, world, 9000, player):
            maximum += 9000
        if _ffps_has_money(state, world, 7770, player):
            maximum += 7770
        if _ffps_has_money(state, world, 12500, player):
            maximum += 12500
        if _ffps_has_money(state, world, 5, player):
            maximum += 5
        if _ffps_has_money(state, world, 4100, player):
            maximum += 4100
        if _ffps_has_money(state, world, 19000, player):
            maximum += 19000
        if _ffps_has_money(state, world, 32000, player):
            maximum += 32000
        if _ffps_has_money(state, world, 71000, player):
            maximum += 71000
        if _ffps_has_money(state, world, 15, player) and state.has("Funtime Chica Animatronic", player) \
                and state.has("Music Man Animatronic", player) and state.has("El Chip Animatronic", player) \
                and state.has("Stage Upgrade", player, 4):
            maximum += 15
    return maximum >= mon and _ffps_can_get_points(state, player)


# Sets rules on entrances and advancements that are always applied
def set_rules(myWorld: "FFPSWorld", player: int):
    world = myWorld.multiworld
    set_rule(world.get_location("Buy Ballpit Decor", player),
             lambda state: _ffps_has_money(state, myWorld, 30, player))
    set_rule(world.get_location("Buy Cups Upgrade 1", player),
             lambda state: _ffps_has_money(state, myWorld, 5, player))
    set_rule(world.get_location("Buy Cups Upgrade 2", player),
             lambda state: _ffps_has_money(state, myWorld, 20, player))
    set_rule(world.get_location("Buy Stage Upgrade 1", player),
             lambda state: _ffps_has_money(state, myWorld, 25, player))
    set_rule(world.get_location("Buy Stage Upgrade 2", player),
             lambda state: _ffps_has_money(state, myWorld, 75, player))
    set_rule(world.get_location("Buy Sanitation Station Decor", player),
             lambda state: _ffps_has_money(state, myWorld, 100, player))
    set_rule(world.get_location("Buy Discount Cooling Unit Decor", player),
             lambda state: _ffps_has_money(state, myWorld, 25, player))
    set_rule(world.get_location("Buy Duck Pond Decor", player),
             lambda state: _ffps_has_money(state, myWorld, 45, player))
    set_rule(world.get_location("Buy Paper Pals Decor", player),
             lambda state: _ffps_has_money(state, myWorld, 5, player))
    set_rule(world.get_location("Buy Bucket Bob Animatronic", player),
             lambda state: _ffps_has_money(state, myWorld, 25, player))
    set_rule(world.get_location("Buy Mr Can Do Animatronic", player),
             lambda state: _ffps_has_money(state, myWorld, 25, player))
    set_rule(world.get_location("Buy Mr Hugs Animatronic", player),
             lambda state: _ffps_has_money(state, myWorld, 25, player))
    set_rule(world.get_location("Buy No. 1 Crate Animatronic", player),
             lambda state: _ffps_has_money(state, myWorld, 25, player))
    set_rule(world.get_location("Buy Pan Stan Animatronic", player),
             lambda state: _ffps_has_money(state, myWorld, 25, player))
    set_rule(world.get_location("Buy Fruit Maze Decor", player),
             lambda state: state.has("Catalogue 2 Unlock", player) and _ffps_has_money(state, myWorld, 150, player))
    set_rule(world.get_location("Buy Midnight Motorist Decor", player),
             lambda state: state.has("Catalogue 2 Unlock", player) and _ffps_has_money(state, myWorld, 170, player))
    set_rule(world.get_location("Buy Gumball Machine Decor", player),
             lambda state: state.has("Catalogue 2 Unlock", player) and _ffps_has_money(state, myWorld, 125, player))
    set_rule(world.get_location("Buy Stage Light Decor", player),
             lambda state: state.has("Catalogue 2 Unlock", player) and _ffps_has_money(state, myWorld, 90, player))
    set_rule(world.get_location("Buy Traffic Light Decor", player),
             lambda state: state.has("Catalogue 2 Unlock", player) and _ffps_has_money(state, myWorld, 80, player))
    set_rule(world.get_location("Buy Happy Frog Animatronic", player),
             lambda state: state.has("Catalogue 2 Unlock", player) and _ffps_has_money(state, myWorld, 200, player))
    set_rule(world.get_location("Buy Mr Hippo Animatronic", player),
             lambda state: state.has("Catalogue 2 Unlock", player) and _ffps_has_money(state, myWorld, 190, player))
    set_rule(world.get_location("Buy Nedd Bear Animatronic", player),
             lambda state: state.has("Catalogue 2 Unlock", player) and _ffps_has_money(state, myWorld, 260, player))
    set_rule(world.get_location("Buy Pig Patch Animatronic", player),
             lambda state: state.has("Catalogue 2 Unlock", player) and _ffps_has_money(state, myWorld, 230, player))
    set_rule(world.get_location("Buy Candy Cadet Decor", player),
             lambda state: state.has("Catalogue 2 Unlock", player) and _ffps_has_money(state, myWorld, 310, player))
    set_rule(world.get_location("Buy Stage Upgrade 3", player),
             lambda state: (state.has("Catalogue 2 Unlock", player) and _ffps_has_money(state, myWorld, 110, player)) or (state.has("Catalogue 3 Unlock", player) and _ffps_has_money(state, myWorld, 810, player)))
    set_rule(world.get_location("Buy Stage Upgrade 4", player),
             lambda state: (state.has("Catalogue 2 Unlock", player) and _ffps_has_money(state, myWorld, 200, player)) or (state.has("Catalogue 3 Unlock", player) and _ffps_has_money(state, myWorld, 810, player)))
    set_rule(world.get_location("Buy Cups Upgrade 3", player),
             lambda state: (state.has("Catalogue 2 Unlock", player) and _ffps_has_money(state, myWorld, 50, player))
             or state.has("Catalogue 4 Unlock", player) and _ffps_has_money(state, myWorld, 3100, player))
    set_rule(world.get_location("Buy Speaker Upgrade 1", player),
             lambda state: state.has("Catalogue 2 Unlock", player) and _ffps_has_money(state, myWorld, 125, player))
    set_rule(world.get_location("Buy Speaker Upgrade 2", player),
             lambda state: state.has("Catalogue 2 Unlock", player) and _ffps_has_money(state, myWorld, 250, player))
    set_rule(world.get_location("Buy Side Stage Upgrade", player),
             lambda state: state.has("Catalogue 3 Unlock", player) and _ffps_has_money(state, myWorld, 1000, player))
    set_rule(world.get_location("Buy Ballpit Tower Decor", player),
             lambda state: state.has("Catalogue 3 Unlock", player) and _ffps_has_money(state, myWorld, 750, player))
    set_rule(world.get_location("Buy Ladder Tower Decor", player),
             lambda state: state.has("Catalogue 3 Unlock", player) and _ffps_has_money(state, myWorld, 900, player))
    set_rule(world.get_location("Buy Carnival Hoops Decor", player),
             lambda state: state.has("Catalogue 3 Unlock", player) and _ffps_has_money(state, myWorld, 550, player))
    set_rule(world.get_location("Buy Roller Coaster Decor", player),
             lambda state: state.has("Catalogue 3 Unlock", player) and _ffps_has_money(state, myWorld, 450, player))
    set_rule(world.get_location("Buy Lemonade Clown Decor", player),
             lambda state: state.has("Catalogue 3 Unlock", player) and _ffps_has_money(state, myWorld, 390, player))
    set_rule(world.get_location("Buy Punch Clown Decor", player),
             lambda state: state.has("Catalogue 3 Unlock", player) and _ffps_has_money(state, myWorld, 490, player))
    set_rule(world.get_location("Buy Jukebox Decor", player),
             lambda state: state.has("Catalogue 3 Unlock", player) and _ffps_has_money(state, myWorld, 1000, player))
    set_rule(world.get_location("Buy Medical Station Decor", player),
             lambda state: state.has("Catalogue 3 Unlock", player) and _ffps_has_money(state, myWorld, 600, player))
    set_rule(world.get_location("Buy Security Door Decor", player),
             lambda state: state.has("Catalogue 3 Unlock", player) and _ffps_has_money(state, myWorld, 1200, player))
    set_rule(world.get_location("Buy Rockstar Freddy Animatronic", player),
             lambda state: state.has("Catalogue 3 Unlock", player) and _ffps_has_money(state, myWorld, 2000, player))
    set_rule(world.get_location("Buy Rockstar Bonnie Animatronic", player),
             lambda state: state.has("Catalogue 3 Unlock", player) and _ffps_has_money(state, myWorld, 2000, player))
    set_rule(world.get_location("Buy Rockstar Chica Animatronic", player),
             lambda state: state.has("Catalogue 3 Unlock", player) and _ffps_has_money(state, myWorld, 2000, player))
    set_rule(world.get_location("Buy Rockstar Foxy Animatronic", player),
             lambda state: state.has("Catalogue 3 Unlock", player) and _ffps_has_money(state, myWorld, 2500, player))
    set_rule(world.get_location("Buy Stage Upgrade 5", player),
             lambda state: state.has("Catalogue 3 Unlock", player) and _ffps_has_money(state, myWorld, 810, player))
    set_rule(world.get_location("Buy Balloon Cart Decor", player),
             lambda state: state.has("Catalogue 4 Unlock", player) and _ffps_has_money(state, myWorld, 3500, player))
    set_rule(world.get_location("Buy Confetti Floor", player),
             lambda state: state.has("Catalogue 4 Unlock", player) and _ffps_has_money(state, myWorld, 5000, player))
    set_rule(world.get_location("Buy Deluxe Ballpit Decor", player),
             lambda state: state.has("Catalogue 4 Unlock", player) and _ffps_has_money(state, myWorld, 4400, player))
    set_rule(world.get_location("Buy Pizza Light Decor", player),
             lambda state: state.has("Catalogue 4 Unlock", player) and _ffps_has_money(state, myWorld, 3900, player))
    set_rule(world.get_location("Buy Data Archive Decor", player),
             lambda state: state.has("Catalogue 4 Unlock", player) and _ffps_has_money(state, myWorld, 6000, player))
    set_rule(world.get_location("Buy Gravity Vortex Decor", player),
             lambda state: state.has("Catalogue 4 Unlock", player) and _ffps_has_money(state, myWorld, 9000, player))
    set_rule(world.get_location("Buy Orville Elephant Animatronic", player),
             lambda state: state.has("Catalogue 4 Unlock", player) and _ffps_has_money(state, myWorld, 4100, player))
    set_rule(world.get_location("Buy Prize King Decor", player),
             lambda state: state.has("Catalogue 4 Unlock", player) and _ffps_has_money(state, myWorld, 7770, player))
    set_rule(world.get_location("Buy Security Puppet Decor", player),
             lambda state: state.has("Catalogue 4 Unlock", player) and _ffps_has_money(state, myWorld, 12500, player))
    set_rule(world.get_location("Buy Lefty Animatronic", player),
             lambda state: state.has("Catalogue 4 Unlock", player) and _ffps_has_money(state, myWorld, 5, player))
    set_rule(world.get_location("Buy Music Man Animatronic", player),
             lambda state: state.has("Catalogue 4 Unlock", player) and _ffps_has_money(state, myWorld, 19000, player))
    set_rule(world.get_location("Buy El Chip Animatronic", player),
             lambda state: state.has("Catalogue 4 Unlock", player) and _ffps_has_money(state, myWorld, 32000, player))
    set_rule(world.get_location("Buy Funtime Chica Animatronic", player),
             lambda state: state.has("Catalogue 4 Unlock", player) and _ffps_has_money(state, myWorld, 71000, player))
    set_rule(world.get_location("Buy Pickles Decor", player),
             lambda state: state.has("Catalogue 4 Unlock", player) and state.has("Funtime Chica Animatronic", player)
                           and state.has("Music Man Animatronic", player) and state.has("El Chip Animatronic", player)
                           and state.has("Stage Upgrade", player, 4) and _ffps_has_money(state, myWorld, 15, player))
    set_rule(world.get_location("Buy Cups Upgrade 4", player),
             lambda state: state.has("Catalogue 4 Unlock", player) and _ffps_has_money(state, myWorld, 3100, player))
    for itm in money_table:
        set_rule(world.get_location("Obtained "+str(itm.amount)+" Points", player),
                 lambda state: _ffps_can_get_points(state, player))
    set_rule(world.get_location("Unlocked Catalogue 2", player),
             lambda state: _ffps_can_spend_total(state, myWorld, 100, player))
    set_rule(world.get_location("Unlocked Catalogue 3", player),
             lambda state: _ffps_can_spend_total(state, myWorld, 1000, player) and state.has("Catalogue 2 Unlock", player))
    set_rule(world.get_location("Unlocked Catalogue 4", player),
             lambda state: _ffps_can_spend_total(state, myWorld, 3000, player) and state.has("Catalogue 3 Unlock", player))
    set_rule(world.get_location("Salvage Molten Freddy", player),
             lambda state: True)
    set_rule(world.get_location("Salvage ScrapTrap", player),
             lambda state: state.has("Tuesday Unlock", player))
    set_rule(world.get_location("Salvage Scrap Baby", player),
             lambda state: state.has("Wednesday Unlock", player))
    set_rule(world.get_location("Salvage Lefty", player),
             lambda state: state.has("Thursday Unlock", player))
    set_rule(world.get_location("Bought Printer Upgrade", player),
             lambda state: _ffps_has_money(state, myWorld, 500, player))
    set_rule(world.get_location("Bought Handyman Upgrade", player),
             lambda state: _ffps_has_money(state, myWorld, 900, player))
    set_rule(world.get_location("Bought Internet Upgrade", player),
             lambda state: _ffps_has_money(state, myWorld, 500, player))
    set_rule(world.get_location("Buy Balloon Barrel Decor", player),
             lambda state: _ffps_has_money(state, myWorld, 30, player))


# Sets rules on completion condition
def set_completion_rules(world: MultiWorld, player: int):
    completion_requirements = lambda state: \
        state.has("ScrapTrap", player) and \
        state.has("Scrap Baby", player) and \
        state.has("Lefty", player) and \
        state.has("Molten Freddy", player) and \
        state.has("Saturday Unlock", player)
    world.completion_condition[player] = lambda state: completion_requirements(state)
