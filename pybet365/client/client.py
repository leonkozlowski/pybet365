"""
Bet365 API Wrapper.

Bet365 Serves as a Client to make requests to Bet365 API
see for documentation: (https://1394697259.gitbook.io/bet365-api/)

Bet365 Exposes 6 Endpoints:
    Result ["GET"]
    InPlay Filter ["GET"]
    InPlay Odds ["GET"]
    PreMatch odds ["GET"]
    InPlay Events ["GET"]
    Upcoming Events ["GET"]

Responses are parsed into Facade Access objects (Base Bet365Response)
"""
from typing import Optional, Union
from urllib.parse import urljoin

import requests

import pybet365.response as facades
from pybet365.response import Bet365Response
from pybet365.client.config import RESPONSE_OBJECT_FACTORY


class Bet365:
    """
    Bet365 API Wrapper.

    Accessible Endpoints:
        Bet365 Result ["GET"] via `result(...)`
        Bet365 InPlay Filter ["GET"] via `in_play_filter(...)`
        Bet365 InPlay Odds ["GET"] via `in_play_odds(...)`
        Bet365 PreMatch odds ["GET"] via `pre_match_odds(...)`
        Bet365 InPlay Events ["GET"] via `in_play_events(...)`
        Bet365 Upcoming Events ["GET"] via `upcoming_events(...)`
    """

    def __init__(self, api_host, api_key):
        """Constructor for Bet365."""
        self.base_url = "https://bet365-sports-odds.p.rapidapi.com/{}/bet365/"
        self.headers = {
            "x-rapidapi-host": api_host,
            "x-rapidapi-key": api_key,
        }

    def _get(
        self, url_extras: str, params: dict, version: str = "v1"
    ) -> Bet365Response:
        """
        Request maker for Bet365.

        NOTE: Internal method to be invoked by direct endpoint requests

        Args:
            url_extras (str): Tail for desired endpoint provided by caller
            params (dict): GET operation params dict
            version (str): API version for `url` provided by caller

        Returns:
            Bet365Response: Response object accessible by dot notation

        Raises:
            `raise_for_status()` for statuses other than `200`
        """
        url = urljoin(self.base_url.format(version), url_extras)

        response = requests.get(
            url=url, headers=self.headers, params=self._prune(params)
        )
        response.raise_for_status()

        try:
            # Using factory pattern we instantiate the Response Object
            delegation = getattr(
                facades, RESPONSE_OBJECT_FACTORY.get(url_extras)
            )

            # Load the desired `.json()` response to ResponseObject
            delegate_object = delegation(response.json())

        except AttributeError:
            # fall back on `.json()` if facade does not exist
            return response.json()

        return delegate_object

    def result(self, event_id: str) -> Bet365Response:
        """
        Caller for `Result` endpoint of Bet365 API.

        Args:
            event_id (str): Sporting event id to get result for

        Returns:
            Bet365Response: Response Object for `result` endpoint
        """
        querystring = {
            "event_id": event_id
        }

        return self._get(url_extras="result", params=querystring)

    def in_play_filter(
        self,
        sport_id: Optional[str] = None,
        league_id: Optional[str] = None
    ) -> Bet365Response:
        """
        Caller for `InPlay Filters` endpoint of Bet365 API.

        Args:
            sport_id (Optional[str]): Identifier for sport type
            league_id (Optional[str]): Identifier for specific league

        Returns:
            Bet365Response: Response Object for `in_play_filter` endpoint
        """
        querystring = {
            "sport_id": sport_id,
            "league_id": league_id
        }

        return self._get(url_extras="inplay_filter", params=querystring)

    def in_play_odds(
        self,
        fi: str,
        raw: Optional[str] = None,
        lineup: Optional[str] = None,
        stats: Optional[str] = None,
    ) -> Bet365Response:
        """
        Caller for `InPlay Odds` endpoint of Bet365 API.

        Args:
            fi (str): FI from Bet365 InPlay
            raw (Optional[str]): option for raw Bet365 body response
            lineup (Optional[str]): lineup info (NOTE: ONLY FOR CRICKET)
            stats (Optional[str]): extra stats info
                (NOTE: ONLY FOR SOCCER, BASKETBALL, CRICKET, BASEBALL, TENNIS)

        Returns:
            Bet365Response: Response Object for `in_play_odds` endpoint
        """
        querystring = {
            "FI": fi,
            "raw": raw,
            "lineup": lineup,
            "stats": stats
        }

        return self._get(url_extras="event", params=querystring)

    def pre_match_odds(
        self, fi: str, raw: Optional[str] = None
    ) -> Bet365Response:
        """
        Caller for `PreMatch Odds` endpoint of Bet365 API.

        Args:
            fi (str): FI from Bet365 InPlay
            raw (Optional[str]): option for raw Bet365 body response

        Returns:
            Bet365Response: Response Object for `pre_match_odds` endpoint
        """
        querystring = {
            "FI": fi,
            "raw": raw
        }

        return self._get(
            url_extras="prematch", params=querystring, version="v2"
        )

    def in_play_events(self, raw: Optional[str] = None) -> Bet365Response:
        """
        Caller for `InPlay Events` endpoint of Bet365 API.

        Args:
            raw (Optional[str]): option for raw Bet365 body response

        Returns:
            Bet365Response: Response Object for `in_play_events` endpoint
        """
        querystring = {
            "raw": raw
        }

        return self._get(url_extras="inplay", params=querystring)

    def upcoming_events(
        self,
        sport_id: str,
        page: Optional[str] = None,
        lng_id: Optional[str] = None,
        day: Optional[str] = None,
        league_id: Optional[str] = None,
    ) -> Bet365Response:
        """
        Caller for `Upcoming Events` endpoint of Bet365 API.

        Args:
            sport_id (str): String identifier for sport type
            page (Optional[str]): Pagination for API Response
                (NOTE: Out of box default is 50)
            lng_id (Optional[str]): Language Id
            day (Optional[str]): Go forward ONLY date to query
                (e.g.) - 20201124
            league_id (Optional[str]): Id for desired league

        Returns:
            Bet365Response: Response Object for `upcoming_events` endpoint
        """
        querystring = {
            "sport_id": sport_id,
            "page": page,
            "LNG_ID": lng_id,
            "day": day,
            "league_id": league_id,
        }

        return self._get(url_extras="upcoming", params=querystring)

    @staticmethod
    def _prune(params: dict) -> Union[dict, None]:
        """
        Cleaner of `params` dictionary for API Request

        If `value` for `key` is `NoneType` this key will be removed

        Args:
            params (dict): `params` dictionary for API request
            (e.g.)
                { "sport_id": "19", "lng_id": None }

        Returns:
            pruned_params (dict): `params` dict without `None` values or keys
            (e.g.)
                { "sport_id": "19" }
        """
        pruned_params = dict((k, v) for k, v in params.items() if v)

        return pruned_params
