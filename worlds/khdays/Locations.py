import typing

from BaseClasses import Location
from .Items import item_table, ItemData


class KHDaysLocation(Location):
    game: str = "Kingdom Hearts Days"
    code: int = 0


location_table = {
    "Mission 1: Potion 1": 500100,
    "Mission 3: Potion 1": 500300,
    "Mission 4: Ether 1": 500400,
    "Mission 4: Ether 2": 500401,
    "Mission 4: Ether 3": 500402,
    "Mission 7: Potion 1": 500700,
    "Mission 7: Potion 2": 500701,
    "Mission 9: Potion 2": 500901,
    "Mission 9: Potion 4": 500903,
    "Mission 9: Potion 6": 500905,
    "Mission 8: Potion 1": 500800,
    "Mission 11: Potion 1": 501100,
    "Mission 11: Potion 2": 501101,
    "Mission 11: Potion 3": 501102,
    "Mission 11: Loaded Gear 5": 501104,
    "Mission 12: Potion 1": 501200,
    "Mission 12: Potion 2": 501201,
}

for i in range(36):
    location_table["Level Up "+str(2+i)] = 516200+i

for i in range(99):
    location_table["Moogle: Potion "+str(1+i)] = 510100+i

for i in range(93):
    location_table["Mission "+str(i+1)+": Reward 1"] = 520101+(i*100)
    location_table["Mission "+str(i+1)+": Reward 2"] = 520102+(i*100)
    location_table["Mission "+str(i+1)+": Reward 3"] = 520103+(i*100)
    location_table["Mission "+str(i+1)+": Reward 4"] = 520104+(i*100)
    location_table["Mission "+str(i+1)+": Reward 5"] = 520105+(i*100)

lookup_id_to_Location: typing.Dict[int, str] = {data: item_name for item_name, data in location_table.items() if
                                                data}
