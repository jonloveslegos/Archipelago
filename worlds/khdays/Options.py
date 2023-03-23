import typing
from Options import Option, Range


class DayRequirement(Range):
    """What day do you need to start to win the game?"""
    range_start = 8
    range_end = 358
    default = 358


khdays_options: typing.Dict[str, type(Option)] = {
    "DayRequirement": DayRequirement,
}
