from BaseClasses import Item, ItemClassification
import typing


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: any


class DeltaruneItem(Item):
    game: str = "Deltarune"


item_table = {
    "Dark Candy": ItemData(1, ItemClassification.filler),
    "ReviveMint": ItemData(2, ItemClassification.useful),
    "Glowshard": ItemData(3, ItemClassification.filler),
    "Manual": ItemData(4, ItemClassification.progression),
    "Spincake": ItemData(7, ItemClassification.useful),
    "Darkburger": ItemData(8, ItemClassification.filler),
    "LancerCookie": ItemData(9, ItemClassification.filler),
    "ClubsSandwich": ItemData(11, ItemClassification.filler),
    "HeartsDonut": ItemData(12, ItemClassification.filler),
    "ChocDiamond": ItemData(13, ItemClassification.filler),
    "RouxlsRoux": ItemData(15, ItemClassification.filler),
    "Egg": ItemData(10002, ItemClassification.filler),
    "BrokenCake": ItemData(10003, ItemClassification.progression),
    "Broken Key A": ItemData(10004, ItemClassification.progression),
    "Door Key": ItemData(10005, ItemClassification.progression),
    "Broken Key B": ItemData(10006, ItemClassification.progression),
    "Broken Key C": ItemData(10007, ItemClassification.progression),
    "ShadowCrystal": ItemData(10013, ItemClassification.progression),
    "Fields Key": ItemData(11000, ItemClassification.progression),
    "Bake Sale Key": ItemData(11001, ItemClassification.progression),
    "Forest Key": ItemData(11002, ItemClassification.progression),
    "Castle Key": ItemData(11003, ItemClassification.progression),
    "Top Cake": ItemData(11004, ItemClassification.progression),
    "Amber Card": ItemData(20001, ItemClassification.useful),
    "Dice Brace": ItemData(20002, ItemClassification.useful),
    "White Ribbon": ItemData(20004, ItemClassification.useful),
    "IronShackle": ItemData(20005, ItemClassification.useful),
    "JevilsTail": ItemData(20007, ItemClassification.useful),
    "Spookysword": ItemData(30005, ItemClassification.useful),
    "Brave Ax": ItemData(30006, ItemClassification.useful),
    "DevilsKnife": ItemData(30007, ItemClassification.useful),
    "Ragger": ItemData(30009, ItemClassification.useful),
    "DaintyScarf": ItemData(30010, ItemClassification.useful),
    "40 Gold": ItemData(40040, ItemClassification.filler),
    "Fields Warp": ItemData(50000, ItemClassification.progression),
    "Forest Warp": ItemData(50001, ItemClassification.progression),
    "Bake Sale Warp": ItemData(50002, ItemClassification.progression),
    "Castle Warp": ItemData(50003, ItemClassification.progression),
    "King-Shaped Key Piece": ItemData(70000, ItemClassification.progression),
}

non_key_items = {
    "Glowshard": 1,
    "Spincake": 1,
    "White Ribbon": 1,
    "ReviveMint": 2,
    "Ragger": 1,
    "Dice Brace": 1,
    "40 Gold": 1,
    "ClubsSandwich": 1,
    "Manual": 1,
    "Egg": 1,
    "ShadowCrystal": 1,
    "DevilsKnife": 1,
    "JevilsTail": 1,
    "IronShackle": 1,
    "Amber Card": 2,
    "Brave Ax": 1,
    "DaintyScarf": 1,
    "Spookysword": 1,

}

warp_doors = [
    "Fields Warp",
    "Forest Warp",
    "Bake Sale Warp",
    "Castle Warp",
]

super_boss_rewards = [
    "JevilsTail",
    "DevilsKnife",
    "ShadowCrystal",
]

key_items = {
    "Top Cake": 1,
    "Manual": 1,
    "Broken Key C": 1,
    "Broken Key B": 1,
    "BrokenCake": 1,
    "Door Key": 1,
    "Broken Key A": 1,
    "Fields Warp": 1,
    "Forest Warp": 1,
    "Bake Sale Warp": 1,
    "Castle Warp": 1,
    "Fields Key": 1,
    "Bake Sale Key": 1,
    "Forest Key": 1,
    "Castle Key": 1,

}

junk_weights_all = {
    "Dark Candy": 40,
    "Darkburger": 70,
    "LancerCookie": 50,
    "HeartsDonut": 60,
    "ChocDiamond": 60,
    "RouxlsRoux": 60,
}
junk_weights_all = {item: 500-weight for item, weight in junk_weights_all.items()}