import worlds.generic.Rules
from ..generic.Rules import set_rule, add_rule
from BaseClasses import MultiWorld
from ..AutoWorld import LogicMixin
from .Locations import advancement_table


class DustAETLogic(LogicMixin):
    pass


# Sets rules on entrances and advancements that are always applied
def set_rules(world: MultiWorld, player: int):
    set_rule(world.get_entrance("To Aurora Village from The Glade P2", player), lambda state: state.has("Dust Storm", player))
    set_rule(world.get_entrance("To The Glade P2 from The Glade P1", player), lambda state: state.has("Slash", player))
    set_rule(world.get_entrance("To The Sorrowing Meadow from Cirromon Caverns P2", player), lambda state: state.has("RedKey", player))
    set_rule(world.get_entrance("To Cirromon Caverns P2 from Cirromon Caverns P1", player), lambda state: state.has("Crouch Slide", player))
    set_rule(world.get_entrance("To Everdawn Basin from Blackmoor Mountains", player), lambda state: state.has("Iron Grip", player) and state.has("Double Jump", player) and state.has("Fire Projectile", player) and state.has("Lighting Projectile", player) and state.has("Boost Jump", player) and state.has("YellowKey", player))
    set_rule(world.get_entrance("To Blackmoor Mountains from The Sorrowing Meadow", player), lambda state: state.has("CoraQuest01", player) and state.has("CoraQuest02", player) and state.has("CoraQuest03", player) and state.has("CoraQuest04", player))
    for adv in advancement_table:
        if adv.__contains__("Chest"):
            set_rule(world.get_location(adv, player), lambda state: state.has_all("TreasureKey", player))


# Sets rules on completion condition
def set_completion_rules(world: MultiWorld, player: int):
    print(world.get_region("Everdawn Basin", player).entrances)
    world.completion_condition[player] = lambda state: state.can_reach(world.get_region("Everdawn Basin", player))
