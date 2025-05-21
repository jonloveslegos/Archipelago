from Options import Toggle, PerGameCommonOptions
from dataclasses import dataclass


class RandomizeStartingAbilities(Toggle):
    """Randomizes the ability to attack and jump."""
    display_name = "Randomize Starting Abilities"


class RandomizeFidget(Toggle):
    """Randomizes the ability to use Fidget's basic projectile."""
    display_name = "Randomize Fidget"


class RandomizeSkillGems(Toggle):
    """Randomizes the skill gems you get each level."""
    display_name = "Randomize Skill Gems"


@dataclass
class DustAETOptions(PerGameCommonOptions):
    randomize_starting_abilities:         RandomizeStartingAbilities
    randomize_fidget:                     RandomizeFidget
    randomize_skill_gems:                 RandomizeSkillGems

