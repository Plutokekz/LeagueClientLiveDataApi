"""
provides classes for the game data
"""
from pydantic import BaseModel


class GameData(BaseModel):
    """
    Represents the current data of a game
    """

    gameMode: str
    gameTime: float
    mapName: str
    mapNumber: int
    mapTerrain: str
