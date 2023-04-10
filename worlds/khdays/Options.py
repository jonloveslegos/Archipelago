import typing
from Options import Option, Range, Choice


class StartingCharacter(Choice):
    """What character you have unlocked from the start"""
    option_Roxas = 0
    option_Axel = 1
    option_Xigbar = 2
    option_Saix = 3
    option_Xaldin = 4
    option_Sora = 5
    option_Demyx = 6
    option_Larxene = 7
    option_Lexaeus = 8
    option_Luxord = 9
    option_Marluxia = 10
    option_Riku = 11
    option_Vexen = 12
    option_Xemnas = 13
    option_Xion = 14
    option_Zexion = 15
    option_Mickey = 16
    option_Donald = 17
    option_Goofy = 18
    option_Dual_Wield_Roxas = 19
    default = 0


class DayRequirement(Range):
    """What day do you need to start to win the game?"""
    range_start = 8
    range_end = 358
    default = 358


khdays_options: typing.Dict[str, type(Option)] = {
    "DayRequirement": DayRequirement,
    "StartingCharacter": StartingCharacter,
}
