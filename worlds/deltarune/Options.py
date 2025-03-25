from Options import Choice, Toggle, Range, PerGameCommonOptions
from dataclasses import dataclass


class StartingArea(Choice):
    """Which area to start with access to."""
    display_name = "Starting Area"
    option_ruins = 0
    option_snowdin = 1
    option_waterfall = 2
    option_hotland = 3
    option_core = 4
    default = 0


@dataclass
class DeltaruneOptions(PerGameCommonOptions):
    starting_area:                            StartingArea
