# League Client Live Data Api
An async api wrapper for the [game client api](https://developer.riotgames.com/docs/lol#game-client-api) from league of legends.
For every endpoint there is a pydantic BaseModel that represents the data from the response of the request. 
# Setup
## Installation

```bash
git clone https://github.com/Plutokekz/LeagueClientLiveDataApi.git
poetry install
```
## Usage
Get the events from your current game
````python
from pathlib import Path

from live_client_data import LeagueClientLiveDataApi


if __name__ == "__main__":
    config_file = Path("config.yaml")
    api = LeagueClientLiveDataApi()
    async def main():
        while True:
            data = await api.event_data()
            print(data)
    api.loop.run_until_complete(main())
````
## Config

the config file contains currently 2 entries on for the api endpoint and one for the 
ssl certificate of riot games. You can download the file from [here](https://developer.riotgames.com/docs/lol#game-client-api). 

````yaml
cert_file: "riotgames.pem"
url: "https://127.0.0.1:2999/liveclientdata"
````
