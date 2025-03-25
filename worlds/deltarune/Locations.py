from BaseClasses import Location
import typing


class AdvData(typing.NamedTuple):
    id: typing.Optional[int]
    region: str


class DeltaruneAdvancement(Location):
    game: str = "Deltarune"


advancement_table = {
    "CH1: Glowshard": AdvData(1, "???"),
    "CH1: Candy Tree 1 Item 1": AdvData(2, "???"),
    "CH1: Candy Tree 1 Item 2": AdvData(3, "???"),
    "CH1: Candy Tree 2 Item 1": AdvData(4, "???"),
    "CH1: Candy Tree 2 Item 2": AdvData(5, "???"),
    "CH1: Fix Cake": AdvData(6, "???"),
}

exclusion_table = {
}

events_table = {
}
