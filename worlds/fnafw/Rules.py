from ..generic.Rules import set_rule
from BaseClasses import MultiWorld


# Sets rules on entrances and advancements that are always applied
def set_rules(world: MultiWorld, player: int):
    pass


# Sets rules on completion condition
def set_completion_rules(world: MultiWorld, player: int):
    completion_requirements = lambda state: True
    world.completion_condition[player] = lambda state: completion_requirements(state)
