"""
provides classes for all game data
"""
from typing import List

from pydantic import BaseModel

from .event import Events
from .game_data import GameData
from .player import ActivePlayer, Player


class AllGameData(BaseModel):
    """
    Represents all the available game data
    """

    activePlayer: ActivePlayer
    allPlayers: List[Player]
    events: Events
    gameData: GameData
