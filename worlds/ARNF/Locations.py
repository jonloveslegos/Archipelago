import logging

from typing import Callable, Dict, NamedTuple, Optional
from BaseClasses import Location


class ARNFLocation(Location):
    game: str = "A Robot Named Fight!"

# TODO: Figure out locked items for ability to add progression items to Archipelago
# class ARNFLocationData(NamedTuple):
    # region: str
    # address: Optional[int] = None
    # locked_item: Optional[str] = None


arnf_locations_start_id = 73310000
normal_total_locations = 36
classic_boss_rush_offset = 50
classic_boss_rush_total_locations = 13
exterminator_offset = 100
exterminator_total_locations = 47


def get_ordered_item_pickups(game_mode: int = 1) -> Dict[str, int]:
    item_return: Dict[str, int] = {}
    logger = logging.getLogger()
    
    #Add items for Normal Mode
    if game_mode == 1:
        item_return = {**item_return, **{ f"Normal{i+1}": arnf_locations_start_id+i for i in range(normal_total_locations) }}
    
    #Add items for Classic Boss Rush
    if game_mode == 2:
        item_return = {**item_return, **{ f"CBR{i+1}": arnf_locations_start_id+classic_boss_rush_offset+i for i in range(classic_boss_rush_total_locations) }}
    
    #Add items for Exterminator
    if game_mode == 4:
        item_return = {**item_return, **{ f"Exterm{i+1}": arnf_locations_start_id+exterminator_offset+i for i in range(exterminator_total_locations) }}
    
    return item_return


item_pickups = get_ordered_item_pickups()
location_table = item_pickups
lookup_id_to_name: Dict[int, str] = {id: name for name, id in location_table.items()}