"""
provides classes for the champion stats
"""
from typing import Optional

from pydantic import BaseModel


class ChampionStats(BaseModel):
    """
    Represent the champion stats
    """

    abilityPower: float
    armor: float
    armorPenetrationFlat: float
    armorPenetrationPercent: float
    attackDamage: float
    attackRange: float
    attackSpeed: float
    bonusArmorPenetrationPercent: float
    bonusMagicPenetrationPercent: float
    cooldownReduction: Optional[float]
    critChance: float
    critDamage: float
    currentHealth: float
    healthRegenRate: float
    lifeSteal: float
    magicLethality: float
    magicPenetrationFlat: float
    magicPenetrationPercent: float
    magicResist: float
    maxHealth: float
    moveSpeed: float
    physicalLethality: float
    resourceMax: float
    resourceRegenRate: float
    resourceType: str
    resourceValue: float
    spellVamp: float
    tenacity: float
