from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, DeathLink, Range, Choice, PerGameCommonOptions


class NormalModeIncluded(Choice):
    """Whether a playthrough of normal mode is included for this player.  Please note that approximately 35 non-progress items are in each run."""
    display_name = "Normal Mode Included"
    option_off = 0
    option_on = 1
    default = 1


class ClassicBossRushIncluded(Choice):
    """Whether a playthrough of Classic Boss Rush is included for this player.  Please note that 11 items are in each run."""
    display_name = "Classic Boss Rush Included"
    option_off = 0
    option_on = 1
    default = 1


@dataclass
class ARNFOptions(PerGameCommonOptions):
    normal_mode_included: NormalModeIncluded
    classic_boss_rush_included: ClassicBossRushIncluded
    death_link: DeathLink