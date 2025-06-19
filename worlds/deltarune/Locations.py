from BaseClasses import Location
import typing


class AdvData(typing.NamedTuple):
    id: typing.Optional[int]
    region: str


class DeltaruneAdvancement(Location):
    game: str = "Deltarune"


advancement_table = {
    "CH1: Glowshard": AdvData(1, "CH1: Castle Town"),
    "CH1: Dark Candy 1": AdvData(2, "CH1: Fields"),
    "CH1: Dark Candy 2": AdvData(3, "CH1: Fields"),
    "CH1: Dark Candy 3": AdvData(4, "CH1: Fields"),
    "CH1: Dark Candy 4": AdvData(5, "CH1: Fields"),
    "CH1: Top Cake": AdvData(6, "CH1: Bake Sale"),
    "CH1: ChocDiamond Bake Sale": AdvData(7, "CH1: Bake Sale"),
    "CH1: HeartsDonut Bake Sale": AdvData(8, "CH1: Bake Sale"),
    "CH1: LancerCookie Bake Sale": AdvData(9, "CH1: Bake Sale"),
    "CH1: Castle Rudinn ChocoDiamond": AdvData(10, "CH1: Card Castle"),
    "CH1: Return Top Cake": AdvData(11, "CH1: Fields"),
    "CH1: Manual": AdvData(12, "CH1: Castle Town"),
    "CH1: Ribbon": AdvData(13, "CH1: Fields"),
    "CH1: Broken Key C": AdvData(14, "CH1: Fields"),
    "CH1: Dancers ReviveMint": AdvData(15, "CH1: Bake Sale"),
    "CH1: Broken Key B": AdvData(16, "CH1: Bake Sale"),
    "CH1: Ragger": AdvData(17, "CH1: Forest"),
    "CH1: Dice Brace": AdvData(18, "CH1: Forest"),
    "CH1: 40 Gold Chest": AdvData(19, "CH1: Bake Sale"),
    "CH1: ClubsSandwich": AdvData(20, "CH1: Card Castle"),
    "CH1: Lancer Paintings ReviveMint": AdvData(21, "CH1: Card Castle"),
    "CH1: Throw Away Manual": AdvData(22, "CH1: Castle Town"),
    "CH1: BrokenCake": AdvData(23, "CH1: Fields"),
    "CH1: Egg": AdvData(24, "CH1: Bake Sale"),
    "CH1: ShadowCrystal": AdvData(25, "CH1: Card Castle"),
    "CH1: DevilsKnife": AdvData(26, "CH1: Card Castle"),
    "CH1: JevilsTail": AdvData(27, "CH1: Card Castle"),
    "CH1: Door Key": AdvData(28, "CH1: Bake Sale"),
    "CH1: Broken Key A": AdvData(29, "CH1: Fields"),
    "CH1: IronShackle": AdvData(30, "CH1: Card Castle"),
    "CH1: Fields Warp Door": AdvData(31, "CH1: Fields"),
    "CH1: Forest Warp Door": AdvData(32, "CH1: Forest"),
    "CH1: Bake Sale Warp Door": AdvData(33, "CH1: Bake Sale"),
    "CH1: Castle Warp Door": AdvData(34, "CH1: Card Castle"),
    "CH2: Noelle Tea": AdvData(35, "CH2: City"),
    "CH2: Kris Tea": AdvData(36, "CH2: City"),
    "CH2: Susie Tea": AdvData(37, "CH2: City"),
    "CH2: Ralsei Tea": AdvData(38, "CH2: City"),
    "CH2: Spincake": AdvData(39, "CH2: Castle Town"),
    "CH2: CD Bagel Box Shop": AdvData(40, "CH2: City"),
    "CH2: Chalk": AdvData(41, "CH2: Castle Town"),
    "CH2: Dog Dollar": AdvData(42, "CH2: Castle Town"),
    "CH1: Seam Shop 1": AdvData(50, "CH1: Fields"),
    "CH1: Seam Shop 2": AdvData(51, "CH1: Fields"),
    "CH1: Seam Shop 3": AdvData(52, "CH1: Fields"),
    "CH1: Seam Shop 4": AdvData(53, "CH1: Fields"),
    "CH1: Rouxls Shop 1": AdvData(60, "CH1: Card Castle"),
    "CH1: Rouxls Shop 2": AdvData(61, "CH1: Card Castle"),
    "CH1: Rouxls Shop 3": AdvData(62, "CH1: Card Castle"),
    "CH1: Rouxls Shop 4": AdvData(63, "CH1: Card Castle"),
}

exclusion_table = {
    "all_routes": {
    }
}

events_table = {
}
