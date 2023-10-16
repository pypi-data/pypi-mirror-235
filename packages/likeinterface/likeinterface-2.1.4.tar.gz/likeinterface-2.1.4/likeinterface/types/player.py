from __future__ import annotations

from likeinterface.enums import State
from likeinterface.types.base import LikeObject


class Player(LikeObject):
    id: int
    """Some player ID."""
    is_left: bool
    """Is player left from game."""
    stack: int
    """Current player stack."""
    behind: int
    """Stacksize in the game."""
    front: int
    """Posted chips in the game."""
    round_bet: int
    """Posted chips for round."""
    state: State
    """Player state (init, out, alive, allin)."""
