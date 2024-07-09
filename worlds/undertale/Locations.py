from BaseClasses import Location
import typing


class AdvData(typing.NamedTuple):
    id: typing.Optional[int]
    er_region: str  # entrance rando region
    location_group: str = "region"


class UndertaleAdvancement(Location):
    game: str = "Undertale"


advancement_table = {
    "Snowman Piece": AdvData(79100, "room_tundra6A"),
    "Snowman Piece 2": AdvData(79101, "room_tundra6A"),
    "Snowman Piece 3": AdvData(79102, "room_tundra6A"),
    "Nicecream Snowdin": AdvData(79001, "room_tundra8"),
    "Nicecream Waterfall": AdvData(79002, "room_water_nicecream"),
    "Nicecream Punch Card Trade": AdvData(79003, "room_water_nicecream"),
    "Quiche Bench": AdvData(79004, "room_water5A"),
    "Tutu Hidden": AdvData(79005, "room_water3A"),
    "Punch Card": AdvData(79006, "room_water_nicecream"),
    "Ballet Shoes": AdvData(79007, "room_water_shoe"),
    "Instant Noodles": AdvData(79008, "room_fire_lab1"),
    "Burnt Pan": AdvData(79009, "room_fire6A"),
    "Stained Apron": AdvData(79010, "room_fire_apron"),
    "Core Top-Left Trash Can": AdvData(79011, "room_fire_core_treasureleft"),
    "New Home Present 1": AdvData(79012, "room_asrielroom_final"),
    "New Home Present 2": AdvData(79013, "room_asrielroom_final"),
    "Monster Candy Bowl 1": AdvData(79014, "room_ruins7A"),
    "Monster Candy Bowl 2": AdvData(79015, "room_ruins7A"),
    "Monster Candy Bowl 3": AdvData(79016, "room_ruins7A"),
    "Monster Candy Bowl 4": AdvData(79017, "room_ruins7A"),
    "Left Spider Bake Sale": AdvData(79018, "room_ruins12B"),
    "Right Spider Bake Sale": AdvData(79019, "room_ruins12B"),
    "Faded Ribbon": AdvData(79020, "room_ruins14"),
    "Toy Knife": AdvData(79021, "room_ruins18OLD"),
    "B.Scotch Pie": AdvData(79022, "room_asrielroom"),
    "Astronaut Food 1": AdvData(79023, "room_water_trashzone2"),
    "Astronaut Food 2": AdvData(79024, "room_water_trashzone2"),
    "Sans Hot Dog Sale 1": AdvData(79026, "room_fire_hotdog"),
    "Sans Hot Cat Sale": AdvData(79027, "room_fire_hotdog"),
    "Sans Hot Dog Sale 2": AdvData(79028, "room_fire_hotdog"),
    "Sans Hot Dog Sale 3": AdvData(79029, "room_fire_hotdog"),
    "Sans Hot Dog Sale 4": AdvData(79030, "room_fire_hotdog"),
    "Popato Chisps Machine": AdvData(79031, "room_fire_labelevator"),
    "Hotel Door Hush Puppy": AdvData(79032, "room_fire_hoteldoors"),
    "Undyne Letter": AdvData(79033, "room_tundra_town"),
    "Snowdin Shop 1": AdvData(79034, "room_shop1"),
    "Snowdin Shop 2": AdvData(79035, "room_shop1"),
    "Snowdin Shop 3": AdvData(79036, "room_shop1"),
    "Snowdin Shop 4": AdvData(79037, "room_shop1"),
    "Gerson Shop 1": AdvData(79038, "room_shop2"),
    "Gerson Shop 2": AdvData(79039, "room_shop2"),
    "Gerson Shop 3": AdvData(79040, "room_shop2"),
    "Gerson Shop 4": AdvData(79041, "room_shop2"),
    "Bratty Catty Shop 1": AdvData(79042, "room_shop3"),
    "Bratty Catty Shop 2": AdvData(79043, "room_shop3"),
    "Bratty Catty Shop 3": AdvData(79044, "room_shop3"),
    "Bratty Catty Shop 4": AdvData(79045, "room_shop3"),
    "Burgerpants Shop 1": AdvData(79046, "room_shop4"),
    "Burgerpants Shop 2": AdvData(79047, "room_shop4"),
    "Burgerpants Shop 3": AdvData(79048, "room_shop4"),
    "Burgerpants Shop 4": AdvData(79049, "room_shop4"),
    "Temmie Shop 1": AdvData(79050, "room_shop5"),
    "Temmie Shop 2": AdvData(79051, "room_shop5"),
    "Temmie Shop 3": AdvData(79052, "room_shop5"),
    "Temmie Shop 4": AdvData(79053, "room_shop5"),
    "Papyrus Hangout": AdvData(79056, "room_tundra_town"),
    "Undyne Cook-off": AdvData(79057, "room_water_undyneyard"),
    "Mettaton Fight": AdvData(79062, "room_fire_core_metttest"),
    "Alphys Date": AdvData(79063, "room_fire_prelab"),
    "Left New Home Key": AdvData(79064, "room_kitchen_final"),
    "Right New Home Key": AdvData(79065, "room_asghouse3"),
    "Toriel Fight": AdvData(79066, "room_basement4"),
    "Papyrus Fight": AdvData(79067, "room_fogroom"),
    "Undyne Fight": AdvData(79068, "room_water_undynefinal"),
    "Hapstablook Diary 1": AdvData(79070, "room_water_hapstablook"),
    "Hapstablook Diary 2": AdvData(79071, "room_water_hapstablook"),
    "Hapstablook Diary 3": AdvData(79072, "room_water_hapstablook"),
    "Hapstablook Diary 4": AdvData(79073, "room_water_hapstablook"),
    "Hapstablook Diary 5": AdvData(79074, "room_water_hapstablook"),
    "Hapstablook Diary 6": AdvData(79075, "room_water_hapstablook"),
    "Ruins Colored Lever Fall Room": AdvData(79076, "room_ruins15E"),
    "Ruins Toriel's Room": AdvData(79077, "room_torielroom"),
    "Ruins Toriel's Kitchen": AdvData(79078, "room_kitchen"),
    "Snowdin Forest Fishing Rod": AdvData(79079, "room_tundra3A"),
    "Snowdin Forest Dog Smell Rating Station": AdvData(79080, "room_tundra8A"),
    "Snowdin Forest Sliding Puzzle Fall Room": AdvData(79081, "room_tundra_icehole"),
    "Snowdin Town Inn": AdvData(79082, "room_tundra_inn"),
    "Snowdin Town Grillby's": AdvData(79083, "room_tundra_grillby"),
    "Snowdin Town Librarby": AdvData(79084, "room_tundra_library"),
    "Waterfall Piano Puzzle": AdvData(79085, "room_water_piano"),
    "Waterfall Napstablook's House": AdvData(79086, "room_water_blookhouse"),
    "Hotland Upper Lab Room": AdvData(79087, "room_fire_lab2"),
    "Hotland Resort Restaurant": AdvData(79088, "room_fire_restaurant"),
    "Snowdin Forest Mysterious Door": AdvData(79089, "room_icecave1"),
    "LOVE 2": AdvData(79902, "???"),
    "LOVE 3": AdvData(79903, "???"),
    "LOVE 4": AdvData(79904, "???"),
    "LOVE 5": AdvData(79905, "???"),
    "LOVE 6": AdvData(79906, "???"),
    "LOVE 7": AdvData(79907, "???"),
    "LOVE 8": AdvData(79908, "???"),
    "LOVE 9": AdvData(79909, "???"),
    "LOVE 10": AdvData(79910, "???"),
    "LOVE 11": AdvData(79911, "???"),
    "LOVE 12": AdvData(79912, "???"),
    "LOVE 13": AdvData(79913, "???"),
    "LOVE 14": AdvData(79914, "???"),
    "LOVE 15": AdvData(79915, "???"),
    "LOVE 16": AdvData(79916, "???"),
    "LOVE 17": AdvData(79917, "???"),
    "LOVE 18": AdvData(79918, "???"),
    "LOVE 19": AdvData(79919, "???"),
    "LOVE 20": AdvData(79920, "???"),
    "ATK 2": AdvData(79800, "???"),
    "ATK 3": AdvData(79801, "???"),
    "ATK 4": AdvData(79802, "???"),
    "ATK 5": AdvData(79803, "???"),
    "ATK 6": AdvData(79804, "???"),
    "ATK 7": AdvData(79805, "???"),
    "ATK 8": AdvData(79806, "???"),
    "ATK 9": AdvData(79807, "???"),
    "ATK 10": AdvData(79808, "???"),
    "ATK 11": AdvData(79809, "???"),
    "ATK 12": AdvData(79810, "???"),
    "ATK 13": AdvData(79811, "???"),
    "ATK 14": AdvData(79812, "???"),
    "ATK 15": AdvData(79813, "???"),
    "ATK 16": AdvData(79814, "???"),
    "ATK 17": AdvData(79815, "???"),
    "ATK 18": AdvData(79816, "???"),
    "ATK 19": AdvData(79817, "???"),
    "ATK 20": AdvData(79818, "???"),
    "DEF 5": AdvData(79700, "???"),
    "DEF 9": AdvData(79701, "???"),
    "DEF 13": AdvData(79702, "???"),
    "DEF 17": AdvData(79703, "???"),
    "HP 2": AdvData(79600, "???"),
    "HP 3": AdvData(79601, "???"),
    "HP 4": AdvData(79602, "???"),
    "HP 5": AdvData(79603, "???"),
    "HP 6": AdvData(79604, "???"),
    "HP 7": AdvData(79605, "???"),
    "HP 8": AdvData(79606, "???"),
    "HP 9": AdvData(79607, "???"),
    "HP 10": AdvData(79608, "???"),
    "HP 11": AdvData(79609, "???"),
    "HP 12": AdvData(79610, "???"),
    "HP 13": AdvData(79611, "???"),
    "HP 14": AdvData(79612, "???"),
    "HP 15": AdvData(79613, "???"),
    "HP 16": AdvData(79614, "???"),
    "HP 17": AdvData(79615, "???"),
    "HP 18": AdvData(79616, "???"),
    "HP 19": AdvData(79617, "???"),
    "HP 20": AdvData(79618, "???"),
    "Ruins Kill 1": AdvData(79119, "Ruins Grind Rooms"),
    "Ruins Kill 2": AdvData(79120, "Ruins Grind Rooms"),
    "Ruins Kill 3": AdvData(79121, "Ruins Grind Rooms"),
    "Ruins Kill 4": AdvData(79122, "Ruins Grind Rooms"),
    "Ruins Kill 5": AdvData(79123, "Ruins Grind Rooms"),
    "Ruins Kill 6": AdvData(79124, "Ruins Grind Rooms"),
    "Ruins Kill 7": AdvData(79125, "Ruins Grind Rooms"),
    "Ruins Kill 8": AdvData(79126, "Ruins Grind Rooms"),
    "Ruins Kill 9": AdvData(79127, "Ruins Grind Rooms"),
    "Ruins Kill 10": AdvData(79128, "Ruins Grind Rooms"),
    "Ruins Kill 11": AdvData(79129, "Ruins Grind Rooms"),
    "Ruins Kill 12": AdvData(79130, "Ruins Grind Rooms"),
    "Ruins Kill 13": AdvData(79131, "Ruins Grind Rooms"),
    "Ruins Kill 14": AdvData(79132, "Ruins Grind Rooms"),
    "Ruins Kill 15": AdvData(79133, "Ruins Grind Rooms"),
    "Ruins Kill 16": AdvData(79134, "Ruins Grind Rooms"),
    "Ruins Kill 17": AdvData(79135, "Ruins Grind Rooms"),
    "Ruins Kill 18": AdvData(79136, "Ruins Grind Rooms"),
    "Ruins Kill 19": AdvData(79137, "Ruins Grind Rooms"),
    "Ruins Kill 20": AdvData(79138, "Ruins Grind Rooms"),
    "Snowdin Kill 1": AdvData(79139, "Snowdin Grind Rooms"),
    "Snowdin Kill 2": AdvData(79140, "Snowdin Grind Rooms"),
    "Snowdin Kill 3": AdvData(79141, "Snowdin Grind Rooms"),
    "Snowdin Kill 4": AdvData(79142, "Snowdin Grind Rooms"),
    "Snowdin Kill 5": AdvData(79143, "Snowdin Grind Rooms"),
    "Snowdin Kill 6": AdvData(79144, "Snowdin Grind Rooms"),
    "Snowdin Kill 7": AdvData(79145, "Snowdin Grind Rooms"),
    "Snowdin Kill 8": AdvData(79146, "Snowdin Grind Rooms"),
    "Snowdin Kill 9": AdvData(79147, "Snowdin Grind Rooms"),
    "Snowdin Kill 10": AdvData(79148, "Snowdin Grind Rooms"),
    "Snowdin Kill 11": AdvData(79149, "Snowdin Grind Rooms"),
    "Snowdin Kill 12": AdvData(79150, "Snowdin Grind Rooms"),
    "Snowdin Kill 13": AdvData(79151, "Snowdin Grind Rooms"),
    "Snowdin Kill 14": AdvData(79152, "Snowdin Grind Rooms"),
    "Snowdin Kill 15": AdvData(79153, "Snowdin Grind Rooms"),
    "Snowdin Kill 16": AdvData(79154, "Snowdin Grind Rooms"),
    "Waterfall Kill 1": AdvData(79155, "Waterfall Grind Rooms"),
    "Waterfall Kill 2": AdvData(79156, "Waterfall Grind Rooms"),
    "Waterfall Kill 3": AdvData(79157, "Waterfall Grind Rooms"),
    "Waterfall Kill 4": AdvData(79158, "Waterfall Grind Rooms"),
    "Waterfall Kill 5": AdvData(79159, "Waterfall Grind Rooms"),
    "Waterfall Kill 6": AdvData(79160, "Waterfall Grind Rooms"),
    "Waterfall Kill 7": AdvData(79161, "Waterfall Grind Rooms"),
    "Waterfall Kill 8": AdvData(79162, "Waterfall Grind Rooms"),
    "Waterfall Kill 9": AdvData(79163, "Waterfall Grind Rooms"),
    "Waterfall Kill 10": AdvData(79164, "Waterfall Grind Rooms"),
    "Waterfall Kill 11": AdvData(79165, "Waterfall Grind Rooms"),
    "Waterfall Kill 12": AdvData(79166, "Waterfall Grind Rooms"),
    "Waterfall Kill 13": AdvData(79167, "Waterfall Grind Rooms"),
    "Waterfall Kill 14": AdvData(79168, "Waterfall Grind Rooms"),
    "Waterfall Kill 15": AdvData(79169, "Waterfall Grind Rooms"),
    "Waterfall Kill 16": AdvData(79170, "Waterfall Grind Rooms"),
    "Waterfall Kill 17": AdvData(79171, "Waterfall Grind Rooms"),
    "Waterfall Kill 18": AdvData(79172, "Waterfall Grind Rooms"),
    "Hotland Kill 1": AdvData(79173, "???"),
    "Hotland Kill 2": AdvData(79174, "???"),
    "Hotland Kill 3": AdvData(79175, "???"),
    "Hotland Kill 4": AdvData(79176, "???"),
    "Hotland Kill 5": AdvData(79177, "???"),
    "Hotland Kill 6": AdvData(79178, "???"),
    "Hotland Kill 7": AdvData(79179, "???"),
    "Hotland Kill 8": AdvData(79180, "???"),
    "Hotland Kill 9": AdvData(79181, "???"),
    "Hotland Kill 10": AdvData(79182, "???"),
    "Hotland Kill 11": AdvData(79183, "???"),
    "Hotland Kill 12": AdvData(79184, "???"),
    "Hotland Kill 13": AdvData(79185, "???"),
    "Hotland Kill 14": AdvData(79186, "???"),
    "Hotland Kill 15": AdvData(79187, "???"),
    "Hotland Kill 16": AdvData(79188, "???"),
    "Hotland Kill 17": AdvData(79189, "???"),
    "Hotland Kill 18": AdvData(79190, "???"),
    "Hotland Kill 19": AdvData(79191, "???"),
    "Hotland Kill 20": AdvData(79192, "???"),
    "Hotland Kill 21": AdvData(79193, "???"),
    "Hotland Kill 22": AdvData(79194, "???"),
    "Hotland Kill 23": AdvData(79195, "???"),
    "Hotland Kill 24": AdvData(79196, "???"),
    "Hotland Kill 25": AdvData(79197, "???"),
    "Hotland Kill 26": AdvData(79198, "???"),
    "Hotland Kill 27": AdvData(79199, "???"),
    "Hotland Kill 28": AdvData(79200, "???"),
    "Hotland Kill 29": AdvData(79201, "???"),
    "Hotland Kill 30": AdvData(79202, "???"),
    "Hotland Kill 31": AdvData(79203, "???"),
    "Hotland Kill 32": AdvData(79204, "???"),
    "Hotland Kill 33": AdvData(79205, "???"),
    "Hotland Kill 34": AdvData(79206, "???"),
    "Hotland Kill 35": AdvData(79207, "???"),
    "Hotland Kill 36": AdvData(79208, "???"),
    "Hotland Kill 37": AdvData(79209, "???"),
    "Hotland Kill 38": AdvData(79210, "???"),
    "Hotland Kill 39": AdvData(79211, "???"),
    "Hotland Kill 40": AdvData(79212, "???"),
}

for i in range(100):
    advancement_table.__setitem__("Ruins Spare " + str(i + 1), AdvData(78013+i, "Ruins Grind Rooms"))
    advancement_table.__setitem__("Snowdin Spare " + str(i + 1), AdvData(78113+i, "Snowdin Grind Rooms"))
    advancement_table.__setitem__("Waterfall Spare " + str(i + 1), AdvData(78213+i, "Waterfall Grind Rooms"))
    advancement_table.__setitem__("Hotland Spare " + str(i + 1), AdvData(78313+i, "???"))

exclusion_table = {
    "pacifist": {
        "LOVE 2",
        "LOVE 3",
        "LOVE 4",
        "LOVE 5",
        "LOVE 6",
        "LOVE 7",
        "LOVE 8",
        "LOVE 9",
        "LOVE 10",
        "LOVE 11",
        "LOVE 12",
        "LOVE 13",
        "LOVE 14",
        "LOVE 15",
        "LOVE 16",
        "LOVE 17",
        "LOVE 18",
        "LOVE 19",
        "LOVE 20",
        "ATK 2",
        "ATK 3",
        "ATK 4",
        "ATK 5",
        "ATK 6",
        "ATK 7",
        "ATK 8",
        "ATK 9",
        "ATK 10",
        "ATK 11",
        "ATK 12",
        "ATK 13",
        "ATK 14",
        "ATK 15",
        "ATK 16",
        "ATK 17",
        "ATK 18",
        "ATK 19",
        "ATK 20",
        "DEF 5",
        "DEF 9",
        "DEF 13",
        "DEF 17",
        "HP 2",
        "HP 3",
        "HP 4",
        "HP 5",
        "HP 6",
        "HP 7",
        "HP 8",
        "HP 9",
        "HP 10",
        "HP 11",
        "HP 12",
        "HP 13",
        "HP 14",
        "HP 15",
        "HP 16",
        "HP 17",
        "HP 18",
        "HP 19",
        "HP 20",
        "Snowman Piece 2",
        "Snowman Piece 3",
        "Ruins Kill 1",
        "Ruins Kill 2",
        "Ruins Kill 3",
        "Ruins Kill 4",
        "Ruins Kill 5",
        "Ruins Kill 6",
        "Ruins Kill 7",
        "Ruins Kill 8",
        "Ruins Kill 9",
        "Ruins Kill 10",
        "Ruins Kill 11",
        "Ruins Kill 12",
        "Ruins Kill 13",
        "Ruins Kill 14",
        "Ruins Kill 15",
        "Ruins Kill 16",
        "Ruins Kill 17",
        "Ruins Kill 18",
        "Ruins Kill 19",
        "Ruins Kill 20",
        "Snowdin Kill 1",
        "Snowdin Kill 2",
        "Snowdin Kill 3",
        "Snowdin Kill 4",
        "Snowdin Kill 5",
        "Snowdin Kill 6",
        "Snowdin Kill 7",
        "Snowdin Kill 8",
        "Snowdin Kill 9",
        "Snowdin Kill 10",
        "Snowdin Kill 11",
        "Snowdin Kill 12",
        "Snowdin Kill 13",
        "Snowdin Kill 14",
        "Snowdin Kill 15",
        "Snowdin Kill 16",
        "Waterfall Kill 1",
        "Waterfall Kill 2",
        "Waterfall Kill 3",
        "Waterfall Kill 4",
        "Waterfall Kill 5",
        "Waterfall Kill 6",
        "Waterfall Kill 7",
        "Waterfall Kill 8",
        "Waterfall Kill 9",
        "Waterfall Kill 10",
        "Waterfall Kill 11",
        "Waterfall Kill 12",
        "Waterfall Kill 13",
        "Waterfall Kill 14",
        "Waterfall Kill 15",
        "Waterfall Kill 16",
        "Waterfall Kill 17",
        "Waterfall Kill 18",
        "Hotland Kill 1",
        "Hotland Kill 2",
        "Hotland Kill 3",
        "Hotland Kill 4",
        "Hotland Kill 5",
        "Hotland Kill 6",
        "Hotland Kill 7",
        "Hotland Kill 8",
        "Hotland Kill 9",
        "Hotland Kill 10",
        "Hotland Kill 11",
        "Hotland Kill 12",
        "Hotland Kill 13",
        "Hotland Kill 14",
        "Hotland Kill 15",
        "Hotland Kill 16",
        "Hotland Kill 17",
        "Hotland Kill 18",
        "Hotland Kill 19",
        "Hotland Kill 20",
        "Hotland Kill 21",
        "Hotland Kill 22",
        "Hotland Kill 23",
        "Hotland Kill 24",
        "Hotland Kill 25",
        "Hotland Kill 26",
        "Hotland Kill 27",
        "Hotland Kill 28",
        "Hotland Kill 29",
        "Hotland Kill 30",
        "Hotland Kill 31",
        "Hotland Kill 32",
        "Hotland Kill 33",
        "Hotland Kill 34",
        "Hotland Kill 35",
        "Hotland Kill 36",
        "Hotland Kill 37",
        "Hotland Kill 38",
        "Hotland Kill 39",
        "Hotland Kill 40",
    },
    "neutral": {
        "Undyne Letter",
        "Sans Hot Dog Sale 1",
        "Sans Hot Cat Sale",
        "Sans Hot Dog Sale 2",
        "Sans Hot Dog Sale 3",
        "Sans Hot Dog Sale 4",
        "Popato Chisps Machine",
        "Hotel Door Hush Puppy",
        "LOVE 2",
        "LOVE 3",
        "LOVE 4",
        "LOVE 5",
        "LOVE 6",
        "LOVE 7",
        "LOVE 8",
        "LOVE 9",
        "LOVE 10",
        "LOVE 11",
        "LOVE 12",
        "LOVE 13",
        "LOVE 14",
        "LOVE 15",
        "LOVE 16",
        "LOVE 17",
        "LOVE 18",
        "LOVE 19",
        "LOVE 20",
        "Papyrus Hangout",
        "Undyne Cook-off",
        "Alphys Date",
        "ATK 2",
        "ATK 3",
        "ATK 4",
        "ATK 5",
        "ATK 6",
        "ATK 7",
        "ATK 8",
        "ATK 9",
        "ATK 10",
        "ATK 11",
        "ATK 12",
        "ATK 13",
        "ATK 14",
        "ATK 15",
        "ATK 16",
        "ATK 17",
        "ATK 18",
        "ATK 19",
        "ATK 20",
        "DEF 5",
        "DEF 9",
        "DEF 13",
        "DEF 17",
        "HP 2",
        "HP 3",
        "HP 4",
        "HP 5",
        "HP 6",
        "HP 7",
        "HP 8",
        "HP 9",
        "HP 10",
        "HP 11",
        "HP 12",
        "HP 13",
        "HP 14",
        "HP 15",
        "HP 16",
        "HP 17",
        "HP 18",
        "HP 19",
        "HP 20",
        "Snowman Piece 2",
        "Snowman Piece 3",
        "Ruins Kill 1",
        "Ruins Kill 2",
        "Ruins Kill 3",
        "Ruins Kill 4",
        "Ruins Kill 5",
        "Ruins Kill 6",
        "Ruins Kill 7",
        "Ruins Kill 8",
        "Ruins Kill 9",
        "Ruins Kill 10",
        "Ruins Kill 11",
        "Ruins Kill 12",
        "Ruins Kill 13",
        "Ruins Kill 14",
        "Ruins Kill 15",
        "Ruins Kill 16",
        "Ruins Kill 17",
        "Ruins Kill 18",
        "Ruins Kill 19",
        "Ruins Kill 20",
        "Snowdin Kill 1",
        "Snowdin Kill 2",
        "Snowdin Kill 3",
        "Snowdin Kill 4",
        "Snowdin Kill 5",
        "Snowdin Kill 6",
        "Snowdin Kill 7",
        "Snowdin Kill 8",
        "Snowdin Kill 9",
        "Snowdin Kill 10",
        "Snowdin Kill 11",
        "Snowdin Kill 12",
        "Snowdin Kill 13",
        "Snowdin Kill 14",
        "Snowdin Kill 15",
        "Snowdin Kill 16",
        "Waterfall Kill 1",
        "Waterfall Kill 2",
        "Waterfall Kill 3",
        "Waterfall Kill 4",
        "Waterfall Kill 5",
        "Waterfall Kill 6",
        "Waterfall Kill 7",
        "Waterfall Kill 8",
        "Waterfall Kill 9",
        "Waterfall Kill 10",
        "Waterfall Kill 11",
        "Waterfall Kill 12",
        "Waterfall Kill 13",
        "Waterfall Kill 14",
        "Waterfall Kill 15",
        "Waterfall Kill 16",
        "Waterfall Kill 17",
        "Waterfall Kill 18",
        "Hotland Kill 1",
        "Hotland Kill 2",
        "Hotland Kill 3",
        "Hotland Kill 4",
        "Hotland Kill 5",
        "Hotland Kill 6",
        "Hotland Kill 7",
        "Hotland Kill 8",
        "Hotland Kill 9",
        "Hotland Kill 10",
        "Hotland Kill 11",
        "Hotland Kill 12",
        "Hotland Kill 13",
        "Hotland Kill 14",
        "Hotland Kill 15",
        "Hotland Kill 16",
        "Hotland Kill 17",
        "Hotland Kill 18",
        "Hotland Kill 19",
        "Hotland Kill 20",
        "Hotland Kill 21",
        "Hotland Kill 22",
        "Hotland Kill 23",
        "Hotland Kill 24",
        "Hotland Kill 25",
        "Hotland Kill 26",
        "Hotland Kill 27",
        "Hotland Kill 28",
        "Hotland Kill 29",
        "Hotland Kill 30",
        "Hotland Kill 31",
        "Hotland Kill 32",
        "Hotland Kill 33",
        "Hotland Kill 34",
        "Hotland Kill 35",
        "Hotland Kill 36",
        "Hotland Kill 37",
        "Hotland Kill 38",
        "Hotland Kill 39",
        "Hotland Kill 40",
    },
    "genocide": {
        "Undyne Letter",
        "Sans Hot Dog Sale 1",
        "Sans Hot Cat Sale",
        "Sans Hot Dog Sale 2",
        "Sans Hot Dog Sale 3",
        "Sans Hot Dog Sale 4",
        "Popato Chisps Machine",
        "Nicecream Snowdin",
        "Nicecream Waterfall",
        "Nicecream Punch Card Trade",
        "Punch Card",
        "Stained Apron",
        "Hotel Door Hush Puppy",
        "Papyrus Hangout",
        "Undyne Cook-off",
        "Alphys Date",
    },
    "NoLove": {
        "LOVE 2",
        "LOVE 3",
        "LOVE 4",
        "LOVE 5",
        "LOVE 6",
        "LOVE 7",
        "LOVE 8",
        "LOVE 9",
        "LOVE 10",
        "LOVE 11",
        "LOVE 12",
        "LOVE 13",
        "LOVE 14",
        "LOVE 15",
        "LOVE 16",
        "LOVE 17",
        "LOVE 18",
        "LOVE 19",
        "LOVE 20",
    },
    "NoKills": {
        "Ruins Kill 1",
        "Ruins Kill 2",
        "Ruins Kill 3",
        "Ruins Kill 4",
        "Ruins Kill 5",
        "Ruins Kill 6",
        "Ruins Kill 7",
        "Ruins Kill 8",
        "Ruins Kill 9",
        "Ruins Kill 10",
        "Ruins Kill 11",
        "Ruins Kill 12",
        "Ruins Kill 13",
        "Ruins Kill 14",
        "Ruins Kill 15",
        "Ruins Kill 16",
        "Ruins Kill 17",
        "Ruins Kill 18",
        "Ruins Kill 19",
        "Ruins Kill 20",
        "Snowdin Kill 1",
        "Snowdin Kill 2",
        "Snowdin Kill 3",
        "Snowdin Kill 4",
        "Snowdin Kill 5",
        "Snowdin Kill 6",
        "Snowdin Kill 7",
        "Snowdin Kill 8",
        "Snowdin Kill 9",
        "Snowdin Kill 10",
        "Snowdin Kill 11",
        "Snowdin Kill 12",
        "Snowdin Kill 13",
        "Snowdin Kill 14",
        "Snowdin Kill 15",
        "Snowdin Kill 16",
        "Waterfall Kill 1",
        "Waterfall Kill 2",
        "Waterfall Kill 3",
        "Waterfall Kill 4",
        "Waterfall Kill 5",
        "Waterfall Kill 6",
        "Waterfall Kill 7",
        "Waterfall Kill 8",
        "Waterfall Kill 9",
        "Waterfall Kill 10",
        "Waterfall Kill 11",
        "Waterfall Kill 12",
        "Waterfall Kill 13",
        "Waterfall Kill 14",
        "Waterfall Kill 15",
        "Waterfall Kill 16",
        "Waterfall Kill 17",
        "Waterfall Kill 18",
        "Hotland Kill 1",
        "Hotland Kill 2",
        "Hotland Kill 3",
        "Hotland Kill 4",
        "Hotland Kill 5",
        "Hotland Kill 6",
        "Hotland Kill 7",
        "Hotland Kill 8",
        "Hotland Kill 9",
        "Hotland Kill 10",
        "Hotland Kill 11",
        "Hotland Kill 12",
        "Hotland Kill 13",
        "Hotland Kill 14",
        "Hotland Kill 15",
        "Hotland Kill 16",
        "Hotland Kill 17",
        "Hotland Kill 18",
        "Hotland Kill 19",
        "Hotland Kill 20",
        "Hotland Kill 21",
        "Hotland Kill 22",
        "Hotland Kill 23",
        "Hotland Kill 24",
        "Hotland Kill 25",
        "Hotland Kill 26",
        "Hotland Kill 27",
        "Hotland Kill 28",
        "Hotland Kill 29",
        "Hotland Kill 30",
        "Hotland Kill 31",
        "Hotland Kill 32",
        "Hotland Kill 33",
        "Hotland Kill 34",
        "Hotland Kill 35",
        "Hotland Kill 36",
        "Hotland Kill 37",
        "Hotland Kill 38",
        "Hotland Kill 39",
        "Hotland Kill 40",
    },
    "NoStats": {
        "ATK 2",
        "ATK 3",
        "ATK 4",
        "ATK 5",
        "ATK 6",
        "ATK 7",
        "ATK 8",
        "ATK 9",
        "ATK 10",
        "ATK 11",
        "ATK 12",
        "ATK 13",
        "ATK 14",
        "ATK 15",
        "ATK 16",
        "ATK 17",
        "ATK 18",
        "ATK 19",
        "ATK 20",
        "DEF 5",
        "DEF 9",
        "DEF 13",
        "DEF 17",
        "HP 2",
        "HP 3",
        "HP 4",
        "HP 5",
        "HP 6",
        "HP 7",
        "HP 8",
        "HP 9",
        "HP 10",
        "HP 11",
        "HP 12",
        "HP 13",
        "HP 14",
        "HP 15",
        "HP 16",
        "HP 17",
        "HP 18",
        "HP 19",
        "HP 20",
    },
    "all_routes": {
    }
}
no_spare = set()
for i in range(100):
    no_spare.add("Ruins Spare " + str(i + 1))
    no_spare.add("Snowdin Spare " + str(i + 1))
    no_spare.add("Waterfall Spare " + str(i + 1))
    no_spare.add("Hotland Spare " + str(i + 1))
exclusion_table.__setitem__("NoSpare", no_spare.copy())

events_table = {
}
