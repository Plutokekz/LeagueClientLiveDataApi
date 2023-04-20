"""
Provides config dataclass
"""
from pydantic.dataclasses import dataclass


@dataclass
class Config:
    """
    Represents config file
    """

    cert_file: str
    url: str
