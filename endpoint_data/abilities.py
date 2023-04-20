"""
provides classes for the champion abilities
"""
from pydantic import BaseModel


class Ability(BaseModel):
    """
    Represents an ability
    """

    abilityLevel: int
    displayName: str
    id: str
    rawDescription: str
    rawDisplayName: str


class Passive(BaseModel):
    """
    Represents a passiv ability
    """

    displayName: str
    id: str
    rawDescription: str
    rawDisplayName: str


class Abilities(BaseModel):
    """
    Represents all abilities of a champion
    """

    E: Ability
    Passive: Passive
    Q: Ability
    R: Ability
    W: Ability
