from Options import Toggle, PerGameCommonOptions
from dataclasses import dataclass
try:
    from custom_worlds.undertale.Options import *
except ModuleNotFoundError:
    from worlds.undertale.Options import *


class IncludeUndertale(Toggle):
    """Includes Undertale in generation"""
    display_name = "Include Undertale"
    default = 0


@dataclass
class PangeaOptions(PerGameCommonOptions):
    include_undertale:                           IncludeUndertale

    # undertale
    route_required:                           RouteRequired
    starting_area:                            StartingArea
    key_hunt:                                 KeyHunt
    key_pieces:                               KeyPieces
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
    entrance_rando:                           EntranceRando

