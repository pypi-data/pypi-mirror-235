from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from likeinterface.methods.base import Method, Request
from likeinterface.types import Cards

if TYPE_CHECKING:
    from likeinterface.interface import Interface


class SetNextGame(Method[bool]):
    """
    Use this method to set next game.

    Parameters
      Name            | Type           | Required | Description

      1. access       | String         | Yes      | Game unique ID
      2. cards        | :class:`Cards` | No       | Game cards

    Result
      :class:`bool`
    """

    __name__ = "like/setNextGame"
    __returning__ = bool

    access: str
    cards: Optional[Cards] = None

    def request(self, interface: Interface) -> None:
        return Request(method=self.__name__, data=self.model_dump())
