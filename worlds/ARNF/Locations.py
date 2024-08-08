import logging

from typing import Callable, Dict, NamedTuple, Optional
from BaseClasses import Location, MultiWorld
from .Constants import normal_location_prefix, normal_item_prefix, progression_item_prefix, arnf_locations_start_id, normal_total_locations, normal_locations_region_one, normal_locations_region_two, normal_locations_region_three


class ARNFLocation(Location):
    game: str = "A Robot Named Fight!"

# TODO: Figure out locked items for ability to add progression items to Archipelago
class ARNFLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable[[MultiWorld, int], bool] = lambda multiworld, player: True
    locked_item: Optional[str] = None


def get_ordered_item_pickups(game_mode: int = 1) -> Dict[str, ARNFLocationData]:
    item_return: Dict[str, ARNFLocationData] = {}
    logger = logging.getLogger()
    
    #Add items for Normal Mode
    if game_mode == 1:
        # item_return = {**item_return, **{ f"Normal{i+1}": arnf_locations_start_id+i for i in range(normal_total_locations) }}
        for i in range(1, normal_locations_region_one+1):
            item_return[f"{normal_location_prefix}{i}"] = ARNFLocationData(region = "BreakoutOne", address=arnf_locations_start_id+i)
        for i in range(normal_locations_region_one+1, normal_locations_region_one+normal_locations_region_two+1):
            item_return[f"{normal_location_prefix}{i}"] = ARNFLocationData(region = "BreakoutTwo", address=arnf_locations_start_id+i, locked_item=f"{progression_item_prefix}4")
        for i in range(normal_locations_region_one+normal_locations_region_two+1, normal_locations_region_one+normal_locations_region_two+normal_locations_region_three+1):
            item_return[f"{normal_location_prefix}{i}"] = ARNFLocationData(region = "BreakoutThree", address=arnf_locations_start_id+i, locked_item=f"{progression_item_prefix}7")
        
    # #Add items for Classic Boss Rush
    # if game_mode == 2:
        # item_return = {**item_return, **{ f"CBR{i+1}": arnf_locations_start_id+classic_boss_rush_offset+i for i in range(classic_boss_rush_total_locations) }}
    
    # #Add items for Exterminator
    # if game_mode == 4:
        # item_return = {**item_return, **{ f"Exterm{i+1}": arnf_locations_start_id+exterminator_offset+i for i in range(exterminator_total_locations) }}
    
    return item_return


# item_pickups = get_ordered_item_pickups()
# location_table = item_pickups
# lookup_id_to_name: Dict[int, str] = {id: name for name, id in location_table.items()}

location_data_table = get_ordered_item_pickups()
location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}