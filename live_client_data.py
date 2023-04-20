"""
provides the live-client-data api wrapper
"""
import asyncio
import logging
from asyncio import AbstractEventLoop
from pathlib import Path
from typing import Optional

import httpx

import utils
from endpoint_data.abilities import Abilities
from endpoint_data.all_game_data import AllGameData
from endpoint_data.event import Events
from endpoint_data.game_data import GameData
from endpoint_data.player import ActivePlayer, Scores, Items, Players
from endpoint_data.runes import FullRunes, Runes
from endpoint_data.summoner_spell import SummonerSpells

logger = logging.getLogger(__name__)


class NotA200StatusCodeException(Exception):
    """
    If the status_code from the response is not 200 this exception is raised
    """


class LeagueClientLiveDataApi:
    """
    The main class to accesses the live data api
    """

    client: httpx.AsyncClient
    loop: Optional[AbstractEventLoop]
    url: str

    def __init__(
        self, path: Path = Path("config.yaml"), loop: Optional[AbstractEventLoop] = None
    ):
        config = utils.load_config(path)
        self.client = httpx.AsyncClient(verify=config.cert_file)
        self.loop = loop if loop is not None else asyncio.new_event_loop()
        self.url = config.url

    async def _request(self, url):
        logger.debug("sending request to: %s", url)
        response = await self.client.get(url)
        if response.status_code != 200:
            raise NotA200StatusCodeException(
                f"{response.status_code}, {response.content}"
            )
        logger.debug("response: %s", response.json())
        return response.json()

    async def all_game_data(self) -> AllGameData:
        """
        request all the game data
        :return: all the game data
        """
        return AllGameData(**await self._request(f"{self.url}/allgamedata"))

    async def active_player(self) -> ActivePlayer:
        """
        request the current player
        :return: the activ player
        """
        return ActivePlayer(**await self._request(f"{self.url}/activeplayer"))

    async def active_player_name(self) -> str:
        """
        request the activ player name
        :return: the player name
        """
        return str(await self._request(f"{self.url}/activeplayername"))

    async def active_player_abilities(self) -> Abilities:
        """
        request the abilities from the activ player
        :return: champion abilities
        """
        return Abilities(**await self._request(f"{self.url}/activeplayerabilities"))

    async def active_player_runes(self) -> FullRunes:
        """
        request the runes for the activ player
        :return: a full rune set
        """
        return FullRunes(**await self._request(f"{self.url}/activeplayerrunes"))

    async def player_list(self) -> Players:
        """
        request the list of playing player in the game
        :return: a list of players
        """
        return Players(__root__=await self._request(f"{self.url}/playerlist"))

    async def player_scores(self, summoner_name) -> Scores:
        """
        request the score for a player
        :param summoner_name: name of a player from the player list
        :return: the score of the player
        """
        return Scores(
            **await self._request(
                f"{self.url}/playerscores?summonerName={summoner_name}"
            )
        )

    async def player_summoner_spells(self, summoner_name) -> SummonerSpells:
        """
        request the summoners spells for a player
        :param summoner_name: name of a player from the player list
        :return: summoner spells
        """
        return SummonerSpells(
            **await self._request(
                f"{self.url}/playersummonerspells?summonerName={summoner_name}"
            )
        )

    async def player_main_runes(self, summoner_name) -> Runes:
        """
        request the runes of a player
        :param summoner_name: name of a player from the player list
        :return: runes
        """
        return Runes(
            **await self._request(
                f"{self.url}/playermainrunes?summonerName={summoner_name}"
            )
        )

    async def player_items(self, summoner_name) -> Items:
        """
        request the items of a player
        :param summoner_name: name of a player from the player list
        :return: a list of items
        """
        return Items(
            **await self._request(
                f"{self.url}/playeritems?summonerName={summoner_name}"
            )
        )

    async def event_data(self) -> Events:
        """
        request the game events
        :return: a list of events
        """
        return Events(**await self._request(f"{self.url}/eventdata"))

    async def game_stats(self) -> GameData:
        """
        request the game data
        :return: game data
        """
        return GameData(**await self._request(f"{self.url}/gamestats"))
