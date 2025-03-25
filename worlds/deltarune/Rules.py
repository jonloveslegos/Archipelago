from worlds.generic.Rules import set_rule, add_rule
from BaseClasses import CollectionState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import DeltaruneWorld


# Sets rules on entrances and advancements that are always applied
def set_rules(world: "DeltaruneWorld"):
    player = world.player
    multiworld = world.multiworld


# Sets rules on completion condition
def set_completion_rules(world: "DeltaruneWorld"):
    player = world.player
    multiworld = world.multiworld
    multiworld.completion_condition[player] = lambda state: state.can_reach("Barrier", "Region", player)
