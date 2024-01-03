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


class FNaFWRequireFindChar(Toggle):
    """Makes every character location require the Find Characters chip"""
    display_name = "Require Find Char"
    default = 1


class FNaFWProgressiveAnims(Toggle):
    """Makes you get animatronics in a randomized set order, but with stronger animatronics later in the order"""
    display_name = "Progressive Animatronics"
    default = 1


class FNaFWProgressiveBytes(Toggle):
    """Makes you get bytes in a randomized set order, but with stronger bytes later in the order"""
    display_name = "Progressive Bytes"
    default = 1


class FNaFWProgressiveChips(Toggle):
    """Makes you get chips in a randomized set order, but with stronger chips later in the order (Some chips may be excluded)"""
    display_name = "Progressive Chips"
    default = 1


class FNaFWVanillaLasers(Toggle):
    """Makes the laser switches always be found in their vanilla locations"""
    display_name = "Vanilla Lasers"
    default = 0


class FNaFWCheapEndo(Toggle):
    """Halves the price of the items in the Endo shop"""
    display_name = "Cheaper Endo Price"
    default = 1


class FNaFWVanillaPearl(Toggle):
    """Makes the pearl always be found in its vanilla location"""
    display_name = "Vanilla Pearl"
    default = 0


class FNaFWGoal(Choice):
    """Which ending do you want to be the goal."""
    display_name = "Ending Goal"
    option_scott = 0
    option_clock = 1
    option_fourth_glitch = 2
    option_universe_end = 3
    option_chipper = 4
    option_magic_rainbow = 5
    default = 0


FNaFW_options: typing.Dict[str, type(Option)] = {
    "ending_goal":                                  FNaFWGoal,
    "initial_characters":                           FNaFWInitialCharacters,
    "exclude_halloween":                            FNaFWVanillaHalloween,
    "vanilla_lasers":                               FNaFWVanillaLasers,
    "vanilla_pearl":                                FNaFWVanillaPearl,
    "hard_logic":                                   FNaFWHardLogic,
    "cheap_endo":                                   FNaFWCheapEndo,
    "require_find_char":                            FNaFWRequireFindChar,
    "progressive_anims":                            FNaFWProgressiveAnims,
    "progressive_bytes":                            FNaFWProgressiveBytes,
    "progressive_chips":                            FNaFWProgressiveChips,
}
