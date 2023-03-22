from typing import TYPE_CHECKING

from ..generic.Rules import add_rule

if TYPE_CHECKING:
    from . import KHDaysWorld

def set_rules(khdays_world: "KHDaysWorld"):
    player = khdays_world.player
    world = khdays_world.multiworld