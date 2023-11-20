from BaseClasses import Item, ItemClassification
import typing


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: any
    setId: str


class FNaFWItem(Item):
    game: str = "FFPS"


item_table = {
    "Progressive Endoskeleton": ItemData(797199, ItemClassification.useful, "armor"),
    "Freddy": ItemData(797200, ItemClassification.useful, "1have"),
    "Bonnie": ItemData(797201, ItemClassification.useful, "2have"),
    "Chica": ItemData(797202, ItemClassification.useful, "3have"),
    "Foxy": ItemData(797203, ItemClassification.useful, "4have"),
    "Toy Bonnie": ItemData(797204, ItemClassification.useful, "5have"),
    "Toy Chica": ItemData(797205, ItemClassification.useful, "6have"),
    "Toy Freddy": ItemData(797206, ItemClassification.useful, "7have"),
    "Mangle": ItemData(797207, ItemClassification.useful, "8have"),
    "Balloon Boy": ItemData(797208, ItemClassification.useful, "9have"),
    "JJ": ItemData(797209, ItemClassification.useful, "10have"),
    "Phantom Freddy": ItemData(797210, ItemClassification.useful, "11have"),
    "Phantom Chica": ItemData(797211, ItemClassification.useful, "12have"),
    "Phantom BB": ItemData(797212, ItemClassification.useful, "13have"),
    "Phantom Foxy": ItemData(797213, ItemClassification.useful, "14have"),
    "Phantom Mangle": ItemData(797214, ItemClassification.useful, "15have"),
    "Withered Bonnie": ItemData(797215, ItemClassification.useful, "16have"),
    "Withered Chica": ItemData(797216, ItemClassification.useful, "17have"),
    "Withered Freddy": ItemData(797217, ItemClassification.useful, "18have"),
    "Withered Foxy": ItemData(797218, ItemClassification.useful, "19have"),
    "Shadow Freddy": ItemData(797219, ItemClassification.useful, "20have"),
    "Marionette": ItemData(797220, ItemClassification.useful, "21have"),
    "Phantom Marionette": ItemData(797221, ItemClassification.useful, "22have"),
    "Golden Freddy": ItemData(797222, ItemClassification.useful, "23have"),
    "Paperpals": ItemData(797223, ItemClassification.useful, "24have"),
    "Nightmare Freddy": ItemData(797224, ItemClassification.useful, "25have"),
    "Nightmare Bonnie": ItemData(797225, ItemClassification.useful, "26have"),
    "Nightmare Chica": ItemData(797226, ItemClassification.useful, "27have"),
    "Nightmare Foxy": ItemData(797227, ItemClassification.useful, "28have"),
    "Endo 01": ItemData(797228, ItemClassification.useful, "29have"),
    "Endo 02": ItemData(797229, ItemClassification.useful, "30have"),
    "Plushtrap": ItemData(797230, ItemClassification.useful, "31have"),
    "Endoplush": ItemData(797231, ItemClassification.useful, "32have"),
    "Springtrap": ItemData(797232, ItemClassification.useful, "33have"),
    "RWQ": ItemData(797233, ItemClassification.useful, "34have"),
    "Crying Child": ItemData(797234, ItemClassification.useful, "35have"),
    "Funtime Foxy": ItemData(797235, ItemClassification.useful, "36have"),
    "Nightmare Fredbear": ItemData(797236, ItemClassification.useful, "37have"),
    "Nightmare": ItemData(797237, ItemClassification.useful, "38have"),
    "Fredbear": ItemData(797238, ItemClassification.useful, "39have"),
    "Spring Bonnie": ItemData(797239, ItemClassification.useful, "40have"),
    "Jack-O-Bonnie": ItemData(797240, ItemClassification.useful, "41have"),
    "Jack-O-Chica": ItemData(797241, ItemClassification.useful, "42have"),
    "Animdude": ItemData(797242, ItemClassification.useful, "43have"),
    "Mr. Chipper": ItemData(797243, ItemClassification.useful, "44have"),
    "Nightmare BB": ItemData(797244, ItemClassification.useful, "45have"),
    "Nightmarionne": ItemData(797245, ItemClassification.useful, "46have"),
    "Coffee": ItemData(797246, ItemClassification.useful, "47have"),
    "Purpleguy": ItemData(797247, ItemClassification.useful, "48have"),
    "Headstart Defense": ItemData(797248, ItemClassification.useful, "c1"),
    "Headstart Strength": ItemData(797249, ItemClassification.useful, "c2"),
    "Headstart Speed": ItemData(797250, ItemClassification.useful, "c3"),
    "Evercomet Weak": ItemData(797251, ItemClassification.useful, "c4"),
    "Quickstart Party": ItemData(797252, ItemClassification.useful, "c5"),
    "Block Jumpscare": ItemData(797253, ItemClassification.useful, "c6"),
    "Run Luck": ItemData(797254, ItemClassification.useful, "c7"),
    "Endless Defense": ItemData(797255, ItemClassification.useful, "c8"),
    "Endless Strength": ItemData(797256, ItemClassification.useful, "c9"),
    "Endless Speed": ItemData(797257, ItemClassification.useful, "c10"),
    "Evercomet Strong": ItemData(797258, ItemClassification.useful, "c11"),
    "Auto Giftboxes": ItemData(797259, ItemClassification.useful, "c12"),
    "Auto Regen": ItemData(797260, ItemClassification.useful, "c13"),
    "Find Characters": ItemData(797261, ItemClassification.progression, "c14"),
    "Curse Status": ItemData(797262, ItemClassification.useful, "c15"),
    "Freddle Fury": ItemData(797263, ItemClassification.useful, "c16"),
    "Auto Shield": ItemData(797264, ItemClassification.useful, "c17"),
    "Auto Mimic": ItemData(797265, ItemClassification.useful, "c18"),
    "Counter Bite": ItemData(797266, ItemClassification.useful, "c19"),
    "Pizza Fury": ItemData(797267, ItemClassification.useful, "c20"),
    "Block Unscrew": ItemData(797268, ItemClassification.useful, "c21"),
    "Gnat": ItemData(797269, ItemClassification.useful, "p1"),
    "Neon Bee": ItemData(797270, ItemClassification.useful, "p2"),
    "Neon Wasp": ItemData(797271, ItemClassification.useful, "p3"),
    "Medpod 1": ItemData(797272, ItemClassification.useful, "p4"),
    "Medpod 2": ItemData(797273, ItemClassification.useful, "p5"),
    "Mega-Med": ItemData(797274, ItemClassification.useful, "p6"),
    "Mini-Reaper": ItemData(797275, ItemClassification.useful, "p7"),
    "Reaper": ItemData(797276, ItemClassification.useful, "p8"),
    "X-Reaper": ItemData(797277, ItemClassification.useful, "p9"),
    "Mini-FO": ItemData(797278, ItemClassification.useful, "p10"),
    "UFO": ItemData(797279, ItemClassification.useful, "p11"),
    "X-FO": ItemData(797280, ItemClassification.useful, "p12"),
    "Block5": ItemData(797281, ItemClassification.useful, "p13"),
    "Block20": ItemData(797282, ItemClassification.useful, "p14"),
    "Block50": ItemData(797283, ItemClassification.useful, "p15"),
    "Pop-Pop": ItemData(797284, ItemClassification.useful, "p16"),
    "BOOM!": ItemData(797285, ItemClassification.useful, "p17"),
    "KABOOM!": ItemData(797286, ItemClassification.useful, "p18"),
    "BossDrain01": ItemData(797287, ItemClassification.useful, "p19"),
    "BossDrain02": ItemData(797288, ItemClassification.useful, "p20"),
    "BossDrain-X": ItemData(797289, ItemClassification.useful, "p21"),
    "Choppy's Woods Access Switch": ItemData(797290, ItemClassification.progression, "sw1"),
    "Lilygear Lake Access Switch": ItemData(797291, ItemClassification.progression, "sw2"),
    "Blacktomb Yard Access Switch": ItemData(797292, ItemClassification.progression, "sw3"),
    "Pinwheel Circus Access Switch": ItemData(797293, ItemClassification.progression, "sw4"),
    "Key Shortcut Switch": ItemData(797294, ItemClassification.progression, "sw5"),
    "Laser Switch 1": ItemData(797295, ItemClassification.progression, "sw6"),
    "Laser Switch 2": ItemData(797296, ItemClassification.progression, "sw7"),
    "Laser Switch 3": ItemData(797297, ItemClassification.progression, "sw8"),
    "Laser Switch 4": ItemData(797298, ItemClassification.progression, "sw9"),
    "Key": ItemData(797299, ItemClassification.progression, "key"),
    "Progressive Animatronic": ItemData(797300, ItemClassification.useful, "-"),
    "Progressive Chip": ItemData(797301, ItemClassification.progression, "-"),
    "Progressive Byte": ItemData(797302, ItemClassification.useful, "-"),
}

start_anim_table = [
    "Freddy",
    "Bonnie",
    "Chica",
    "Foxy",
    "Toy Bonnie",
    "Toy Chica",
    "Toy Freddy",
    "Mangle"
]

fazbear_hills_anim_table = [
    "Balloon Boy",
    "JJ",
    "Phantom Freddy",
    "Phantom BB",
    "Phantom Chica"
]

choppys_woods_anim_table = [
    "Phantom Mangle",
    "Withered Foxy",
    "Phantom Foxy"
]

dusting_fields_anim_table = [
    "Withered Chica",
    "Withered Freddy",
    "Withered Bonnie"
]

lilygear_lake_anim_table = [
    "Shadow Freddy",
    "Marionette",
    "Phantom Marionette"
]

mysterious_mine_anim_table = [
    "Golden Freddy",
    "Paperpals",
    "Nightmare Freddy"
]

blacktomb_yard_anim_table = [
    "Nightmare Bonnie",
    "Nightmare Chica",
    "Nightmare Foxy",
]

deep_metal_mine_anim_table = [
    "Endo 01",
    "Endo 02",
    "Plushtrap",
]

pinwheel_circus_anim_table = [
    "Endoplush",
    "Springtrap",
    "RWQ",
]

top_layer_anim_table = [
    "Crying Child",
    "Funtime Foxy",
    "Nightmare Fredbear",
]

pinwheel_funhouse_anim_table = [
    "Nightmare",
    "Fredbear",
    "Spring Bonnie",
]

halloween_anim_table = [
    "Jack-O-Chica",
    "Nightmare BB",
    "Coffee",
    "Jack-O-Bonnie",
    "Purpleguy",
    "Nightmarionne",
    "Mr. Chipper",
    "Animdude",
]

green_chip_table = [
    "Headstart Defense",
    "Headstart Strength",
    "Headstart Speed",
    "Evercomet Weak",
    "Quickstart Party",
    "Block Jumpscare",
    "Run Luck",
]

orange_chip_table = [
    "Evercomet Strong",
    "Endless Speed",
    "Auto Giftboxes",
    "Auto Regen",
    "Endless Defense",
    "Endless Strength",
]

red_chip_table = [
    "Curse Status",
    "Freddle Fury",
    "Auto Shield",
    "Auto Mimic",
    "Counter Bite",
    "Pizza Fury",
    "Block Unscrew"
]

weak_byte_table = [
    "Gnat",
    "Neon Bee",
    "Medpod 1",
    "Medpod 2",
]

byte_table = [
    "Neon Wasp",
    "Mini-Reaper",
    "Reaper",
    "Mini-FO",
    "UFO",
    "Block5",
    "Block20",
    "BossDrain01",
]

strong_byte_table = [
    "Mega-Med",
    "X-Reaper",
    "X-FO",
    "Block50",
    "Pop-Pop",
    "BOOM!",
    "KABOOM!",
    "BossDrain02",
    "BossDrain-X"
]

to_add_to_pool = {

    "Progressive Endoskeleton": 3,
    "Freddy": 1,
    "Bonnie": 1,
    "Chica": 1,
    "Foxy": 1,
    "Toy Bonnie": 1,
    "Toy Chica": 1,
    "Toy Freddy": 1,
    "Mangle": 1,
    "Balloon Boy": 1,
    "JJ": 1,
    "Phantom Freddy": 1,
    "Phantom Chica": 1,
    "Phantom BB": 1,
    "Phantom Foxy": 1,
    "Phantom Mangle": 1,
    "Withered Bonnie": 1,
    "Withered Chica": 1,
    "Withered Freddy": 1,
    "Withered Foxy": 1,
    "Shadow Freddy": 1,
    "Marionette": 1,
    "Phantom Marionette": 1,
    "Golden Freddy": 1,
    "Paperpals": 1,
    "Nightmare Freddy": 1,
    "Nightmare Bonnie": 1,
    "Nightmare Chica": 1,
    "Nightmare Foxy": 1,
    "Endo 01": 1,
    "Endo 02": 1,
    "Plushtrap": 1,
    "Endoplush": 1,
    "Springtrap": 1,
    "RWQ": 1,
    "Crying Child": 1,
    "Funtime Foxy": 1,
    "Nightmare Fredbear": 1,
    "Nightmare": 1,
    "Fredbear": 1,
    "Spring Bonnie": 1,
    "Jack-O-Bonnie": 1,
    "Jack-O-Chica": 1,
    "Animdude": 1,
    "Mr. Chipper": 1,
    "Nightmare BB": 1,
    "Nightmarionne": 1,
    "Coffee": 1,
    "Purpleguy": 1,
    "Headstart Defense": 1,
    "Headstart Strength": 1,
    "Headstart Speed": 1,
    "Evercomet Weak": 1,
    "Quickstart Party": 1,
    "Block Jumpscare": 1,
    "Run Luck": 1,
    "Endless Defense": 1,
    "Endless Strength": 1,
    "Endless Speed": 1,
    "Evercomet Strong": 1,
    "Auto Giftboxes": 1,
    "Auto Regen": 1,
    "Find Characters": 1,
    "Curse Status": 1,
    "Freddle Fury": 1,
    "Auto Shield": 1,
    "Auto Mimic": 1,
    "Counter Bite": 1,
    "Pizza Fury": 1,
    "Block Unscrew": 1,
    "Gnat": 1,
    "Neon Bee": 1,
    "Neon Wasp": 1,
    "Medpod 1": 1,
    "Medpod 2": 1,
    "Mega-Med": 1,
    "Mini-Reaper": 1,
    "Reaper": 1,
    "X-Reaper": 1,
    "Mini-FO": 1,
    "UFO": 1,
    "X-FO": 1,
    "Block5": 1,
    "Block20": 1,
    "Block50": 1,
    "Pop-Pop": 1,
    "BOOM!": 1,
    "KABOOM!": 1,
    "BossDrain01": 1,
    "BossDrain02": 1,
    "BossDrain-X": 1,
    "Choppy's Woods Access Switch": 1,
    "Lilygear Lake Access Switch": 1,
    "Blacktomb Yard Access Switch": 1,
    "Pinwheel Circus Access Switch": 1,
    "Key Shortcut Switch": 1,
    "Laser Switch 1": 1,
    "Laser Switch 2": 1,
    "Laser Switch 3": 1,
    "Laser Switch 4": 1,
    "Key": 1
}

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}
