from BaseClasses import Item, ItemClassification
import typing


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: any


class DeltaruneItem(Item):
    game: str = "Deltarune"


item_table = {
    "Glowshard": ItemData(10003, ItemClassification.useful),
    "Dark Candy": ItemData(10001, ItemClassification.useful),
    "TopCake": ItemData(10006, ItemClassification.progression),
}

non_key_items = {
    "Dark Candy": 4,
    "Glowshard": 1,
    "TopCake": 1,
}

key_items = {
}

junk_weights_all = {
}
