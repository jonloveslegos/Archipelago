from Options import Range, Toggle, Choice, PerGameCommonOptions
from dataclasses import dataclass


class MaxAnimAppear(Range):
    """Max amount of Animatronics that will appear at once."""
    display_name = "Max Animatronics Appearing"
    range_start = 0
    range_end = 4
    default = 4


class RandoCatalogueUnlocks(Toggle):
    """Turns catalogue unlocks into checks."""
    display_name = "Catalogue Rando"
    default = 1


class FullWallet(Toggle):
    """
    Makes when you receive a Wallet Capacity Increase, it gives you money equivalent to your new maximum.
    (Requires Wallet Sanity to be enabled.)
    """
    display_name = "Full Wallet"
    default = 0


class SkipableNight(Toggle):
    """Makes it where you can immediately finish the office section if you have not received any animatronics."""
    display_name = "Skip-able Night"
    default = 1


class ToolUpgradeRando(Toggle):
    """Turns the speed upgrades for the tasks into checks."""
    display_name = "Speed Upgrade Rando"
    default = 0


class EasierMoneyGrinding(Toggle):
    """
    Gives you unlimited playtests to allow easier money grinding.
    LOGIC EXPECTS THIS TO BE ENABLED
    """
    display_name = "Easier Money Grinding"
    default = 1


class WalletSanity(Toggle):
    """Limits how much money you can have based on how many Wallet Capacity Increases you have obtained."""
    display_name = "Wallet-sanity"
    default = 0


class DaySanity(Toggle):
    """You need to receive the corresponding day item to go to the specific day."""
    display_name = "Day-sanity"
    default = 0


class NightDifficulty(Choice):
    """
    Alters mechanics in the Night Mode to make it easier or harder.
    
    Easy Mode:
    Makes the Motion Detector always show where the animatronics are located.
    
    Normal Mode:
    Mechanics are unchanged.
    """
    display_name = "Night Mode Difficulty"
    option_easy = 1
    option_normal = 0
    default = 0


@dataclass
class FFPSOptions(PerGameCommonOptions):
    max_animatronics_appearing:                           MaxAnimAppear
    catalogue_rando:                           RandoCatalogueUnlocks
    night_difficulty:                           NightDifficulty
    upgrade_rando:                           ToolUpgradeRando
    easier_money_grinding:                           EasierMoneyGrinding
    wallet_sanity:                                    WalletSanity
    full_wallet:                           FullWallet
    day_sanity:                            DaySanity
    skipable_night:                         SkipableNight
