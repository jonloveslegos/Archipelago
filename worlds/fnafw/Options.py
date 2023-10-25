import typing
from Options import Option, Range, Toggle, Choice


class FNaFWVanillaHalloween(Toggle):
    """Makes the Halloween Town minigames give the vanilla stuff"""
    display_name = "Vanilla Halloween Town"
    default = 1


class FNaFWInitialCharacters(Toggle):
    """Makes your starting characters be randomized"""
    display_name = "Randomize Initial Characters"
    default = 1


class FNaFWHardLogic(Toggle):
    """Makes it possible to require grinding at the start of the game"""
    display_name = "Hard Logic"
    default = 0


class FNaFWProgressiveAnims(Toggle):
    """Makes you get animatronics in a randomized set order, but with stronger animatronics later in the order"""
    display_name = "Progressive Animatronics"
    default = 0


class FNaFWProgressiveBytes(Toggle):
    """Makes you get bytes in a randomized set order, but with stronger bytes later in the order"""
    display_name = "Progressive Bytes"
    default = 0


class FNaFWProgressiveChips(Toggle):
    """Makes you get chips in a randomized set order, but with stronger chips later in the order"""
    display_name = "Progressive Chips"
    default = 0


FNaFW_options: typing.Dict[str, type(Option)] = {
    "exclude_halloween":                            FNaFWVanillaHalloween,
    "initial_characters":                           FNaFWInitialCharacters,
    "hard_logic":                                   FNaFWHardLogic,
    "progressive_anims":                            FNaFWProgressiveAnims,
    "progressive_bytes":                            FNaFWProgressiveBytes,
    "progressive_chips":                            FNaFWProgressiveChips,
}
