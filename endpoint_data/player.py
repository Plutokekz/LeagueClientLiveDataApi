"""
provides classes for the player, his scores and items
"""
from typing import List

from pydantic import BaseModel

from endpoint_data.abilities import Abilities
from endpoint_data.champion_stata import ChampionStats
from endpoint_data.runes import Runes, FullRunes
from endpoint_data.summoner_spell import SummonerSpells


class Scores(BaseModel):
    """
    Represents a score of a player
    """

    assists: int
    creepScore: int
    deaths: int
    kills: int
    wardScore: float


class ActivePlayer(BaseModel):
    """
    Represents the current playing player
    """

    abilities: Abilities
    championStats: ChampionStats
    currentGold: float
    fullRunes: FullRunes
    level: int
    summonerName: str


class Item(BaseModel):
    """
    Represents an item
    """

    canUse: bool
    consumable: bool
    count: int
    displayName: str
    itemID: int
    price: int
    rawDescription: str
    rawDisplayName: str
    slot: int


class Items(BaseModel):
    """
    Represents a list of items
    """

    __root__: List[Item]


class Player(BaseModel):
    """
    Represents a player
    """

    championName: str
    isBot: bool
    isDead: bool
    items: List[Item]
    level: int
    position: str
    rawChampionName: str
    respawnTimer: float
    runes: Runes
    scores: Scores
    skinID: int
    summonerName: str
    summonerSpells: SummonerSpells
    team: str


class Players(BaseModel):
    """
    Represents a list of players
    """

    __root__: List[Player]
