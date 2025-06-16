from worlds.generic.Rules import set_rule, add_rule
from BaseClasses import CollectionState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import DeltaruneWorld


# Sets rules on entrances and advancements that are always applied
def set_rules(world: "DeltaruneWorld"):
    player = world.player
    multiworld = world.multiworld
    set_rule(multiworld.get_entrance("CH1: Fields Entrance", player), lambda state: state.has("Fields Key", player))
    set_rule(multiworld.get_entrance("CH1: Forest Entrance", player), lambda state: state.has("Forest Key", player))
    set_rule(multiworld.get_entrance("CH1: Bake Sale Entrance", player), lambda state: state.has("Bake Sale Key", player))
    set_rule(multiworld.get_entrance("CH1: Card Castle Entrance", player), lambda state: state.has("Castle Key", player))
    set_rule(multiworld.get_entrance("CH1: Fields Warp", player), lambda state: state.has("Fields Warp", player))
    set_rule(multiworld.get_entrance("CH1: Forest Warp", player), lambda state: state.has("Forest Warp", player))
    set_rule(multiworld.get_entrance("CH1: Bake Sale Warp", player), lambda state: state.has("Bake Sale Warp", player))
    set_rule(multiworld.get_entrance("CH1: Castle Warp", player), lambda state: state.has("Castle Warp", player))
    set_rule(multiworld.get_entrance("CH1: Fields Warp Hub", player), lambda state: state.has("Fields Warp", player))
    set_rule(multiworld.get_entrance("CH1: Forest Warp Hub", player), lambda state: state.has("Forest Warp", player))
    set_rule(multiworld.get_entrance("CH1: Bake Sale Warp Hub", player), lambda state: state.has("Bake Sale Warp", player))
    set_rule(multiworld.get_entrance("CH1: Castle Warp Hub", player), lambda state: state.has("Castle Warp", player))
    set_rule(multiworld.get_location("CH1: Door Key", player),
            lambda state: state.can_reach("CH1: Card Castle", "Region", player) and state.has("Broken Key A", player) and state.has("Broken Key B", player) and state.has("Broken Key C", player))
    set_rule(multiworld.get_location("CH1: Top Cake", player), lambda state: state.has("BrokenCake", player))
    set_rule(multiworld.get_location("CH1: Return Top Cake", player), lambda state: state.has("Top Cake", player))
    set_rule(multiworld.get_location("CH1: Throw Away Manual", player), lambda state: state.has("Manual", player))
    set_rule(multiworld.get_location("CH1: JevilsTail", player), lambda state: state.has("Door Key", player))
    set_rule(multiworld.get_location("CH1: DevilsKnife", player), lambda state: state.has("Door Key", player))
    set_rule(multiworld.get_location("CH1: ShadowCrystal", player), lambda state: state.has("Door Key", player))
    set_rule(multiworld.get_location("CH1: Broken Key A", player), lambda state: state.can_reach("CH1: Card Castle", "Region", player))


# Sets rules on completion condition
def set_completion_rules(world: "DeltaruneWorld"):
    player = world.player
    multiworld = world.multiworld
    multiworld.completion_condition[player] = lambda state: state.can_reach("CH1: Card Castle", "Region", player) and state.has("King-Shaped Key Piece", player, state.count("King-Shaped Key Piece", player))
