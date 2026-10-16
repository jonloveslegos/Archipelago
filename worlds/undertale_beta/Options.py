from Options import Choice, Toggle, Range, PerGameCommonOptions, OptionSet, NamedRange
from dataclasses import dataclass
from .er_data import door_name_list


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


class BonusLocations(Toggle):
    """Choose to have extra locations as chests at various dead ends across the game."""
    display_name = "Extra locations"
    default = 1


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


class GuaranteedFiller(Range):
    """Guarantee this amount of filler items."""
    display_name = "Guaranteed Filler Amount"
    default = 5
    range_start = 0
    range_end = 20


class HubShopCost(Range):
    """How much each location in the Hub shop costs.
    The Hub shop will be given locations only if there are too little locations elsewhere to put everything."""
    display_name = "Hub Shop Cost"
    default = 250
    range_start = 0
    range_end = 1000


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
    """Makes each LOVE increase a separate item and location. Only matters if your goal includes Genocide route"""
    display_name = "Randomize LOVE"
    default = 0


class RandomizeStats(Toggle):
    """Makes each stat increase from EXP a separate item and location. Only matters if your goal includes Genocide route
    Warning: This tends to spam chat with sending out checks."""
    display_name = "Randomize Stats"
    default = 0


class RandoBattleOptions(Toggle):
    """Turns the ITEM button in battle into an item you have to receive."""
    display_name = "Randomize Item Button"
    default = 0


class KillSanity(Choice):
    """Only matters if your goal includes Genocide route. Randomizes Kills, and optionally locks encounters behind receiving Population Packs
    Off: Fully disabled
    Unlocked: Makes every random encounter kill a location
    Locked: Makes every random encounter kill a location, and requires you to receive Population Packs for the area to be able to encounter enemies"""
    display_name = "Kill Sanity"
    option_off = 0
    option_unlocked = 1
    option_locked = 2
    default = 0


class KillSanityPackSize(Range):
    """How many encounters do you unlock per item in Kill Sanity. Only matters if your goal includes Genocide route, and has Kill Sanity on Locked
    Rounds down when you get a pack with more encounters than there are left to unlock in the area"""
    display_name = "Kill Sanity Pack Size"
    default = 5
    range_start = 1
    range_end = 40


class LoveReductionTraps(Range):
    """Adds this many Love Reduction Traps to the pool. Only matters if your goal includes Genocide route, and has Randomize LOVE enabled
    Permenantly reduces your current LOVE by 1 (Max HP and ATK cannot be lowered below 1, and the Stat Menu displays ATK and DEF as 10 lower than it actually is)
    Warning: High values tend to cause many Hub Shop locations to be added to fit all of the items"""
    display_name = "LOVE Reduction Traps"
    default = 0
    range_start = 0
    range_end = 56


class MaxHPReductionTraps(Range):
    """Adds this many Max HP Reduction Traps to the pool. Only matters if your goal includes Genocide route, and has Randomize Stats enabled
    Permenantly reduces your current Max HP by 4 (Minimum of 1)
    Warning: High values tend to cause many Hub Shop locations to be added to fit all of the items"""
    display_name = "Max HP Reduction Traps"
    default = 0
    range_start = 0
    range_end = 24


class ATKReductionTraps(Range):
    """Adds this many ATK Reduction Traps to the pool. Only matters if your goal includes Genocide route, and has Randomize Stats enabled
    Permenantly reduces your current ATK by 2 (Minimum of 1, and is display as 10 lower in the Stat Menu)
    Warning: High values tend to cause many Hub Shop locations to be added to fit all of the items"""
    display_name = "ATK Reduction Traps"
    default = 0
    range_start = 0
    range_end = 24


class DEFReductionTraps(Range):
    """Adds this many DEF Reduction Traps to the pool. Only matters if your goal includes Genocide route, and has Randomize Stats enabled
    Permenantly reduces your current DEF by 1 (No minimum, and is display as 10 lower in the Stat Menu)
    Warning: High values tend to cause many Hub Shop locations to be added to fit all of the items"""
    display_name = "DEF Reduction Traps"
    default = 0
    range_start = 0
    range_end = 15


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
    range_start = 1
    range_end = 100


class EntranceRando(Toggle):
    """Randomize the connections between scenes."""
    display_name = "Entrance Rando"


class Gifting(Toggle):
    """Allows gifting items to other players."""
    display_name = "Gifting"
    default = 0


class SpellsEnabled(OptionSet):
    """Adds the selected Spell types to the pool.
    Valid keys: 
    attack: Spells that deal direct damage to the opponent. (2 total)
    pacifist: Spells that are only useful for sparing the opponent. (1 total)
    violent: Spells that are only useful for damaging the opponent, but do not do so directly. (1 total)
    heal: Spells that heal the player. (3 total)
    gimmick: Spells that don't easily fit into any category, and are usually very different from other spells. (1 total)"""
    display_name = "Spell List"
    default = ["attack", "pacifist", "violent", "heal", "gimmick"]
    valid_keys = frozenset(["attack", "pacifist", "violent", "heal", "gimmick"])


class AddDoorLocks(NamedRange):
    """Amount of random transitions to add locks to that require an item to open.
    The doors at the hub will never be locked
    Adds one location at each locked transition as well, approach the transition to obtain the location, can still be obtained even after unlocking it.
    If the current room has a locked transition, you can press W to warp to the hub, to prevent you from being softlocked inside a one-way room.
    Genocide route goal lowers the possible maximum to 192."""
    
    display_name = "Door Locks Added"
    default = 0
    range_start = 0
    range_end = 206
    special_range_names = {
        "maximum": range_end,
    }


class MandatoryDoorLocks(OptionSet):
    """Requires the chosen Door Locks to exist, these are in addition to the Door Lock amount"""
    display_name = "Mandatory Door Locks"
    default = []
    valid_keys = frozenset(door_name_list.copy())


class ExcludedDoorLocks(OptionSet):
    """Prevents the chosen Door Locks from existing"""
    display_name = "Excluded Door Locks"
    default = []
    valid_keys = frozenset(door_name_list.copy())


@dataclass
class UndertaleOptions(PerGameCommonOptions):
    route_required:                           RouteRequired
    starting_area:                            StartingArea
    bonus_locations:                          BonusLocations
    guaranteed_filler:                        GuaranteedFiller
    hub_shop_cost:                            HubShopCost
    key_hunt:                                 KeyHunt
    key_pieces:                               KeyPieces
    extra_key_pieces:                         ExtraKeyPieces
    rando_item_button:                        RandoBattleOptions
    rando_jump:                               RandomizeJump
    rando_love:                               RandomizeLove
    rando_stats:                              RandomizeStats
    enabled_spells:                           SpellsEnabled
    spare_sanity:                             SpareSanity
    spare_sanity_max:                         SpareSanityMaxSpares
    spare_sanity_pack_size:                   SpareSanityPackSize
    kill_sanity:                              KillSanity
    kill_sanity_pack_size:                    KillSanityPackSize
    door_locks:                               AddDoorLocks
    mandatory_door_locks:                     MandatoryDoorLocks
    excluded_door_locks:                      ExcludedDoorLocks
    prog_armor:                               ProgressiveArmor
    prog_weapons:                             ProgressiveWeapons
    temy_include:                             IncludeTemy
    cut_items:                                CutItems
    no_equips:                                NoEquips
    only_flakes:                              OnlyFlakes
    ice_traps:                                IceTraps
    love_reduction_traps:                     LoveReductionTraps
    max_hp_reduction_traps:                   MaxHPReductionTraps
    atk_reduction_traps:                      ATKReductionTraps
    def_reduction_traps:                      DEFReductionTraps
    # gifting:                                  Gifting
    # entrance_rando:                           EntranceRando
