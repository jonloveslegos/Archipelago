from BaseClasses import Location
import typing


class AdvData(typing.NamedTuple):
    id: typing.Optional[int]
    game_id: str
    vanilla_item_id: str
    region: str


class DustAETAdvancement(Location):
    game: str = "DustAET"

    def __init__(self, player: int, name: str, address: typing.Optional[int], parent):
        super().__init__(player, name, address, parent)
        self.event = not address


advancement_table = {
    "Glade Key 1": AdvData(0, "intro01 0key", "305", 'The Glade P1'),
    "Glade Key 2": AdvData(0, "intro01 0key", "305", 'The Glade P2'),
    "Glade Key 3": AdvData(0, "intro06 0key", "305", 'The Glade P2'),
    "Glade Key 4": AdvData(0, "intro06 1key", "305", 'The Glade P2'),
    "Glade Key 5": AdvData(0, "intro07 0key", "305", 'The Glade P2'),
    "Glade Key 6": AdvData(0, "intro07b 0key", "305", 'Aurora Village'),
    "Glade Key 7": AdvData(0, "intro07b 1key", "305", 'Aurora Village'),
    "Village Key 1": AdvData(0, "village05 0key", "305", 'Aurora Village'),
    "Village Key 2": AdvData(0, "village05 1key", "305", 'Aurora Village'),
    "Village Wall 1": AdvData(0, "village05 0wall", "4", 'Aurora Village'),
    "Glade Key 8": AdvData(0, "intro08c 0key", "305", 'Cirromon Caverns P1'),
    "Glade Key 9": AdvData(0, "intro08c 1key", "305", 'Cirromon Caverns P1'),
    "Glade Chest 1 Item 1": AdvData(0, "intro01b 0", "0", 'The Glade P2'),
    "Glade Chest 1 Item 2": AdvData(0, "intro01b 0", "1", 'The Glade P2'),
    "Glade Chest 1 Item 3": AdvData(0, "intro01b 0", "301", 'The Glade P2'),
    "Glade Chest 2 Item 1": AdvData(0, "intro05 0", "2", 'The Glade P2'),
    "Glade Chest 2 Item 2": AdvData(0, "intro05 0", "2", 'The Glade P2'),
    "Glade Chest 2 Item 3": AdvData(0, "intro05 0", "182", 'The Glade P2'),
    "Glade Chest 3 Item 1": AdvData(0, "intro07b 0", "0", 'The Glade P2'),
    "Glade Chest 3 Item 2": AdvData(0, "intro07b 0", "0", 'The Glade P2'),
    "Glade Chest 3 Item 3": AdvData(0, "intro07b 0", "61", 'The Glade P2'),
    "Village Chest 1 Item 1": AdvData(0, "village02 0", "10", 'Aurora Village'),
    "Village Chest 1 Item 2": AdvData(0, "village02 0", "10", 'Aurora Village'),
    "Village Chest 1 Item 3": AdvData(0, "village02 0", "10", 'Aurora Village'),
    "Village Chest 1 Item 4": AdvData(0, "village02 0", "3", 'Aurora Village'),
    "Village Chest 1 Item 5": AdvData(0, "village02 0", "242", 'Aurora Village'),
    "Village Chest 2 Item 1": AdvData(0, "village03 0", "10", 'Aurora Village'),
    "Village Chest 2 Item 2": AdvData(0, "village03 0", "300", 'Aurora Village'),
    "Village Chest 2 Item 3": AdvData(0, "village03 0", "62", 'Aurora Village'),
    "Glade Chest 4 Item 1": AdvData(0, "intro02b 0", "2", 'Cirromon Caverns P1'),
    "Glade Chest 4 Item 2": AdvData(0, "intro02b 0", "2", 'Cirromon Caverns P1'),
    "Glade Chest 4 Item 3": AdvData(0, "intro02b 0", "192", 'Cirromon Caverns P1'),
    "Village Fidget Doll 1": AdvData(0, "Equip village03 307 2", "307", 'Cirromon Caverns P1'),
    "Village Fidget Doll 2": AdvData(0, "Equip village03 307 2", "307", 'Cirromon Caverns P1'),
    "Village Hotdog 1": AdvData(0, "Equip village03 16 3", "16", 'Everdawn Basin'),
    "Village Hotdog 2": AdvData(0, "Equip village03 16 3", "16", 'Everdawn Basin'),
    "Village Hotdog 3": AdvData(0, "Equip village03 16 3", "16", 'Everdawn Basin'),
    "Village Birthday Cake 1": AdvData(0, "Equip village02alt0 BirthdayCake 2", "20", 'Cirromon Caverns P1'),  # ~16
    "Village Birthday Cake 2": AdvData(0, "Equip village02alt0 BirthdayCake 2", "20", 'Cirromon Caverns P1'),  # ~16
    "Village Revival Stone 1": AdvData(0, "Equip village02alt0 301 2", "301", 'Cirromon Caverns P1'),  # 339
    "Village Revival Stone 2": AdvData(0, "Equip village02alt0 301 2", "301", 'Cirromon Caverns P1'),  # 339
    "Glade Wall 1": AdvData(0, "intro01b 0wall", "4", 'The Glade P2'),
    "Glade Wall 2": AdvData(0, "intro01b 1wall", "4", 'The Glade P2'),
    "Glade Wall 3": AdvData(0, "intro05 0wall", "4", 'The Glade P2'),
    "Glade Wall 4": AdvData(0, "intro06 0wall", "4", 'The Glade P2'),
    "Glade Wall 5": AdvData(0, "intro06 1wall", "4", 'The Glade P2'),
    "Glade Wall 6": AdvData(0, "intro02b 0wall", "4", 'Aurora Village'),
    "Glade Wall 7": AdvData(0, "intro07b 0wall", "4", 'Aurora Village'),
    "Glade Wall 8": AdvData(0, "intro07b 1wall", "4", 'Aurora Village'),
    "Glade Wall 9": AdvData(0, "intro08 0wall", "4", 'Aurora Village'),
    "Glade Wall 10": AdvData(0, "intro08 1wall", "4", 'Aurora Village'),
    "Glade Wall 11": AdvData(0, "intro08b 0wall", "4", 'Aurora Village'),  # ~16
    "Glade Wall 12": AdvData(0, "intro08b 1wall", "4", 'Aurora Village'),  # ~16
    "Glade Wall 13": AdvData(0, "intro02b 1wall", "4", 'Cirromon Caverns P1'),
    "Glade Wall 14": AdvData(0, "intro08c 0wall", "4", 'Cirromon Caverns P1'),
    "Glade Wall 15": AdvData(0, "intro08c 1wall", "4", 'Cirromon Caverns P1'),
    "Glade Fidget Feeble Fruit Gift 1": AdvData(0, "Equip intro02 0 5", "0", 'The Glade P2'),
    "Glade Fidget Feeble Fruit Gift 2": AdvData(0, "Equip intro02 0 5", "0", 'The Glade P2'),
    "Glade Fidget Feeble Fruit Gift 3": AdvData(0, "Equip intro02 0 5", "0", 'The Glade P2'),
    "Glade Fidget Feeble Fruit Gift 4": AdvData(0, "Equip intro02 0 5", "0", 'The Glade P2'),
    "Glade Fidget Feeble Fruit Gift 5": AdvData(0, "Equip intro02 0 5", "0", 'The Glade P2'),
    "Glade Shopkeeper Blueprint Gift": AdvData(0, "Blueprint intro07b 190 1", "-190", 'The Glade P2'),
    "Village NPC Blueprint Gift": AdvData(0, "Blueprint village01 128 1", "-128", 'Aurora Village'),
    "Village Key Gift 1": AdvData(0, "Equip village01 TreasureKey 3", "305", 'Aurora Village'),  # 341
    "Village Key Gift 2": AdvData(0, "Equip village01 TreasureKey 3", "305", 'Aurora Village'),  # 341
    "Village Key Gift 3": AdvData(0, "Equip village01 TreasureKey 3", "305", 'Aurora Village'),  # 341
    "Sanctuary Standing Item": AdvData(0, "sanc02 0equip", "326", 'Aurora Village'),  # 305x4
}

i = 0
for adv in advancement_table:
    if advancement_table[adv].id == 0:
        advancement_table[adv] = AdvData(i+2800, advancement_table[adv].game_id, advancement_table[adv].vanilla_item_id, advancement_table[adv].region)
        i += 1

exclusion_table = {
}

events_table = {
}

lookup_id_to_name: typing.Dict[int, str] = {data.id: item_name for item_name, data in advancement_table.items() if data.id}