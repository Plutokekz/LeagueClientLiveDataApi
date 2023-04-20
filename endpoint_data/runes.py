"""
provides the classes for runes and rune sets
"""
from typing import Union, List

from pydantic import BaseModel


class Rune(BaseModel):
    """
    Represents a Rune
    """

    displayName: str
    id: int
    rawDescription: str
    rawDisplayName: str


class StatRune(BaseModel):
    """
    Represents a stat rune
    """

    id: int
    rawDescription: str


class FullRunes(BaseModel):
    """
    Represents a full set of runes
    """

    generalRunes: List[Union[Rune]]
    keystone: Rune
    primaryRuneTree: Rune
    secondaryRuneTree: Rune
    statRunes: List[Union[StatRune]]


class Runes(BaseModel):
    """
    Represents a basic set of runes
    """

    keystone: Rune
    primaryRuneTree: Rune
    secondaryRuneTree: Rune
