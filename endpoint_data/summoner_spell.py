"""
provides the summoner spell and spells class
"""
from pydantic import BaseModel


class SummonerSpell(BaseModel):
    """
    Represents a summoner spell
    """

    displayName: str
    rawDescription: str
    rawDisplayName: str


class SummonerSpells(BaseModel):
    """
    Represents both summoner spells
    """

    summonerSpellOne: SummonerSpell
    summonerSpellTwo: SummonerSpell
