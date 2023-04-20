"""
provides classes for all game data
"""
from typing import List

from pydantic import BaseModel

from endpoint_data.event import Events
from endpoint_data.game_data import GameData
from endpoint_data.player import ActivePlayer, Player


class AllGameData(BaseModel):
    """
    Represents all the available game data
    """

    activePlayer: ActivePlayer
    allPlayers: List[Player]
    events: Events
    gameData: GameData
