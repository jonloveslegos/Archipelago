from BaseClasses import Location
import typing
from .Items import item_table


class LocData(typing.NamedTuple):
    id: typing.Optional[int]
    region: str
    setId: str
    hintId: str = "NULL"


class FNaFWLocations(Location):
    game: str = "FNaFW"

    def __init__(self, player: int, name: str, address: typing.Optional[int], parent):
        super().__init__(player, name, address, parent)
        self.event = not address


location_table = {
    "Fazbear Hills: Endo Shop 1": LocData(797197, "World", "ar1", "arHINT1"),
    "Fazbear Hills: Endo Shop 2": LocData(797198, "World", "ar2", "arHINT2"),
    "Fazbear Hills: Endo Shop 3": LocData(797199, "World", "ar3", "arHINT3"),
    "Freddy": LocData(797200, "World", "1have"),
    "Bonnie": LocData(797201, "World", "2have"),
    "Chica": LocData(797202, "World", "3have"),
    "Foxy": LocData(797203, "World", "4have"),
    "Toy Bonnie": LocData(797204, "World", "5have"),
    "Toy Chica": LocData(797205, "World", "6have"),
    "Toy Freddy": LocData(797206, "World", "7have"),
    "Mangle": LocData(797207, "World", "8have"),
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
    "RWQ": LocData(797233, "World", "34have"),
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
    "Fazbear Hills: Auto Chipper Chest 1": LocData(797248, "World", "c1"),
    "Fazbear Hills: Auto Chipper Chest 2": LocData(797249, "World", "c2"),
    "Choppy's Woods: Near Lolbit South Chest": LocData(797250, "World", "c3"),
    "Choppy's Woods: Auto Chipper Chest": LocData(797251, "World", "c4"),
    "Dusting Fields: False Tree Chest": LocData(797252, "World", "c5"),
    "Blacktomb Yard: Near Bottom Chest": LocData(797253, "World", "c6"),
    "Choppy's Woods: Near Lolbit North Chest": LocData(797254, "World", "c7"),
    "Mysterious Mine: Topmost Cave Entrance Chest 1": LocData(797255, "World", "c8"),
    "Mysterious Mine: Topmost Cave Entrance Chest 2": LocData(797256, "World", "c9"),
    "Mysterious Mine: Warp 2 Chest": LocData(797257, "World", "c10"),
    "Mysterious Mine: Dusting Fields Cave Entrance Bottom Chest": LocData(797258, "World", "c11"),
    "Mysterious Mine: Dusting Fields Cave Entrance Top Chest": LocData(797259, "World", "c12"),
    "Pinwheel Circus: Past Browboy Chest": LocData(797260, "World", "c13"),
    "Deep-Metal Mine: Near Lolbit Chest": LocData(797261, "World", "c14"),
    "Deep-Metal Mine: Tent Entrance before Browboy Chest": LocData(797262, "World", "c15"),
    "Deep-Metal Mine: Lilygear Lake False Wall To Blacktomb Yard Chest": LocData(797263, "World", "c16"),
    "Lilygear Lake: Clip From Choppy's Woods Chest": LocData(797264, "World", "c17"),
    "Mysterious Mine: Clip From Blacktomb Yard Chest": LocData(797265, "World", "c18"),
    "Pinwheel Funhouse: False Wall After Bubba Chest": LocData(797266, "World", "c19"),
    "Choppy's Woods: False Trees Near Tent Chest": LocData(797267, "World", "c20"),
    "Fazbear Hills: Clip From Dusting Fields Chest": LocData(797268, "World", "c21"),
    "Fazbear Hills: Lolbit Shop 1": LocData(797269, "World", "p1", "pHINT1"),
    "Fazbear Hills: Lolbit Shop 2": LocData(797270, "World", "p2", "pHINT2"),
    "Fazbear Hills: Lolbit Shop 3": LocData(797271, "World", "p3", "pHINT3"),
    "Choppy's Woods: Lolbit Shop 1": LocData(797272, "World", "p4", "pHINT4"),
    "Choppy's Woods: Lolbit Shop 2": LocData(797273, "World", "p5", "pHINT5"),
    "Choppy's Woods: Lolbit Shop 3": LocData(797274, "World", "p6", "pHINT6"),
    "Dusting Fields: Lolbit Shop 1": LocData(797275, "World", "p7", "pHINT7"),
    "Dusting Fields: Lolbit Shop 2": LocData(797276, "World", "p8", "pHINT8"),
    "Dusting Fields: Lolbit Shop 3": LocData(797277, "World", "p9", "pHINT9"),
    "Pinwheel Circus: Lolbit Shop 1": LocData(797278, "World", "p10", "pHINT10"),
    "Pinwheel Circus: Lolbit Shop 2": LocData(797279, "World", "p11", "pHINT11"),
    "Pinwheel Circus: Lolbit Shop 3": LocData(797280, "World", "p12", "pHINT12"),
    "Mysterious Mine: Lolbit Shop 1": LocData(797281, "World", "p13", "pHINT13"),
    "Mysterious Mine: Lolbit Shop 2": LocData(797282, "World", "p14", "pHINT14"),
    "Mysterious Mine: Lolbit Shop 3": LocData(797283, "World", "p15", "pHINT15"),
    "Blacktomb Yard: Lolbit Shop 1": LocData(797284, "World", "p16", "pHINT16"),
    "Blacktomb Yard: Lolbit Shop 2": LocData(797285, "World", "p17", "pHINT17"),
    "Blacktomb Yard: Lolbit Shop 3": LocData(797286, "World", "p18", "pHINT18"),
    "Deep-Metal Mine: Lolbit Shop 1": LocData(797287, "World", "p19", "pHINT19"),
    "Deep-Metal Mine: Lolbit Shop 2": LocData(797288, "World", "p20", "pHINT20"),
    "Deep-Metal Mine: Lolbit Shop 3": LocData(797289, "World", "p21", "pHINT21"),
    "Choppy's Woods: Switch": LocData(797290, "World", "sw1"),
    "Lilygear Lake: Switch": LocData(797291, "World", "sw2"),
    "Blacktomb Yard: Switch": LocData(797292, "World", "sw3"),
    "Pinwheel Circus: Switch": LocData(797293, "World", "sw4"),
    "Lilygear Lake: Key Switch": LocData(797294, "World", "sw5"),
    "Dusting Fields: Laser Switch": LocData(797295, "World", "sw6"),
    "Fazbear Hills: Laser Switch": LocData(797296, "World", "sw7"),
    "Lilygear Lake: Laser Switch": LocData(797297, "World", "sw8"),
    "Deep-Metal Mine: Laser Switch": LocData(797298, "World", "sw9"),
    "Lilygear Lake: Key": LocData(797299, "World", "key"),
}

exclusion_table = {
}

events_table = {
}

lookup_id_to_name: typing.Dict[int, str] = {data.id: item_name for item_name, data in location_table.items() if data.id}
