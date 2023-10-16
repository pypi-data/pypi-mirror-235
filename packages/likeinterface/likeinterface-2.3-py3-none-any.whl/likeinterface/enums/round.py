from enum import Enum


class Round(Enum):
    """
    This object represents game round.
    """

    PREFLOP = 0
    FLOP = 1
    TURN = 2
    RIVER = 3
    SHOWDOWN = 4
