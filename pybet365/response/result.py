"""
Facade for `upcoming_events` Delegation

Bet365 API Responses contain 2 common components
Bet365Response object is tasked to parse:
    "success": int
    "results": list

This module provides delegation for `ResultResponse`

The objects are accessible via dot notation or via `.get(..)`
"""

from typing import List, Union

from pybet365.response.base import (
    Bet365Response,
    MetaBase,
    ResultBase
)


class ResultEvent(dict):
    """Result Endpoint `events` array contents access.
    (e.g.)
        {
            "id": "1231251"
            "text": "1' - 1st Goal -   (Estudiantes Rio Cuarto) -"
        }
    """

    def __init__(self, data: dict):
        """Constructor for UpcomingEventsResponse."""
        super(ResultEvent, self).__init__(data)

    @property
    def id(self) -> str:
        """Access for `id`."""
        return self.get("id")

    @property
    def text(self):
        """Access for `text`."""
        return self.get("text")


class Result(ResultBase):
    """
    Subclass of ResultBase with additional fields for `Result` endpoint.

    (e.g.)
    >>> data = {
    ...   "id":"86576599",
    ...   "sport_id":"1",
    ...   "away":{
    ...       "id":"10361085",
    ...       "name":"Chivas Guadalajara Women"
    ...    },
    ...    "scores": {
    ...        "1": {
    ...            "home": "1",
    ...            "away": "2"
    ...        }
    ...    },
    ...    "updated_at": "1581990232"
    ... }

    >>> Result(data).id
    >>> "86576599"

    >>> Result(data).away.id
    >>> "10361085"
    """

    def __init__(self, data: dict):
        """Constructor for Result."""
        super(Result, self).__init__(data)

    @property
    def o_away(self) -> MetaBase:
        """Access for `o_away`."""
        return MetaBase(self.get("o_away"))

    @property
    def timer(self) -> dict:
        """Access for `timer`."""
        return self.get("timer")

    @property
    def scores(self) -> dict:
        """Access for `scores`."""
        return self.get("scores")

    @property
    def stats(self) -> dict:
        """Access for `stats`."""
        return self.get("stats")

    @property
    def extra(self) -> dict:
        """Access for `extra`."""
        return self.get("extra")

    @property
    def events(self) -> Union[List[ResultEvent], None]:
        """Access for `events`."""
        if not self.get("events"):
            return None

        parsed_results = []
        for record in self.get("events"):
            parsed_results.append(ResultEvent(record))

        return parsed_results

    @property
    def has_lineup(self) -> str:
        """Access for `has_lineup`."""
        return self.get("has_lineup")

    @property
    def inplay_created_at(self) -> str:
        """Access for `inplay_created_at`."""
        return self.get("inplay_created_at")

    @property
    def inplay_updated_at(self) -> str:
        """Access for `inplay_updated_at`."""
        return self.get("inplay_updated_at")

    @property
    def confirmed_at(self) -> str:
        """Access for `confirmed_at`."""
        return self.get("confirmed_at")


class ResultResponse(Bet365Response):
    """
    Response Object Facade for Result Endpoint.

    The object wraps the response and exposes dot notation access

    The top level accesses for `upcoming` endpoint are:
        "success": int
        "results": list

    The `results` object is parsed into `Result` facades
    Say you have a parsed response from UpcomingEvents Endpoint
    >>> response_object.results
    >>> [
    ...   {
    ...     "id": "67890",
    ...     "inplay_created_at": "1586461906"
    ...   },
    ... ]

    >>> response_object.results[0].id
    >>> "67890"

    >>> response_object.results[0].inplay_created_at
    >>> "1576465906"
    """

    def __init__(self, data):
        """Constructor for ResultResponse."""
        super(ResultResponse, self).__init__(data)

    @property
    def results(self) -> Union[List[Result], None]:
        """Access for `results`."""
        if not self._results:
            return None

        parsed_results = []
        for record in self._results:
            parsed_results.append(Result(record))

        return parsed_results
