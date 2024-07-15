from Options import Range, Toggle, Choice, PerGameCommonOptions
from dataclasses import dataclass


class FNaFWVanillaHalloween(Toggle):
    """Makes the Halloween Town minigames give the vanilla stuff"""
    display_name = "Vanilla Halloween Town"
    default = 1


class FNaFWFazcoinChests(Range):
    """How many Fazcoin chests per area will be randomized"""
    display_name = "Randomized Fazcoin Chests"
    default = 1
    range_start = 1
    range_end = 3


class FNaFWInitialCharacters(Choice):
    """Decides your starting characters"""
    display_name = "Initial Characters"
    option_vanilla = 0
    option_limited_random = 1
    option_true_random = 2
    default = 1


class FNaFWHardLogic(Toggle):
    """Makes it possible to require grinding tokens or top layer at the start of the game"""
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


class FNaFWAreaWarping(Choice):
    """How do the warp buttons function?
    visit_area: You have to trigger the warp the same way as vanilla.
    always: You only need the item for that area to warp there.
    warp_item: Similar to always, but you need an additional item for warping."""
    display_name = "Warp Access"
    option_visit_area = 0
    option_always = 1
    option_warp_item = 2
    default = 0


@dataclass
class FNaFWOptions(PerGameCommonOptions):
    ending_goal:                                  FNaFWGoal
    initial_characters:                           FNaFWInitialCharacters
    vanilla_halloween:                            FNaFWVanillaHalloween
    vanilla_lasers:                               FNaFWVanillaLasers
    vanilla_pearl:                                FNaFWVanillaPearl
    hard_logic:                                   FNaFWHardLogic
    cheap_endo:                                   FNaFWCheapEndo
    require_find_char:                            FNaFWRequireFindChar
    progressive_anims:                            FNaFWProgressiveAnims
    progressive_bytes:                            FNaFWProgressiveBytes
    progressive_chips:                            FNaFWProgressiveChips
    area_warping:                                 FNaFWAreaWarping
    fazcoin_chests:                               FNaFWFazcoinChests

