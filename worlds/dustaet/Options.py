import typing
from Options import Option, Toggle


class RandomizeStartingAbilities(Toggle):
    """Randomizes the ability to attack and jump."""
    display_name = "Randomize Starting Abilities"


class RandomizeFidget(Toggle):
    """Randomizes the ability to use Fidget's basic projectile."""
    display_name = "Randomize Fidget"


dustaet_options: typing.Dict[str, type(Option)] = {
    "randomize_starting_abilities":         RandomizeStartingAbilities,
    "randomize_fidget":                     RandomizeFidget,
}
