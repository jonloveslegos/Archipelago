import typing

from BaseClasses import Location
from .Items import item_table, ItemData


class KHDaysLocation(Location):
    game: str = "Kingdom Hearts Days"


location_table = {

}

for (name) in item_table:
    for i in range(item_table[name].khdaysamount):
        location_table[name+" "+str(i+1)] = 20000+i+(item_table[name].khdaysaddress*100)-165478400

lookup_id_to_Location: typing.Dict[int, str] = {data: item_name for item_name, data in location_table.items() if
                                                data}
