from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, DeathLink, Range, Choice, PerGameCommonOptions

class TotalLocations(Range):
    """Number of pickups that should be considered for checks.  Please note that approximately 47 non-progress items and 3 progress items are in each run of the game."""
    display_name = "Total Locations"
    range_start = 20
    range_end = 250
    default = 47

class ItemWeights(Choice):
    """Set item_pool_presets to true if you want to use one of these presets.
    Preset choices for determining the weights of the item pool."""
    display_name = "Item Weights"
    option_default = 0

@dataclass
class ARNFOptions(PerGameCommonOptions):
    total_locations: TotalLocations
    item_weights: ItemWeights
    death_link: DeathLink
