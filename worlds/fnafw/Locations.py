from BaseClasses import Location
import typing
from .Items import item_table


class LocData(typing.NamedTuple):
    id: typing.Optional[int]
    region: str
    setId: str


class FNaFWLocations(Location):
    game: str = "FNaFW"

    def __init__(self, player: int, name: str, address: typing.Optional[int], parent):
        super().__init__(player, name, address, parent)
        self.event = not address


location_table = {
    "Reinforced Endoskeleton": LocData(797197, "World", "ar1"),
    "Steel Endoskeleton": LocData(797198, "World", "ar2"),
    "Titanium Endoskeleton": LocData(797199, "World", "ar3"),
    #"Freddy": LocData(797200, "World", "1have"),
    #"Bonnie": LocData(797201, "World", "2have"),
    #"Chica": LocData(797202, "World", "3have"),
    #"Foxy": LocData(797203, "World", "4have"),
    #"Toy Bonnie": LocData(797204, "World", "5have"),
    #"Toy Chica": LocData(797205, "World", "6have"),
    #"Toy Freddy": LocData(797206, "World", "7have"),
    #"Mangle": LocData(797207, "World", "8have"),
    "Balloon Boy": LocData(797208, "World", "9have"),
    "JJ": LocData(797209, "World", "10have"),
    "Phantom Freddy": LocData(797210, "World", "11have"),
    "Phantom Chica": LocData(797211, "World", "12have"),
    "Phantom BB": LocData(797212, "World", "13have"),
    "Phantom Foxy": LocData(797213, "World", "14have"),
    "Phantom Mangle": LocData(797214, "World", "15have"),
    "Withered Bonnie": LocData(797215, "World", "16have"),
    "Withered Chica": LocData(797216, "World", "17have"),
    "Withered Freddy": LocData(797217, "World", "18have"),
    "Withered Foxy": LocData(797218, "World", "19have"),
    "Shadow Freddy": LocData(797219, "World", "20have"),
    "Marionette": LocData(797220, "World", "21have"),
    "Phantom Marionette": LocData(797221, "World", "22have"),
    "Golden Freddy": LocData(797222, "World", "23have"),
    "Paperpals": LocData(797223, "World", "24have"),
    "Nightmare Freddy": LocData(797224, "World", "25have"),
    "Nightmare Bonnie": LocData(797225, "World", "26have"),
    "Nightmare Chica": LocData(797226, "World", "27have"),
    "Nightmare Foxy": LocData(797227, "World", "28have"),
    "Endo 01": LocData(797228, "World", "29have"),
    "Endo 02": LocData(797229, "World", "30have"),
    "Plushtrap": LocData(797230, "World", "31have"),
    "Endoplush": LocData(797231, "World", "32have"),
    "Springtrap": LocData(797232, "World", "33have"),
    "RXQ": LocData(797233, "World", "34have"),
    "Crying Child": LocData(797234, "World", "35have"),
    "Funtime Foxy": LocData(797235, "World", "36have"),
    "Nightmare Fredbear": LocData(797236, "World", "37have"),
    "Nightmare": LocData(797237, "World", "38have"),
    "Fredbear": LocData(797238, "World", "39have"),
    "Spring Bonnie": LocData(797239, "World", "40have"),
    "Jack-O-Bonnie": LocData(797240, "World", "41have"),
    "Jack-O-Chica": LocData(797241, "World", "42have"),
    "Animdude": LocData(797242, "World", "43have"),
    "Mr. Chipper": LocData(797243, "World", "44have"),
    "Nightmare BB": LocData(797244, "World", "45have"),
    "Nightmarionne": LocData(797245, "World", "46have"),
    "Coffee": LocData(797246, "World", "47have"),
    "Purpleguy": LocData(797247, "World", "48have"),
    "Headstart Defense": LocData(797248, "World", "c1"),
    "Headstart Strength": LocData(797249, "World", "c2"),
    "Headstart Speed": LocData(797250, "World", "c3"),
    "Evercomet Weak": LocData(797251, "World", "c4"),
    "Quickstart Party": LocData(797252, "World", "c5"),
    "Block Jumpscare": LocData(797253, "World", "c6"),
    "Run Luck": LocData(797254, "World", "c7"),
    "Endless Defense": LocData(797255, "World", "c8"),
    "Endless Strength": LocData(797256, "World", "c9"),
    "Endless Speed": LocData(797257, "World", "c10"),
    "Evercomet Strong": LocData(797258, "World", "c11"),
    "Auto Giftboxes": LocData(797259, "World", "c12"),
    "Auto Regen": LocData(797260, "World", "c13"),
    "Find Characters": LocData(797261, "World", "c14"),
    "Curse Status": LocData(797262, "World", "c15"),
    "Freddle Fury": LocData(797263, "World", "c16"),
    "Auto Shield": LocData(797264, "World", "c17"),
    "Auto Mimic": LocData(797265, "World", "c18"),
    "Counter Bite": LocData(797266, "World", "c19"),
    "Pizza Fury": LocData(797267, "World", "c20"),
    "Block Unscrew": LocData(797268, "World", "c21"),
    "Gnat": LocData(797269, "World", "p1"),
    "Neon Bee": LocData(797270, "World", "p2"),
    "Neon Wasp": LocData(797271, "World", "p3"),
    "Medpod 1": LocData(797272, "World", "p4"),
    "Medpod 2": LocData(797273, "World", "p5"),
    "Mega-Med": LocData(797274, "World", "p6"),
    "Mini-Reaper": LocData(797275, "World", "p7"),
    "Reaper": LocData(797276, "World", "p8"),
    "X-Reaper": LocData(797277, "World", "p9"),
    "Mini-FO": LocData(797278, "World", "p10"),
    "UFO": LocData(797279, "World", "p11"),
    "X-FO": LocData(797280, "World", "p12"),
    "Block5": LocData(797281, "World", "p13"),
    "Block20": LocData(797282, "World", "p14"),
    "Block50": LocData(797283, "World", "p15"),
    "Pop-Pop": LocData(797284, "World", "p16"),
    "BOOM!": LocData(797285, "World", "p17"),
    "KABOOM!": LocData(797286, "World", "p18"),
    "BossDrain01": LocData(797287, "World", "p19"),
    "BossDrain02": LocData(797288, "World", "p20"),
    "BossDrain-X": LocData(797289, "World", "p21"),
}

exclusion_table = {
}

events_table = {
}

lookup_id_to_name: typing.Dict[int, str] = {data.id: item_name for item_name, data in location_table.items() if data.id}
