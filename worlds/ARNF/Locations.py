import logging

from typing import Callable, Dict, NamedTuple, Optional
from BaseClasses import Location


class ARNFLocation(Location):
    game: str = "A Robot Named Fight!"


arnf_locations_start_id = 73310000
normal_total_locations = 36
classic_boss_rush_offset = 50
classic_boss_rush_total_locations = 13


def get_ordered_item_pickups(normal_included: int = 1, classic_boss_rush_included: int = 1) -> Dict[str, int]:
    item_return: Dict[str, int] = {}
    logger = logging.getLogger()
    
    #Add items for Normal Mode
    if normal_included == 1:
        item_return = {**item_return, **{ f"Normal{i+1}": arnf_locations_start_id+i for i in range(normal_total_locations) }}
    
    #Add items for Classic Boss Rush
    if classic_boss_rush_included:
        item_return = {**item_return, **{ f"CBR{i+1}": arnf_locations_start_id+classic_boss_rush_offset+i for i in range(classic_boss_rush_total_locations) }}
    
    return item_return


item_pickups = get_ordered_item_pickups()
location_table = item_pickups
lookup_id_to_name: Dict[int, str] = {id: name for name, id in location_table.items()}