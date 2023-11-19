from typing import Callable, Dict, NamedTuple, Optional
from BaseClasses import Item
from .Options import ItemWeights

class ARNFItem(Item):
    game: str = "A Robot Named Fight!"

item_table: Dict[str, int] = {
    "NonProgressionItem": 1,
    "ProgressionItem":    2
}

default_weights: Dict[str, int] = {
    "NonProgressionItem":    1,
    "ProgressionItem":       0
}

item_pool_weights: Dict[int, Dict[str, int]] = {
    ItemWeights.option_default:     default_weights
}

lookup_id_to_name: Dict[int, str] = {id: name for name, id in item_table.items()}
