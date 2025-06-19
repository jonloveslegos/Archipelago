from Options import Choice, Toggle, Range, PerGameCommonOptions
from dataclasses import dataclass


class Notice(Choice):
    """THIS IS NOT AN OPTION:
    Be aware that if there are too many items in the pool, it will remove random filler items!
    So be mindful of that when deciding your options."""
    display_name = "NOTICE: READ OPTION INFO"
    option_understood = 0
    default = 0


class RandomizeSuperBosses(Toggle):
    """Randomizes all rewards for beating Super Bosses."""
    display_name = "Randomize Super Bosses"
    default = 0


class RandomizeWarpDoors(Toggle):
    """Turns unlocking warp doors into items.
    (Logic expects you to first get warp access both to and from the destination.)
    (Also be aware that when choosing a destination, you can choose a blank option to back out of the menu.)"""
    display_name = "Randomize Warp Doors"
    default = 0


class IncludeChapter1(Toggle):
    """Do you want to play Chapter 1?"""
    display_name = "Include Chapter 1"
    default = 1


class IncludeChapter2(Toggle):
    """Do you want to play Chapter 2?"""
    display_name = "Include Chapter 2"
    default = 0


class GoalMacGuffinAmount(Range):
    """How many MacGuffin items are needed for the goal.
    (Chapter 1: King-Shaped Key Piece)"""
    display_name = "Randomize Warp Doors"
    default = 3
    range_start = 1
    range_end = 10


@dataclass
class DeltaruneOptions(PerGameCommonOptions):
    notice_read_option_info:                          Notice
    include_chapter_1:                                IncludeChapter1
    include_chapter_2:                                IncludeChapter2
    goal_macguffin_amount:                            GoalMacGuffinAmount
    randomize_warp_doors:                             RandomizeWarpDoors
    randomize_super_bosses:                           RandomizeSuperBosses
