from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, DeathLink, Range, Choice, PerGameCommonOptions


class NormalIncluded(Toggle):
    """Whether a playthrough of normal mode is included for this player.  Please note that approximately 32 minor items and 4 non-progress major items are in each run."""
    display_name = "Normal Mode Included"
    default = 'true'


class ClassicBossRushIncluded(Toggle):
    """Whether a playthrough of Classic Boss Rush is included for this player.  Please note that 13 items are in each run."""
    display_name = "Classic Boss Rush Included"
    default = 'false'


class StartWithExplorb(Toggle):
    """Whether this player starts with an Explorb in all game modes.  This orb points out where items are hidden, making it easier for players unfamiliar with the hidden locations."""
    display_name = "Start With Explorb"
    default = 'true'

@dataclass
class ARNFOptions(PerGameCommonOptions):
    normal_included: NormalIncluded
    classic_boss_rush_included: ClassicBossRushIncluded
    start_with_explorb: StartWithExplorb
    death_link: DeathLink