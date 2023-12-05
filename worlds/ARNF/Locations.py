import logging

from typing import Callable, Dict, NamedTuple, Optional
from BaseClasses import Location
from .Options import TotalLocations


class ARNFLocation(Location):
    game: str = "A Robot Named Fight!"


arnf_locations_start_id = 7331000


def get_ordered_item_pickups(n: int) -> Dict[str, int]:
    """Get n ItemPickups, capped at the max value for TotalLocations"""
    n = max(n, 0)
    n = min(n, TotalLocations.range_end)
    logger = logging.getLogger()
    logger.info(f'TotalLocations.range_end {TotalLocations.range_end}, max {max(n, 0)}, min {min(n, TotalLocations.range_end)}')
    return { f"ARNF{i+1}": arnf_locations_start_id+i for i in range(n) }


item_pickups = get_ordered_item_pickups(TotalLocations.range_end)
location_table = item_pickups
lookup_id_to_name: Dict[int, str] = {id: name for name, id in location_table.items()}