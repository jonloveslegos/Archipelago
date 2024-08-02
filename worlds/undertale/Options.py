from Options import Choice, Toggle, Range, PerGameCommonOptions
from dataclasses import dataclass


class RouteRequired(Choice):
    """Main route of the game required to win."""
    display_name = "Required Route"
    option_neutral = 0
    option_pacifist = 1
    option_genocide = 2
    option_all_routes = 3
    default = 0


class RandomizeJump(Toggle):
    """Adds the ability to jump with the blue soul to the item pool."""
    display_name = "Randomize Blue Soul jump"
    default = 0


class StartingArea(Choice):
    """Which area to start with access to. (You will always have access to New Home.)"""
    display_name = "Starting Area"
    option_ruins = 0
    option_snowdin = 1
    option_waterfall = 2
    option_hotland = 3
    option_all = 4
    option_none = 5
    default = 0


class AllBosses(Toggle):
    """Requires beating all bosses to goal."""
    display_name = "Require All Bosses"
    default = 1


class IncludeTemy(Toggle):
    """Adds Temmy Armor to the item pool."""
    display_name = "Include Temy Armor"
    default = 1


class KeyPieces(Range):
    """How many required Key Pieces are added to the pool, only matters with Key Piece Hunt enabled."""
    display_name = "Key Piece Amount"
    default = 5
    range_start = 1
    range_end = 10


class ExtraKeyPieces(Range):
    """How many extra Key Pieces are added to the pool, only matters with Key Piece Hunt enabled."""
    display_name = "Extra Key Piece Amount"
    default = 0
    range_start = 0
    range_end = 10


class KeyHunt(Toggle):
    """Adds Key Pieces to the item pool, you need a specified amount of them to enter the last corridor."""
    display_name = "Key Piece Hunt"
    default = 0


class ProgressiveArmor(Toggle):
    """Makes the armor progressive."""
    display_name = "Progressive Armor"
    default = 0


class ProgressiveWeapons(Toggle):
    """Makes the weapons progressive."""
    display_name = "Progressive Weapons"
    default = 0


class OnlyFlakes(Toggle):
    """Replaces all non-required items, except equipment, with Temmie Flakes."""
    display_name = "Only Temmie Flakes"
    default = 0


class NoEquips(Toggle):
    """Removes all equippable items."""
    display_name = "No Equippables"
    default = 0


class RandomizeLove(Toggle):
    """Adds LOVE to the pool. Only matters if your goal includes Genocide route"""
    display_name = "Randomize LOVE"
    default = 0


class RandomizeStats(Toggle):
    """Makes each stat increase from LV a separate item. Only matters if your goal includes Genocide route
    Warning: This tends to spam chat with sending out checks."""
    display_name = "Randomize Stats"
    default = 0


class RandoBattleOptions(Toggle):
    """Turns the ITEM button in battle into an item you have to receive."""
    display_name = "Randomize Item Button"
    default = 0


class KillSanity(Toggle):
    """Makes every random encounter an item you need to receive to allow it to happen, also makes every kill from a random encounter a check. Only matters if your goal includes Genocide route"""
    display_name = "Kill Sanity"
    default = 0


class KillSanityPackSize(Range):
    """How many encounters do you unlock per item in Kill Sanity. Only matters if your goal includes Genocide route, and has Kill Sanity enabled
    Rounds down when you get a pack with more encounters than there are left to unlock in the area"""
    display_name = "Kill Sanity Pack Size"
    default = 5
    range_start = 1
    range_end = 40


class CutItems(Toggle):
    """Adds a chance of having cut items in the pool. (Rock Candy, Puppydough Icecream, etc)"""
    display_name = "Cut Items"
    default = 0


class IceTraps(Range):
    """Adds this many Ice Traps to the pool"""
    display_name = "Ice Trap Count"
    default = 0
    range_start = 0
    range_end = 10


class SpareSanity(Toggle):
    """Makes every spare from a random encounter a check, up to how many spare items you have for that area. Only matters if your goal includes the Pacifist or Neutral route"""
    display_name = "Spare Sanity"
    default = 0


class SpareSanityMaxSpares(Range):
    """How many spares you want to be checks in each area. Only matters if your goal includes the Pacifist or Neutral route, and has Spare Sanity enabled
    Warning: It is not recommended to set this to above 25, because there will be this many, times 4, locations that
    will be tedious to obtain. At maximum, that is 400 locations
    that are just for sparing."""
    display_name = "Spare Sanity Max Spares"
    default = 10
    range_start = 1
    range_end = 100


class SpareSanityPackSize(Range):
    """How many spare checks you want to unlock per item. Only matters if your goal includes the Pacifist or Neutral route, and has Spare Sanity enabled
    Rounds down when you get a pack with more spares than there are left to unlock in the area"""
    display_name = "Spare Sanity Pack Size"
    default = 2
    range_start = 2
    range_end = 100


class EntranceRando(Toggle):
    """Randomize the connections between scenes."""
    display_name = "Entrance Rando"


class Gifting(Toggle):
    """Allows gifting items to other players."""
    display_name = "Gifting"
    default = 0


@dataclass
class UndertaleOptions(PerGameCommonOptions):
    route_required:                           RouteRequired
    starting_area:                            StartingArea
    key_hunt:                                 KeyHunt
    key_pieces:                               KeyPieces
    extra_key_pieces:                         ExtraKeyPieces
    rando_item_button:                        RandoBattleOptions
    rando_jump:                               RandomizeJump
    rando_love:                               RandomizeLove
    rando_stats:                              RandomizeStats
    spare_sanity:                             SpareSanity
    spare_sanity_max:                         SpareSanityMaxSpares
    spare_sanity_pack_size:                   SpareSanityPackSize
    kill_sanity:                              KillSanity
    kill_sanity_pack_size:                    KillSanityPackSize
    temy_include:                             IncludeTemy
    cut_items:                                CutItems
    ice_traps:                                IceTraps
    prog_armor:                               ProgressiveArmor
    prog_weapons:                             ProgressiveWeapons
    no_equips:                                NoEquips
    only_flakes:                              OnlyFlakes
    gifting:                                  Gifting
    # entrance_rando:                           EntranceRando
