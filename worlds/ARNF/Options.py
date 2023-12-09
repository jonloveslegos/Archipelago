from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, DeathLink, Range, Choice, PerGameCommonOptions


class NormalIncluded(Toggle):
    """Whether a playthrough of normal mode is included for this player.  Please note that approximately 35 non-progress items are in each run."""
    display_name = "Normal Mode Included"
    default = 'true'


class ClassicBossRushIncluded(Toggle):
    """Whether a playthrough of Classic Boss Rush is included for this player.  Please note that 11 items are in each run."""
    display_name = "Classic Boss Rush Included"
    default = 'true'


@dataclass
class ARNFOptions(PerGameCommonOptions):
    normal_included: NormalIncluded
    classic_boss_rush_included: ClassicBossRushIncluded
    death_link: DeathLink