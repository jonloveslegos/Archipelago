import typing
from dataclasses import dataclass
from Options import Option, Range, Choice, Toggle, PerGameCommonOptions


class StartingCharacter(Choice):
    """What character you have unlocked from the start"""
    option_Roxas = 0
    option_Axel = 1
    option_Xigbar = 2
    option_Saix = 3
    option_Xaldin = 4
    option_Sora = 5
    option_Demyx = 6
    option_Larxene = 7
    option_Lexaeus = 8
    option_Luxord = 9
    option_Marluxia = 10
    option_Riku = 11
    option_Vexen = 12
    option_Xemnas = 13
    option_Xion = 14
    option_Zexion = 15
    option_Mickey = 16
    option_Donald = 17
    option_Goofy = 18
    option_Dual_Wield_Roxas = 19
    default = 0


class ShardRequirement(Range):
    """How many Memory Shards do you need to do the final day?"""
    range_start = 1
    range_end = 10
    default = 5


class RandomizeEmblems(Toggle):
    """Randomize Unity Badges, Ordeal Emblems, and Ordeal Blazons. Does not add corresponding items."""
    default = 0


class RandomizeSynthesis(Toggle):
    """Randomize synthesized items."""
    default = 0


class RandomizeLevelRewards(Toggle):
    """Randomize level-up rewards."""
    default = 1


class RandomizeHubGifts(Toggle):
    """Randomize gifted items in the hub."""
    default = 0


@dataclass
class KHDaysOptions(PerGameCommonOptions):
    ShardRequirement: ShardRequirement
    StartingCharacter: StartingCharacter
    RandomizeEmblems: RandomizeEmblems
    RandomizeSynthesis: RandomizeSynthesis
    RandomizeLevelRewards: RandomizeLevelRewards
    RandomizeHubGifts: RandomizeHubGifts
