import typing

from BaseClasses import Location
from .Items import item_table, ItemData


class KHDaysLocation(Location):
    game: str = "Kingdom Hearts Days"
    code: int = 0


location_table = {}

for (name) in item_table:
    for i in range(item_table[name].khdaysamount):
        location_table[name+" "+str(i+1)] = 500000+i+1+(item_table[name].khdaysaddress*1000)-1654784000

lookup_id_to_Location: typing.Dict[int, str] = {data: item_name for item_name, data in location_table.items() if
                                                data}
