from __future__ import annotations

from likeinterface.enums import Action as AAction
from likeinterface.enums import Position
from likeinterface.types.base import LikeObject


class Action(LikeObject):
    """
    Player action.
    """

    amount: int
    """Action amount chips."""
    action: AAction
    """Selected action."""
    position: Position
    """Player position (equals to game players index)."""
