from enum import Enum


class Action(Enum):
    """
    This object represents player action.
    """

    FOLD = 0
    CHECK = 1
    CALL = 2
    BET = 3
    RAISE = 4
    ALLIN = 5
