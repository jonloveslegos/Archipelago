from BaseClasses import Item
import typing


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    progression: bool


class UndertaleItem(Item):
    game: str = "Undertale"


item_table = {
    "Progressive Plot": ItemData(77700, True),
    "Monster Candy": ItemData(77001, False),
    "Croquet Roll": ItemData(77002, False),
    "Stick": ItemData(77003, False),
    "Bandage": ItemData(77004, False),
    "Rock Candy": ItemData(77005, False),
    "Pumpkin Rings": ItemData(77006, False),
    "Spider Donut": ItemData(77007, False),
    "Stoic Onion": ItemData(77008, False),
    "Ghost Fruit": ItemData(77009, False),
    "Spider Cider": ItemData(77010, False),
    "Butterscotch Pie": ItemData(77011, False),
    "Faded Ribbon": ItemData(77012, False),
    "Toy Knife": ItemData(77013, False),
    "Tough Glove": ItemData(77014, False),
    "Manly Bandanna": ItemData(77015, False),
    "Snowman Piece": ItemData(77016, False),
    "Nice Cream": ItemData(77017, False),
    "Puppydough Icecream": ItemData(77018, False),
    "Bisicle": ItemData(77019, False),
    "Unisicle": ItemData(77020, False),
    "Cinnamon Bun": ItemData(77021, False),
    "Temmie Flakes": ItemData(77022, False),
    "Abandoned Quiche": ItemData(77023, False),
    "Old Tutu": ItemData(77024, False),
    "Ballet Shoes": ItemData(77025, False),
    "Punch Card": ItemData(77026, True),
    "Annoying Dog": ItemData(77027, False),
    "Dog Salad": ItemData(77028, False),
    "Dog Residue": ItemData(77029, False),
    "Astronaut Food": ItemData(77035, False),
    "Instant Noodles": ItemData(77036, False),
    "Crab Apple": ItemData(77037, False),
    "Hot Dog...?": ItemData(77038, True),
    "Hot Cat": ItemData(77039, False),
    "Glamburger": ItemData(77040, False),
    "Sea Tea": ItemData(77041, False),
    "Starfait": ItemData(77042, False),
    "Legendary Hero": ItemData(77043, False),
    "Cloudy Glasses": ItemData(77044, False),
    "Torn Notebook": ItemData(77045, False),
    "Stained Apron": ItemData(77046, False),
    "Burnt Pan": ItemData(77047, False),
    "Cowboy Hat": ItemData(77048, False),
    "Empty Gun": ItemData(77049, False),
    "Heart Locket": ItemData(77050, False),
    "Worn Dagger": ItemData(77051, False),
    "Real Knife": ItemData(77052, False),
    "The Locket": ItemData(77053, False),
    "Bad Memory": ItemData(77054, False),
    "Dream": ItemData(77055, False),
    "Undyne's Letter": ItemData(77056, False),
    "Undyne Letter EX": ItemData(77057, True),
    "Popato Chisps": ItemData(77058, False),
    "Junk Food": ItemData(77059, False),
    "Mystery Key": ItemData(77060, False),
    "Face Steak": ItemData(77061, False),
    "Hush Puppy": ItemData(77062, False),
    "Snail Pie": ItemData(77063, False),
    "temy armor": ItemData(77064, False),
    "Goat Plush": ItemData(77777, True),
    "Snow Shovel": ItemData(77778, True),
    "Complete Skeleton": ItemData(77779, True),
    "Fish": ItemData(77780, True),
    "Heat Suit": ItemData(77781, True),
    "DT Extractor": ItemData(77782, True),
    "Cooking Set": ItemData(77783, True),
    "Microphone": ItemData(77784, True),
    "Bridge Tools": ItemData(77785, True),
    "Mettaton Plush": ItemData(77786, True),
    "Determination": ItemData(77787, True),
    "LOVE": ItemData(77788, True),
    "Soul Piece": ItemData(77000, True),
    "100G": ItemData(77999, False),
    "1000G": ItemData(77998, False),
    "10000G": ItemData(77997, False),
    "ATK Up": ItemData(77065, False),
    "DEF Up": ItemData(77066, False),
    "HP Up": ItemData(77067, False),
    "Undyne Date": ItemData(None, True),
    "Alphys Date": ItemData(None, True),
    "Papyrus Date": ItemData(None, True),
}

non_key_items = {
    "Butterscotch Pie": 1,
    "100G": 4,
    "1000G": 3,
    "10000G": 1,
    "Face Steak": 1,
    "Snowman Piece": 1,
    "Instant Noodles": 1,
    "Astronaut Food": 2,
    "Hot Cat": 1,
    "Abandoned Quiche": 1,
    "Monster Candy": 4,
    "ATK Up": 19,
    "DEF Up": 4,
    "HP Up": 19,
}

required_armor = {
    "Cloudy Glasses": 1,
    "Torn Notebook": 1,
    "Tough Glove": 1,
    "Manly Bandanna": 1,
    "Old Tutu": 1,
    "Ballet Shoes": 1,
    "Burnt Pan": 1,
    "Stained Apron": 1,
    "Worn Dagger": 1,
    "Heart Locket": 1,
    "Faded Ribbon": 1,
    "Toy Knife": 1,
    "Cowboy Hat": 1,
    "Empty Gun": 1,
}

plot_items = {
    "Goat Plush": 1,
    "Snow Shovel": 1,
    "Complete Skeleton": 1,
    "Fish": 1,
    "Heat Suit": 1,
    "DT Extractor": 1,
    "Cooking Set": 1,
    "Microphone": 1,
    "Bridge Tools": 1,
    "Mettaton Plush": 1,
}

key_items = {
    "Goat Plush": 1,
    "Snow Shovel": 1,
    "Complete Skeleton": 1,
    "Fish": 1,
    "Heat Suit": 1,
    "DT Extractor": 1,
    "Cooking Set": 1,
    "Microphone": 1,
    "Bridge Tools": 1,
    "Mettaton Plush": 1,
    "Punch Card": 3,
    "Hot Dog...?": 1,
    "LOVE": 19,
}

junk_weights_all = {
    "Bisicle": 12,
    "Legendary Hero": 8,
    "Glamburger": 10,
    "Crab Apple": 12,
    "Sea Tea": 12,
    "Nice Cream": 10,
    "Spider Donut": 10,
    "Popato Chisps": 12,
    "Junk Food": 12,
    "Temmie Flakes": 10,
    "Spider Cider": 8,
    "Hot Dog...?": 10,
    "Cinnamon Bun": 10,
    "Starfait": 12,
    "Punch Card": 8,
}

junk_weights_neutral = {
    "Bisicle": 12,
    "Legendary Hero": 8,
    "Glamburger": 10,
    "Crab Apple": 12,
    "Sea Tea": 12,
    "Nice Cream": 10,
    "Spider Donut": 10,
    "Junk Food": 12,
    "Temmie Flakes": 10,
    "Spider Cider": 8,
    "Cinnamon Bun": 10,
    "Starfait": 12,
    "Punch Card": 8,
}

junk_weights_pacifist = {
    "Bisicle": 12,
    "Legendary Hero": 8,
    "Glamburger": 10,
    "Crab Apple": 12,
    "Sea Tea": 12,
    "Nice Cream": 10,
    "Spider Donut": 10,
    "Popato Chisps": 12,
    "Junk Food": 12,
    "Temmie Flakes": 10,
    "Spider Cider": 8,
    "Hot Dog...?": 10,
    "Cinnamon Bun": 10,
    "Starfait": 12,
    "Punch Card": 8,
}

junk_weights_genocide = {
    "Bisicle": 12,
    "Legendary Hero": 8,
    "Glamburger": 10,
    "Crab Apple": 12,
    "Sea Tea": 12,
    "Nice Cream": 10,
    "Spider Donut": 10,
    "Junk Food": 12,
    "Temmie Flakes": 10,
    "Spider Cider": 8,
    "Cinnamon Bun": 10,
    "Starfait": 12,
}

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}
