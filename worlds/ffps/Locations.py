from BaseClasses import Location
import typing
from .Items import item_table


class LocData(typing.NamedTuple):
    id: typing.Optional[int]
    region: str
    setId: str


class CSData(typing.NamedTuple):
    id: typing.Optional[int]
    amount: int


class FFPSLocations(Location):
    game: str = "FFPS"

    def __init__(self, player: int, name: str, address: typing.Optional[int], parent):
        super().__init__(player, name, address, parent)
        self.event = not address


location_table = {
    "Salvage ScrapTrap": LocData(57500, 'Salvage', "m3"),
    "Salvage Scrap Baby": LocData(57501, 'Salvage', "m4"),
    "Salvage Lefty": LocData(57502, 'Salvage', "m5"),
    "Salvage Molten Freddy": LocData(57503, 'Salvage', "m2"),
    "Unlocked Catalogue 2": LocData(57504, 'Pizzeria', "un1"),
    "Unlocked Catalogue 3": LocData(57505, 'Pizzeria', "un2"),
    "Unlocked Catalogue 4": LocData(57506, 'Pizzeria', "un3"),
    "Bought Printer Upgrade": LocData(57507, 'Office', "printer"),
    "Bought Handyman Upgrade": LocData(57508, 'Office', "handyman"),
    "Bought Internet Upgrade": LocData(57509, 'Office', "hispeed"),
}

money_table = [
    CSData(57510, 1000),
    CSData(57511, 2000),
    CSData(57512, 3000),
    CSData(57513, 4000),
    CSData(57514, 5000),
    CSData(57515, 6000),
    CSData(57516, 7000),
    CSData(57517, 8000),
    CSData(57518, 9000),
    CSData(57519, 10000),
    CSData(57520, 11000),
    CSData(57521, 12000),
    CSData(57522, 13000),
    CSData(57523, 14000),
    CSData(57524, 15000),
    CSData(57525, 16000),
    CSData(57526, 17000),
    CSData(57527, 18000),
    CSData(57528, 19000),
    CSData(57529, 20000),
]

for itm in money_table:
    location_table.update({"Obtained "+str(itm.amount)+" Points": LocData(itm.id, 'Pizzeria', "")})

for name, data in item_table.items():
    if data.setId != "":
        if data.code >= 55600 and data.setId != "day2" and data.setId != "day3" and data.setId != "day4" and \
                data.setId != "day5" and data.setId != "day6" and data.setId != "stage" and \
                data.setId != "maxmoney" and data.setId != "money" and data.setId != "cups" and \
                data.setId != "speakers":
            location_table.update({"Buy " + name: LocData(len(location_table)+57500, 'Pizzeria', data.setId), })
for i in range(5):
    location_table.update({"Buy Stage Upgrade " +
                           str(i+1): LocData(len(location_table)+57500, 'Pizzeria', 'stage'), })
for i in range(4):
    location_table.update({"Buy Cups Upgrade " +
                           str(i+1): LocData(len(location_table)+57500, 'Pizzeria', 'cups'), })
for i in range(2):
    location_table.update({"Buy Speaker Upgrade " +
                           str(i+1): LocData(len(location_table)+57500, 'Pizzeria', 'speakers'), })

exclusion_table = {
}

events_table = {
}

lookup_id_to_name: typing.Dict[int, str] = {data.id: item_name for item_name, data in location_table.items() if data.id}
