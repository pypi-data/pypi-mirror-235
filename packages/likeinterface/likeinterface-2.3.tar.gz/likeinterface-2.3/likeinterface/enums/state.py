from enum import Enum


class State(Enum):
    """
    This object represents player state in the game.
    """

    INIT = 0
    OUT = 1
    ALIVE = 2
    ALLIN = 3
