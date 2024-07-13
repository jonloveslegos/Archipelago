from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, DeathLink, Range, Choice, PerGameCommonOptions


class GameMode(Choice):
    """The type of game mode that this player will be performing.
    Normal contains approximately 36 non-progression items, and 3 progression items.
    Classic Boss Rush (accessed via the Seeded Runs menu option, then under the Secrets menu on the left) contains 13 items.
    Exterminator contains 47 non-progression items and 3 progression items."""
    display_name = "Game Mode"
    option_normal = 1
    option_classic_boss_rush = 2
    option_exterminator = 4
    default = 1


class GrantAchievementsMode(Choice):
    """Select 'Necessary' to gain only the achievements needed to unlock included game modes.  Select 'All' to grant all achievements to any selected save slots."""
    display_name = "Grant Achievements"
    option_none = 0
    option_necessary = 1
    option_all = 2
    default = 1


class StartWithExplorb(Toggle):
    """Whether this player starts with an Explorb in all game modes.  This orb points out where items are hidden, making it easier for players unfamiliar with the hidden locations."""
    display_name = "Start With Explorb"
    default = 'true'


class StartWithWallJump(Toggle):
    """Whether this player starts with Wall Jump enabled in all game modes.  Normally, this is unlocked by sequence breaking once."""
    display_name = "Start With Wall Jump"
    default = 'true'


@dataclass
class ARNFOptions(PerGameCommonOptions):
    game_mode: GameMode
    grant_achievements_mode: GrantAchievementsMode
    start_with_explorb: StartWithExplorb
    start_with_wall_jump: StartWithWallJump
    death_link: DeathLink