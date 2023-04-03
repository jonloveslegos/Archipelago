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
    "Starting Ability 1": AdvData(0, "Starting Ability 1", "~3", 'The Glade P1'),
    "Starting Ability 2": AdvData(0, "Starting Ability 2", "~4", 'The Glade P1'),
    "Starting Ability 3": AdvData(0, "Starting Ability 3", "~5", 'The Glade P1'),
    "Ability 0": AdvData(0, "Ability 0", "~0", 'The Glade P2'),
    "Ability 1": AdvData(0, "Ability 1", "~1", 'Aurora Village'),
    "Ability 2": AdvData(0, "Ability 2", "~2", 'The Sorrowing Meadow'),
    "Ability 10": AdvData(0, "Ability 10", "~10", 'The Glade P2'),
    "Ability 12": AdvData(0, "Ability 12", "~12", 'The Glade P2'),
    "Ability 14": AdvData(0, "Ability 14", "~14", 'Cirromon Caverns P1'),
    "Ability 15": AdvData(0, "Ability 15", "~15", 'Blackmoor Mountains'),  # ~15 and 322
    "Ability 16": AdvData(0, "Ability 16", "~16", 'The Sorrowing Meadow'),  # ~16 and 330
    "Ability 17": AdvData(0, "Ability 16", "~17", 'Blackmoor Mountains'),  # ~16 and ~15 and ~1 and ~2 and ~17 and 322
    "Blue Resonance Gem": AdvData(0, "Blue Resonance Gem", "321", 'Aurora Village'),
    "Red Resonance Gem": AdvData(0, "Red Resonance Gem", "322", 'Aurora Village'),
    "Green Resonance Gem": AdvData(0, "Green Resonance Gem", "323", 'The Sorrowing Meadow'),
    "Yellow Resonance Gem": AdvData(0, "Yellow Resonance Gem", "324", 'Blackmoor Mountains'),  # ~16 and ~15 and 322
    "White Resonance Gem": AdvData(0, "White Resonance Gem", "325", 'Aurora Village'),  # ~14 or 325
    "Rainbow Resonance Gem": AdvData(0, "Equip cave12 RainbowKey 1", "328", 'The Sorrowing Meadow'),  # 308
    "Cove Key 1": AdvData(0, "cove01b 0key", "305", 'Hidden Cove'),  # ~16
    "Cove Key 2": AdvData(0, "cove01b 1key", "305", 'Hidden Cove'),  # ~16
    "Cove Wall 1": AdvData(0, "cove01 0wall", "4", 'Hidden Cove'),  # ~16
    "Cove Teleport Stone": AdvData(0, "cove02 0equip", "300", 'Hidden Cove'),  # ~16
    "Glade Key 1": AdvData(0, "intro01 0key", "305", 'The Glade P1'),
    "Glade Key 2": AdvData(0, "intro01 0key", "305", 'The Glade P2'),
    "Glade Key 3": AdvData(0, "intro06 0key", "305", 'The Glade P2'),
    "Glade Key 4": AdvData(0, "intro06 1key", "305", 'The Glade P2'),
    "Glade Key 5": AdvData(0, "intro07 0key", "305", 'The Glade P2'),
    "Glade Key 6": AdvData(0, "intro07b 0key", "305", 'Aurora Village'),
    "Glade Key 7": AdvData(0, "intro07b 1key", "305", 'Aurora Village'),
    "Ivydale Key 1": AdvData(0, "ivy01 0key", "305", 'Cirromon Caverns P2'),
    "Ivydale Key 2": AdvData(0, "ivy01 1key", "305", 'Cirromon Caverns P2'),
    "Village Key 1": AdvData(0, "village05 0key", "305", 'Aurora Village'),
    "Village Key 2": AdvData(0, "village05 1key", "305", 'Aurora Village'),
    "Village Wall 1": AdvData(0, "village05 0wall", "4", 'Aurora Village'),
    "Ivydale Wall 1": AdvData(0, "ivy01 0wall", "4", 'Ivydale Glen'),  # ~14 or 325
    "Ivydale Wall 2": AdvData(0, "ivy01 1wall", "4", 'Ivydale Glen'),  # ~14 or 325
    "Ivydale Wall 3": AdvData(0, "ivy02 0wall", "4", 'Ivydale Glen'),  # 325
    "Ivydale Laundry": AdvData(0, "ivy02 0equip", "338", 'Ivydale Glen'),  # 325
    "Glade Key 8": AdvData(0, "intro08c 0key", "305", 'Cirromon Caverns P1'),
    "Glade Key 9": AdvData(0, "intro08c 1key", "305", 'Cirromon Caverns P1'),
    "Smith Chest 1 Item 1": AdvData(0, "smith03 0", "126", 'Archers\' Pass'),
    "Smith Chest 2 Item 1": AdvData(0, "smith03b 2", "301", 'Archers\' Pass'),
    "Smith Chest 3 Item 1": AdvData(0, "smith03b 0", "194", 'Archers\' Pass'),
    "Smith Chest 4 Item 1": AdvData(0, "smith03b 1", "65", 'Archers\' Pass'),
    "Forest Chest 4 Item 1": AdvData(0, "forest09b 0", "16", 'Abadis Forest'),  # ~16
    "Forest Chest 4 Item 2": AdvData(0, "forest09b 0", "132", 'Abadis Forest'),  # ~16
    "Forest Chest 3 Item 1": AdvData(0, "forest08 0", "12", 'Abadis Forest'),  # ~15
    "Forest Chest 3 Item 2": AdvData(0, "forest08 0", "12", 'Abadis Forest'),  # ~15
    "Forest Chest 3 Item 3": AdvData(0, "forest08 0", "12", 'Abadis Forest'),  # ~15
    "Forest Chest 3 Item 4": AdvData(0, "forest08 0", "14", 'Abadis Forest'),  # ~15
    "Forest Chest 3 Item 5": AdvData(0, "forest08 0", "300", 'Abadis Forest'),  # ~15
    "Forest Chest 3 Item 6": AdvData(0, "forest08 0", "305", 'Abadis Forest'),  # ~15
    "Forest Chest 2 Item 1": AdvData(0, "forest04c 0", "301", 'Abadis Forest'),  # ~15 and ~16
    "Forest Chest 2 Item 2": AdvData(0, "forest04c 0", "200", 'Abadis Forest'),  # ~15 and ~16
    "Forest Chest 1 Item 1": AdvData(0, "forest02 0", "124", 'Abadis Forest'),
    "Forest Chest 1 Item 2": AdvData(0, "forest02 0", "1", 'Abadis Forest'),
    "Forest Chest 1 Item 3": AdvData(0, "forest02 0", "1", 'Abadis Forest'),
    "Forest Chest 1 Item 4": AdvData(0, "forest02 0", "1", 'Abadis Forest'),
    "Forest Chest 1 Item 5": AdvData(0, "forest02 0", "1", 'Abadis Forest'),
    "Forest Chest 1 Item 6": AdvData(0, "forest02 0", "1", 'Abadis Forest'),
    "Forest Chest 1 Item 7": AdvData(0, "forest02 0", "1", 'Abadis Forest'),
    "Forest Chest 1 Item 8": AdvData(0, "forest02 0", "1", 'Abadis Forest'),
    "Forest Chest 1 Item 9": AdvData(0, "forest02 0", "1", 'Abadis Forest'),
    "Forest Chest 1 Item 10": AdvData(0, "forest02 0", "1", 'Abadis Forest'),
    "Forest Chest 1 Item 11": AdvData(0, "forest02 0", "1", 'Abadis Forest'),
    "Meadow Key 1": AdvData(0, "grave03 0key", "305", 'The Sorrowing Meadow'),
    "Meadow Key 2": AdvData(0, "grave04 0key", "305", 'The Sorrowing Meadow'),
    "Meadow Key 3": AdvData(0, "grave04 1key", "305", 'The Sorrowing Meadow'),
    "Meadow Key 4": AdvData(0, "grave04 2key", "305", 'The Sorrowing Meadow'),
    "Meadow Key 5": AdvData(0, "grave07 0key", "305", 'The Sorrowing Meadow'),  # 323
    "Meadow Key 6": AdvData(0, "grave07 1key", "305", 'The Sorrowing Meadow'),  # 323
    "Meadow Key 7": AdvData(0, "grave11 0key", "305", 'The Sorrowing Meadow'),  # ~16
    "Meadow Key 8": AdvData(0, "grave20 0key", "305", 'The Sorrowing Meadow'),  # ~16
    "Meadow Key 9": AdvData(0, "grave21 0key", "305", 'The Sorrowing Meadow'),  # ~16
    "Meadow Key 10": AdvData(0, "grave21 1key", "305", 'The Sorrowing Meadow'),  # ~16
    "Meadow Key 11": AdvData(0, "grave21 2key", "305", 'The Sorrowing Meadow'),  # ~16
    "Meadow Key 12": AdvData(0, "grave23 0key", "305", 'The Sorrowing Meadow'),  # ~16
    "Meadow Key 13": AdvData(0, "grave24 0key", "305", 'The Sorrowing Meadow'),  # ~16
    "Meadow Key 14": AdvData(0, "grave24 1key", "305", 'The Sorrowing Meadow'),  # ~16
    "Meadow Key 15": AdvData(0, "grave13 0key", "305", 'The Sorrowing Meadow'),  # ~16 and ~15
    "Meadow Key 16": AdvData(0, "grave13b 0key", "305", 'The Sorrowing Meadow'),  # ~16 and ~15
    "Meadow Key 17": AdvData(0, "grave13b 1key", "305", 'The Sorrowing Meadow'),  # ~16 and ~15
    "Meadow Key 18": AdvData(0, "grave13b 2key", "305", 'The Sorrowing Meadow'),  # ~16 and ~15
    "Meadow Key 19": AdvData(0, "grave22 0key", "305", 'The Sorrowing Meadow'),  # ~16 and ~17
    "Meadow Key 20": AdvData(0, "grave22 1key", "305", 'The Sorrowing Meadow'),  # ~16 and ~17
    "Meadow Key 21": AdvData(0, "grave22 2key", "305", 'The Sorrowing Meadow'),  # ~16 and ~17
    "Smith Key 1": AdvData(0, "smith00 0key", "305", 'Archers\' Pass'),  # ~15 and 321
    "Smith Key 3": AdvData(0, "smith04b 0key", "305", 'Archers\' Pass'),  # 321 and 322 and 323 and 324
    "Smith Key 4": AdvData(0, "smith04b 1key", "305", 'Archers\' Pass'),  # 321 and 322 and 323
    "Smith Key 2": AdvData(0, "smith04 0key", "305", 'Archers\' Pass'),
    "Smith Key 7": AdvData(0, "smith05 0key", "305", 'Cirromon Caverns P2'),  # ~15
    "Smith Key 6": AdvData(0, "smith05 1key", "305", 'Cirromon Caverns P2'),  # ~15
    "Smith Key 8": AdvData(0, "smith05 2key", "305", 'Cirromon Caverns P2'),  # ~15
    "Smith Key 5": AdvData(0, "smith06 0key", "305", 'Archers\' Pass'),
    "Smith Wall 1": AdvData(0, "smith00 0wall", "4", 'Archers\' Pass'),  # ~15 and 321
    "Smith Wall 2": AdvData(0, "smith04 0wall", "4", 'Archers\' Pass'),
    "Smith Wall 3": AdvData(0, "smith04 1wall", "4", 'Archers\' Pass'),
    "Smith Wall 4": AdvData(0, "smith04 2wall", "4", 'Archers\' Pass'),
    "Forest Key 1": AdvData(0, "forest03 0key", "305", 'Abadis Forest'),
    "Forest Key 2": AdvData(0, "forest07 0key", "305", 'Abadis Forest'),
    "Forest Key 3": AdvData(0, "forest08 0key", "305", 'Abadis Forest'),
    "Forest Key 4": AdvData(0, "forest08 1key", "305", 'Abadis Forest'),
    "Forest Key 5": AdvData(0, "forest09 0key", "305", 'Abadis Forest'),
    "Forest Key 6": AdvData(0, "forest11 0key", "305", 'Abadis Forest'),
    "Forest Wall 1": AdvData(0, "forest07 0wall", "4", 'Abadis Forest'),  # 321
    "Forest Wall 2": AdvData(0, "forest08c 0wall", "4", 'Abadis Forest'),
    "Forest Wall 3": AdvData(0, "forest09 0wall", "4", 'Abadis Forest'),
    "Forest Wall 4": AdvData(0, "forest09 1wall", "4", 'Abadis Forest'),
    "Cave Wall 1": AdvData(0, "cave02b 0wall", "4", 'Cirromon Caverns P1'),
    "Cave Wall 2": AdvData(0, "cave02b 1wall", "4", 'Cirromon Caverns P2'),
    "Cave Key 1": AdvData(0, "cave02 0key", "305", 'Cirromon Caverns P1'),
    "Cave Key 2": AdvData(0, "cave02b 0key", "305", 'Cirromon Caverns P2'),
    "Cave Key 3": AdvData(0, "cave02b 1key", "305", 'Cirromon Caverns P2'),
    "Cave Key 4": AdvData(0, "cave02b 2key", "305", 'Cirromon Caverns P2'),
    "Cave Key 5": AdvData(0, "cave05b 0key", "305", 'Cirromon Caverns P1'),
    "Cave Key 6": AdvData(0, "cave05b 1key", "305", 'Cirromon Caverns P1'),
    "Cave Key 7": AdvData(0, "cave05b 2key", "305", 'Cirromon Caverns P1'),
    "Cave Key 8": AdvData(0, "cave08 0key", "305", 'Cirromon Caverns P1'),
    "Cave Key 9": AdvData(0, "cave12 0key", "305", 'Cirromon Caverns P1'),
    "Cave Key 10": AdvData(0, "cave12b 0key", "305", 'The Sorrowing Meadow'),
    "Cave Key 11": AdvData(0, "cave12b 1key", "305", 'Cirromon Caverns P1'),
    "Cave Key 12": AdvData(0, "cave12b 2key", "305", 'Cirromon Caverns P1'),
    "Cave Key 13": AdvData(0, "cave13 0key", "305", 'Cirromon Caverns P1'),
    "Cave Key 14": AdvData(0, "cave19 0key", "305", 'Cirromon Caverns P2'),  # ~17 and 322
    "Cave Key 15": AdvData(0, "cave21 0key", "305", 'Cirromon Caverns P2'),  # ~15 and 322
    "Cave Key 16": AdvData(0, "cave21 1key", "305", 'Cirromon Caverns P2'),
    "Cave Key 17": AdvData(0, "cave23 0key", "305", 'The Sorrowing Meadow'),
    "Cave Key 18": AdvData(0, "cave27 0key", "305", 'Cirromon Caverns P2'),  # ~15 and 322
    "Cave Wall 4": AdvData(0, "cave12 0wall", "4", 'Cirromon Caverns P1'),
    "Cave Wall 5": AdvData(0, "cave12 1wall", "4", 'Cirromon Caverns P2'),
    "Cave Wall 6": AdvData(0, "cave13 0wall", "4", 'The Sorrowing Meadow'),
    "Cave Wall 7": AdvData(0, "cave15 0wall", "4", 'Cirromon Caverns P1'),  # 322 and ~16
    "Cave Wall 9": AdvData(0, "cave27 0wall", "4", 'Cirromon Caverns P1'),  # 322 and ~15
    "Cave Wall 8": AdvData(0, "cave19 0wall", "4", 'The Sorrowing Meadow'),
    "Forest Haley Device": AdvData(0, "forest07 0equip", "320", 'Abadis Forest'),  # 321
    "Cave Chest 2 Item 1": AdvData(0, "cave04 0", "-252", 'Cirromon Caverns P1'),
    "Cave Chest 9 Item 1": AdvData(0, "cave27 0", "-254", 'The Sorrowing Meadow'),
    "Cave Chest 8 Item 1": AdvData(0, "cave24 0", "13", 'The Sorrowing Meadow'),
    "Cave Chest 8 Item 2": AdvData(0, "cave24 0", "13", 'The Sorrowing Meadow'),
    "Cave Chest 8 Item 3": AdvData(0, "cave24 0", "13", 'The Sorrowing Meadow'),
    "Cave Chest 8 Item 4": AdvData(0, "cave24 0", "13", 'The Sorrowing Meadow'),
    "Cave Chest 8 Item 5": AdvData(0, "cave24 0", "13", 'The Sorrowing Meadow'),
    "Cave Chest 8 Item 6": AdvData(0, "cave24 0", "249", 'The Sorrowing Meadow'),
    "Cave Chest 7 Item 1": AdvData(0, "cave22 0", "-195", 'The Sorrowing Meadow'),
    "Cave Chest 6 Item 1": AdvData(0, "cave19b 0", "-139", 'Cirromon Caverns P2'),  # ~17 and 322
    "Cave Chest 5 Item 1": AdvData(0, "cave17 0", "15", 'The Sorrowing Meadow'),
    "Cave Chest 5 Item 2": AdvData(0, "cave17 0", "12", 'The Sorrowing Meadow'),
    "Cave Chest 5 Item 3": AdvData(0, "cave17 0", "12", 'The Sorrowing Meadow'),
    "Cave Chest 5 Item 4": AdvData(0, "cave17 0", "12", 'The Sorrowing Meadow'),
    "Cave Chest 5 Item 5": AdvData(0, "cave17 0", "12", 'The Sorrowing Meadow'),
    "Cave Chest 5 Item 6": AdvData(0, "cave17 0", "12", 'The Sorrowing Meadow'),
    "Cave Chest 5 Item 7": AdvData(0, "cave17 0", "73", 'The Sorrowing Meadow'),
    "Cave Chest 4 Item 1": AdvData(0, "cave05b 0", "15", 'Cirromon Caverns P1'),
    "Cave Chest 4 Item 2": AdvData(0, "cave05b 0", "13", 'Cirromon Caverns P1'),
    "Cave Chest 4 Item 3": AdvData(0, "cave05b 0", "250", 'Cirromon Caverns P1'),
    "Cave Chest 3 Item 1": AdvData(0, "cave04 1", "10", 'Cirromon Caverns P1'),
    "Cave Chest 3 Item 2": AdvData(0, "cave04 1", "10", 'Cirromon Caverns P1'),
    "Cave Chest 3 Item 3": AdvData(0, "cave04 1", "10", 'Cirromon Caverns P1'),
    "Cave Chest 3 Item 4": AdvData(0, "cave04 1", "-70", 'Cirromon Caverns P1'),
    "Meadow Chest 11 Item 1": AdvData(0, "grave24 0", "16", 'Cirromon Caverns P2'),  # ~16 and 322
    "Meadow Chest 11 Item 2": AdvData(0, "grave24 0", "16", 'Cirromon Caverns P2'),  # ~16 and 322
    "Meadow Chest 11 Item 3": AdvData(0, "grave24 0", "16", 'Cirromon Caverns P2'),  # ~16 and 322
    "Meadow Chest 11 Item 4": AdvData(0, "grave24 0", "16", 'Cirromon Caverns P2'),  # ~16 and 322
    "Meadow Chest 11 Item 5": AdvData(0, "grave24 0", "15", 'Cirromon Caverns P2'),  # ~16 and 322
    "Meadow Chest 11 Item 6": AdvData(0, "grave24 0", "15", 'Cirromon Caverns P2'),  # ~16 and 322
    "Meadow Chest 10 Item 1": AdvData(0, "grave22 0", "253", 'Cirromon Caverns P2'),  # ~16 and 322
    "Meadow Chest 10 Item 2": AdvData(0, "grave22 0", "11", 'Cirromon Caverns P2'),  # ~16 and 322
    "Meadow Chest 10 Item 3": AdvData(0, "grave22 0", "11", 'Cirromon Caverns P2'),  # ~16 and 322
    "Meadow Chest 10 Item 4": AdvData(0, "grave22 0", "11", 'Cirromon Caverns P2'),  # ~16 and 322
    "Meadow Chest 10 Item 5": AdvData(0, "grave22 0", "11", 'Cirromon Caverns P2'),  # ~16 and 322
    "Meadow Chest 10 Item 6": AdvData(0, "grave22 0", "11", 'Cirromon Caverns P2'),  # ~16 and 322
    "Meadow Chest 9 Item 1": AdvData(0, "grave14 0", "18", 'Cirromon Caverns P2'),  # ~16 and 322
    "Meadow Chest 9 Item 2": AdvData(0, "grave14 0", "-134", 'Cirromon Caverns P2'),  # ~16 and 322
    "Meadow Chest 8 Item 1": AdvData(0, "grave13 0", "16", 'Cirromon Caverns P2'),  # ~16 and 322
    "Meadow Chest 8 Item 2": AdvData(0, "grave13 0", "16", 'Cirromon Caverns P2'),  # ~16 and 322
    "Meadow Chest 8 Item 3": AdvData(0, "grave13 0", "16", 'Cirromon Caverns P2'),  # ~16 and 322
    "Meadow Chest 8 Item 4": AdvData(0, "grave13 0", "-198", 'Cirromon Caverns P2'),  # ~16 and 322
    "Meadow Chest 7 Item 1": AdvData(0, "grave07 0", "76", 'Cirromon Caverns P2'),  # 323
    "Meadow Chest 6 Item 1": AdvData(0, "grave05 0", "-132", 'Cirromon Caverns P2'),
    "Meadow Chest 5 Item 1": AdvData(0, "grave09 0", "197", 'Cirromon Caverns P2'),  # 323
    "Meadow Chest 4 Item 1": AdvData(0, "grave08 0", "-256", 'Cirromon Caverns P1'),  # ~16 and 322 and 323
    "Meadow Chest 3 Item 1": AdvData(0, "grave04 0", "305", 'Cirromon Caverns P2'),
    "Meadow Chest 2 Item 1": AdvData(0, "grave03 0", "74", 'Cirromon Caverns P2'),
    "Meadow Chest 2 Item 2": AdvData(0, "grave03 0", "14", 'Cirromon Caverns P2'),
    "Meadow Chest 2 Item 3": AdvData(0, "grave03 0", "14", 'Cirromon Caverns P2'),
    "Meadow Chest 2 Item 4": AdvData(0, "grave03 0", "14", 'Cirromon Caverns P2'),
    "Cove Chest 1 Item 1": AdvData(0, "cove01 0", "14", 'Hidden Cove'),
    "Cove Chest 1 Item 2": AdvData(0, "cove01 0", "14", 'Hidden Cove'),
    "Cove Chest 1 Item 3": AdvData(0, "cove01 0", "14", 'Hidden Cove'),
    "Cove Chest 1 Item 4": AdvData(0, "cove01 0", "71", 'Hidden Cove'),
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
    "Farm Chest 1 Item 1": AdvData(0, "farm01 0", "10", 'Geehan\'s Farm'),
    "Farm Chest 1 Item 2": AdvData(0, "farm01 0", "10", 'Geehan\'s Farm'),
    "Farm Chest 1 Item 3": AdvData(0, "farm01 0", "10", 'Geehan\'s Farm'),
    "Farm Chest 1 Item 4": AdvData(0, "farm01 0", "191", 'Geehan\'s Farm'),
    "Glade Chest 4 Item 1": AdvData(0, "intro02b 0", "2", 'Cirromon Caverns P2'),
    "Glade Chest 4 Item 2": AdvData(0, "intro02b 0", "2", 'Cirromon Caverns P2'),
    "Glade Chest 4 Item 3": AdvData(0, "intro02b 0", "192", 'Cirromon Caverns P2'),
    "Village Fidget Doll 1": AdvData(0, "Equip village03 307 2", "307", 'Cirromon Caverns P1'),
    "Village Fidget Doll 2": AdvData(0, "Equip village03 307 2", "307", 'Cirromon Caverns P1'),
    "Meadow Chest 1 Item 1": AdvData(0, "grave01b 0", "17", 'Blackmoor Mountains'),  # ~16
    "Meadow Chest 1 Item 2": AdvData(0, "grave01b 0", "17", 'Blackmoor Mountains'),  # ~16
    "Meadow Chest 1 Item 3": AdvData(0, "grave01b 0", "17", 'Blackmoor Mountains'),  # ~16
    "Cave Chest 1 Item 1": AdvData(0, "cave02 0", "127", 'Cirromon Caverns P1'),
    "Cave Chest 1 Item 2": AdvData(0, "cave02 0", "12", 'Cirromon Caverns P1'),
    "Cave Chest 1 Item 3": AdvData(0, "cave02 0", "12", 'Cirromon Caverns P1'),
    "Cave Chest 1 Item 4": AdvData(0, "cave02 0", "12", 'Cirromon Caverns P1'),
    "Village Hotdog 1": AdvData(0, "Equip village03 16 3", "16", 'Everdawn Basin'),
    "Village Hotdog 2": AdvData(0, "Equip village03 16 3", "16", 'Everdawn Basin'),
    "Village Hotdog 3": AdvData(0, "Equip village03 16 3", "16", 'Everdawn Basin'),
    "Village Birthday Cake 1": AdvData(0, "Equip village02alt0 BirthdayCake 2", "20", 'Cirromon Caverns P1'),  # ~16
    "Village Birthday Cake 2": AdvData(0, "Equip village02alt0 BirthdayCake 2", "20", 'Cirromon Caverns P1'),  # ~16
    "Village Revival Stone 1": AdvData(0, "Equip village02alt0 301 2", "301", 'Cirromon Caverns P1'),  # 339
    "Village Revival Stone 2": AdvData(0, "Equip village02alt0 301 2", "301", 'Cirromon Caverns P1'),  # 339
    "Mansion A Item": AdvData(0, "mansiona02 0equip", "330", 'Cirromon Caverns P2'),  # 323 and 330
    "Mansion B Item": AdvData(0, "mansionb03 0equip", "331", 'The Sorrowing Meadow'),  # ~16 and 331
    "Mansion C Item": AdvData(0, "mansionc04 0equip", "332", 'The Sorrowing Meadow'),  # ~16 and 332
    "Mansion D Item": AdvData(0, "mansiond02 0equip", "333", 'The Sorrowing Meadow'),  # ~16 and 333
    "Meadow Wall 1": AdvData(0, "grave01b 0wall", "4", 'Blackmoor Mountains'),
    "Meadow Wall 2": AdvData(0, "grave03 0wall", "4", 'The Sorrowing Meadow'),
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
    "Cave Wall 3": AdvData(0, "cave05b 0wall", "4", 'Cirromon Caverns P1'),
    "Farm Wall 1": AdvData(0, "farm01 0wall", "4", 'Geehan\'s Farm'),  # ~12 or ~15
    "Farm Wall 2": AdvData(0, "farm01 1wall", "4", 'Geehan\'s Farm'),  # ~12 or ~15
    "Farm Wall 3": AdvData(0, "farm01 2wall", "4", 'Geehan\'s Farm'),  # ~12 or ~15
    "Farm Wall 4": AdvData(0, "farm01 3wall", "4", 'Geehan\'s Farm'),  # ~12 or ~15
    "Farm Wall 5": AdvData(0, "farm01 4wall", "4", 'Geehan\'s Farm'),  # ~12 or ~15
    "Farm Wall 6": AdvData(0, "farm02 0wall", "4", 'Geehan\'s Farm'),  # ~12 or ~15
    "Farm Watch": AdvData(0, "farm02 oequip", "341", 'Geehan\'s Farm'),  # ~12 or ~15
    "Cave Light Ring": AdvData(0, "Equip cave12 249 1", "249", 'Cirromon Caverns P2'),
    "Cave Doenjang 1": AdvData(0, "Equip cave12 Doenjang 3", "17", 'Cirromon Caverns P1'),  # 337
    "Cave Doenjang 2": AdvData(0, "Equip cave12 Doenjang 3", "17", 'Cirromon Caverns P1'),  # 337
    "Cave Doenjang 3": AdvData(0, "Equip cave12 Doenjang 3", "17", 'Cirromon Caverns P1'),  # 337
    "Cave Reed's Box 3": AdvData(0, "Equip cave12 ReedBox 1", "339", 'Cirromon Caverns P1'),  # 307
    "Cave Sheep 1": AdvData(0, "Equip cave08 0 GappySheep 1", "336", 'Cirromon Caverns P2'),
    "Cave Sheep 2": AdvData(0, "Equip cave12 0 GappySheep 1", "336", 'Cirromon Caverns P2'),
    "Cave Sheep 3": AdvData(0, "Equip cave12 1 GappySheep 1", "336", 'The Sorrowing Meadow'),
    "Cave Sheep 4": AdvData(0, "Equip cave13 0 GappySheep 1", "336", 'Cirromon Caverns P1'),
    "Cave Sheep 5": AdvData(0, "Equip cave15 0 GappySheep 1", "336", 'Cirromon Caverns P1'),  # 322
    "Cave Sheep 6": AdvData(0, "Equip cave21 0 GappySheep 1", "336", 'The Sorrowing Meadow'),
    "Cave Red Moss 1": AdvData(0, "cave24 0equip", "337", 'The Sorrowing Meadow'),
    "Cave Red Moss 2": AdvData(0, "cave24 1equip", "337", 'The Sorrowing Meadow'),
    "Cave Red Moss 3": AdvData(0, "cave24 2equip", "337", 'The Sorrowing Meadow'),
    "Cave Stick": AdvData(0, "cave14 0equip", "335", 'The Sorrowing Meadow'),
    "Cave Red Orb": AdvData(0, "cave15 1equip", "306", 'Cirromon Caverns P1'),  # 322 and ~16
    "Challenge 1 Giant Augment": AdvData(0, "challenge00 0equip", "126", 'Aurora Village'),
    "Challenge 2 Key 1": AdvData(0, "challenge01 0key", "305", 'Aurora Village'),  # ~15
    "Challenge 2 Wetsuit": AdvData(0, "challenge01b 0equip", "194", 'Aurora Village'),
    "Challenge 3 Spectral Vest": AdvData(0, "challenge02 0equip", "199", 'Aurora Village'),  # ~16
    "Challenge 4 Warrior Pendant": AdvData(0, "challenge03 0equip", "79", 'Cirromon Caverns P2'),  # ~16
    "Challenge 5 Ring": AdvData(0, "challenge04 0equip", "251", 'Cirromon Caverns P2'),  # ~16
    "Challenge 6 Chest 1 Item 1": AdvData(0, "challenge05 0", "131", 'Cirromon Caverns P2'),
    "Challenge 6 Scrap Augment": AdvData(0, "challenge05 0equip", "128", 'Cirromon Caverns P2'),
    "Poisioned Event Item 1": AdvData(0, "SideEvent 8 3 2", "3", 'Aurora Village'),
    "Poisioned Event Item 2": AdvData(0, "SideEvent 8 3 2", "3", 'Aurora Village'),
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
        advancement_table[adv] = AdvData(i+9683000, advancement_table[adv].game_id, advancement_table[adv].vanilla_item_id, advancement_table[adv].region)
        i += 1

exclusion_table = {
}

events_table = {
}

lookup_id_to_name: typing.Dict[int, str] = {data.id: item_name for item_name, data in advancement_table.items() if data.id}