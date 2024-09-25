import logging

from typing import Callable, Dict, NamedTuple, Optional
from BaseClasses import Item, ItemClassification, MultiWorld
from .Constants import normal_item_prefix, progression_item_prefix, arnf_locations_start_id, normal_total_locations, normal_locations_region_one, normal_locations_region_two, normal_locations_region_three


class ARNFItem(Item):
    game: str = "A Robot Named Fight!"


class ARNFItemData(NamedTuple):
    code: Optional[int] = None
    amount_in_pool: int = 1
    type: ItemClassification = ItemClassification.filler
    can_create: Callable[[MultiWorld, int], bool] = lambda multiworld, player: True


# classic_boss_rush_item_prefix = "CBRItem"
# exterminator_item_prefix = "Exterm"
item_data_table: Dict[str, ARNFItemData] = {}

for i in range(0, normal_total_locations-2):
    item_data_table[f"{normal_item_prefix}{i+1}"] = ARNFItemData(code = arnf_locations_start_id+i+1)
item_data_table[f"{progression_item_prefix}4"] = ARNFItemData(code = arnf_locations_start_id+normal_total_locations-2, amount_in_pool = 1, type=ItemClassification.progression)
item_data_table[f"{progression_item_prefix}7"] = ARNFItemData(code = arnf_locations_start_id+normal_total_locations-1, amount_in_pool = 1, type=ItemClassification.progression)


# for i in range(1, normal_locations_region_one):
    # item_data_table[f"{normal_item_prefix}{i}"] = ARNFItemData(code = arnf_locations_start_id+i)
# item_data_table[f"{normal_item_prefix}{normal_locations_region_one}"] = ARNFItemData(code = arnf_locations_start_id+normal_locations_region_one, type=ItemClassification.progression)
# for i in range(normal_locations_region_one, normal_locations_region_one+normal_locations_region_two):
    # item_data_table[f"{normal_item_prefix}{i}"] = ARNFItemData(code = arnf_locations_start_id+i)
# item_data_table[f"{normal_item_prefix}{normal_locations_region_one+normal_locations_region_two}"] = ARNFItemData(code = arnf_locations_start_id+normal_locations_region_one+normal_locations_region_two, type=ItemClassification.progression)
# for i in range(normal_locations_region_one+normal_locations_region_two, normal_locations_region_one+normal_locations_region_two+normal_locations_region_three+1):
    # item_data_table[f"{normal_item_prefix}{i}"] = ARNFItemData(code = arnf_locations_start_id+i)


# for i in range(classic_boss_rush_total_locations):
    # item_data_table[f"{classic_boss_rush_item_prefix}{i}"] = ARNFItemData(code = arnf_locations_start_id+classic_boss_rush_offset+i)
# for i in range(exterminator_total_locations):
    # item_data_table[f"{exterminator_item_prefix}{i}"] = ARNFItemData(code = arnf_locations_start_id+exterminator_offset+i)

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}