from Options import Choice, Option, Toggle, DeathLink
import typing


class Goal(Choice):
    """The victory condition for your run. Stuff after the goal will not be shuffled."""

    display_name = "Goal"
    option_mechanical_bosses = 0
    option_plantera = 1
    option_golem = 2
    option_empress_of_light = 3
    option_lunatic_cultist = 4
    option_moon_lord = 5
    option_zenith = 6
    default = 0


class Achievements(Choice):
    """
    Adds checks upon collecting achievements. Achievements for clearing bosses and events are excluded.
    "Exclude Grindy" also excludes fishing achievements.
    """

    display_name = "Achievements"
    option_none = 0
    option_exclude_grindy = 1
    option_exclude_fishing = 2
    option_all = 3
    default = 1


class FightDifficulty(Choice):
    """
    Changes difficulty of fight requirements.
    """

    display_name = "Fight Difficulty"
    option_easy = 0
    option_medium = 1
    option_hard = 2
    option_insane = 3
    default = 0


class RandomizeCraftingStations(Toggle):
    """
    Makes you require items to use each crafting station.
    """

    display_name = "Randomize Crafting Stations"
    default = 0


class RandomizePickaxes(Toggle):
    """
    Makes you require items to use each tier of pickaxe.
    """

    display_name = "Randomize Pickaxes"
    default = 0


class RandomizeHammers(Toggle):
    """
    Makes you require items to use each tier of hammer.
    """

    display_name = "Randomize Hammers"
    default = 0


class RandomizeCrystals(Toggle):
    """
    Makes you require items to use any Life/Mana Crystals and Life Fruit.
    """

    display_name = "Randomize Crystals"
    default = 0


options: typing.Dict[str, type(Option)] = {  # type: ignore
    "goal": Goal,
    "achievements": Achievements,
    "death_link": DeathLink,
    "fight_difficulty": FightDifficulty,
    "randomize_crafting_stations": RandomizeCraftingStations,
    "randomize_pickaxes": RandomizePickaxes,
    "randomize_hammers": RandomizeHammers,
    "randomize_crystals": RandomizeCrystals,
}
