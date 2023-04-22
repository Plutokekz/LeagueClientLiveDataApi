"""
provides classes for the game events
"""
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class EventType(Enum):
    """
    Represents all possible game event types
    """

    TurretKilled = "TurretKilled"
    InhibKilled = "InhibKilled"
    FirstBrick = "FirstBrick"
    ChampionKill = "ChampionKill"
    MinionsSpawning = "MinionsSpawning"
    GameStart = "GameStart"
    FirstBlood = "FirstBlood"
    Ace = "Ace"
    HeraldKill = "HeraldKill"
    DragonKill = "DragonKill"
    BaronKill = "BaronKill"
    InhibRespawningSoon = "InhibRespawningSoon"


class Event(BaseModel):
    """
    Represents a game event
    """

    EventID: int
    EventName: EventType
    EventTime: float
    DragonType: Optional[str]
    Assisters: Optional[List[str]]
    KillerName: Optional[str]
    InhibKilled: Optional[str]
    TurretKilled: Optional[str]
    Stolen: Optional[bool]
    AcingTeam: Optional[str]
    Acer: Optional[str]
    InhibRespawningSoon: Optional[str]


class Events(BaseModel):
    """
    Represents a list of game events
    """

    Events: List[Event]
