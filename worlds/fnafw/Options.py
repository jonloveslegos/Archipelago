import typing
from Options import Option, Range, Toggle, Choice


class VanillaHalloween(Toggle):
    """Makes the Halloween Town minigames give the vanilla stuff"""
    display_name = "Vanilla Halloween Town"
    default = 1


class InitialCharacters(Toggle):
    """Makes your starting characters be randomized"""
    display_name = "Randomize Initial Characters"
    default = 1


FNaFW_options: typing.Dict[str, type(Option)] = {
    "exclude_halloween":                           VanillaHalloween,
    "initial_characters":                          InitialCharacters,
}
