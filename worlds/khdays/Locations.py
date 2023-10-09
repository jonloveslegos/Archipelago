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
    "Mission 5: Blazing Shard 1": 500500,
    "Mission 7: Potion 1": 500700,
    "Mission 7: Potion 2": 500701,
    "Mission 7: Shining Shard 3": 500702,
    "Mission 9: Fire Recipe 1": 500900,
    "Mission 9: Potion 2": 500901,
    "Mission 9: Blazing Shard 3": 500902,
    "Mission 9: Potion 4": 500903,
    "Mission 9: Blazing Shard 5": 500904,
    "Mission 9: Potion 6": 500905,
    "Mission 9: Blazing Shard 7": 500906,
    "Mission 8: Potion 1": 500800,
    "Mission 11: Potion 1": 501100,
    "Mission 11: Potion 2": 501101,
    "Mission 11: Potion 3": 501102,
    "Mission 11: Loaded Gear 5": 501104,
    "Mission 12: Potion 1": 501200,
    "Mission 12: Potion 2": 501201,
    "Mission 13: Power Unit 1": 501300,
    "Mission 14: Potion 1": 501400,
    "Mission 14: Potion 2": 501401,
    "Mission 14: Potion 5": 501404,
    "Moogle: Panel Slot 1": 510000,
    "Moogle: Aerial Recovery 1": 524700,
    "Moogle: Power Unit 1": 534600,
    "Moogle: Brawl Ring 1": 555800,
    "Moogle: Fire 1": 519200,
    "Moogle: Fire 2": 519201,
    "Moogle: Blizzard 1": 519500,
    "Moogle: Blizzard 2": 519501,
    "Moogle: Soldier Ring 1": 556000,
    "Moogle: Wild Gear 3 1": 530600,
    "Moogle: Lift Gear 3 1": 530400,
    "Moogle: Chrono Gear 3 1": 530000,
    "Moogle: Technical Gear 3 1": 529800,
    "Moogle: Triplecast 3 1": 521400,
    "Mission 15: Potion 2": 501501,
    "Mission 15: Potion 4": 501503,
    "Mission 15: Potion 5": 501504,
    "Mission 15: Panacea 1": 501500,
}

for i in range(20):
    location_table["Moogle: Potion "+str(i+1)] = 510100+i
    location_table["Moogle: Ether "+str(i+1)] = 510400+i

for i in range(10):
    location_table["Moogle: Fire "+str(i+3)] = 519200+i+2
    location_table["Moogle: Limit Recharge "+str(i+1)] = 511000+i

for i in range(39):
    location_table["Hub: Level Up "+str(1+i)] = 516200+i

for i in range(93):
    location_table["Mission "+str(i+1)+": Reward 1"] = 570101+(i*100)
    location_table["Mission "+str(i+1)+": Reward 2"] = 570102+(i*100)
    location_table["Mission "+str(i+1)+": Reward 3"] = 570103+(i*100)
    location_table["Mission "+str(i+1)+": Reward 4"] = 570104+(i*100)
    location_table["Mission "+str(i+1)+": Reward 5"] = 570105+(i*100)

lookup_id_to_Location: typing.Dict[int, str] = {data: item_name for item_name, data in location_table.items() if
                                                data}
