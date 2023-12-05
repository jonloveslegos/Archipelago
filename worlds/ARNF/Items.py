from typing import Callable, Dict, NamedTuple, Optional
from BaseClasses import Item, ItemClassification, MultiWorld
from .Options import ItemWeights

class ARNFItem(Item):
    game: str = "A Robot Named Fight!"

class ARNFItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    can_create: Callable[[MultiWorld, int], bool] = lambda multiworld, player: True


item_data_table: Dict[str, ARNFItemData] = {
    "NonProgressionItem": ARNFItemData(
        code=7331000,
        type=ItemClassification.filler,
    )
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}

# item_table: Dict[str, int] = {
    # "NonProgressionItem": 1,
    # "ProgressionItem":    2
# }

# default_weights: Dict[str, int] = {
    # "NonProgressionItem":    1,
    # "ProgressionItem":       0
# }

# item_pool_weights: Dict[int, Dict[str, int]] = {
    # ItemWeights.option_default:     default_weights
# }

# lookup_id_to_name: Dict[int, str] = {id: name for name, id in item_table.items()}