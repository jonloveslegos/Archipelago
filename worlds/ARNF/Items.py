from typing import Callable, Dict, NamedTuple, Optional
from BaseClasses import Item, ItemClassification, MultiWorld
from .Locations import arnf_locations_start_id, normal_total_locations, classic_boss_rush_offset, classic_boss_rush_total_locations


class ARNFItem(Item):
    game: str = "A Robot Named Fight!"


class ARNFItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    can_create: Callable[[MultiWorld, int], bool] = lambda multiworld, player: True


normal_item_prefix = "NormalItem"
classic_boss_rush_item_prefix = "CBRItem"
item_data_table: Dict[str, ARNFItemData] = {}

for i in range(normal_total_locations):
    item_data_table[f"{normal_item_prefix}{i}"] = ARNFItemData(code = arnf_locations_start_id+i)
for i in range(classic_boss_rush_total_locations):
    item_data_table[f"{classic_boss_rush_item_prefix}{i}"] = ARNFItemData(code = arnf_locations_start_id+classic_boss_rush_offset+i)

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}