import logging

from typing import Callable, Dict, NamedTuple, Optional
from BaseClasses import Location
from .Options import NormalModeIncluded, ClassicBossRushIncluded


class ARNFLocation(Location):
    game: str = "A Robot Named Fight!"


arnf_locations_start_id = 73310000
normal_mode_total_locations = 35
classic_boss_rush_total_locations = 11

def get_ordered_item_pickups() -> Dict[str, int]:
    item_return: Dict[str, int] = {}
    logger = logging.getLogger()
    #logger.info(f'TotalLocations.range_end {TotalLocations.range_end}, max {max(n, 0)}, min {min(n, TotalLocations.range_end)}')
    
    #Add items for Normal Mode
    if NormalModeIncluded:
        item_return = {**item_return, **{ f"Normal{i+1}": arnf_locations_start_id+i for i in range(normal_mode_total_locations) }}
    
    #Add items for Classic Boss Rush
    if ClassicBossRushIncluded:
        item_return = {**item_return, **{ f"CBR{i+1}": arnf_locations_start_id+normal_mode_total_locations+i for i in range(classic_boss_rush_total_locations) }}
    
    return item_return


item_pickups = get_ordered_item_pickups()
location_table = item_pickups
lookup_id_to_name: Dict[int, str] = {id: name for name, id in location_table.items()}