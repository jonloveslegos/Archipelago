from typing import Callable, Dict, NamedTuple, Optional
from BaseClasses import Location
from .Options import TotalLocations

class ARNFLocation(Location):
    game: str = "A Robot Named Fight!"

def get_classic_item_pickups(n: int) -> Dict[str, int]:
    """Get n ItemPickups, capped at the max value for TotalLocations"""
    n = max(n, 0)
    n = min(n, TotalLocations.range_end)
    return { f"ItemPickup{i+1}": i for i in range(n) }

item_pickups = get_classic_item_pickups(TotalLocations.range_end)
location_table = item_pickups

lookup_id_to_name: Dict[int, str] = {id: name for name, id in location_table.items()}
