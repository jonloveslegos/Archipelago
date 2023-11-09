from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, DeathLink, Range, Choice, PerGameCommonOptions

@dataclass
class ARNFOptions(PerGameCommonOptions):
    death_link: DeathLink
