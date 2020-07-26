"""
Facade for `in_play_events` Delegation

Bet365 API Responses contain 2 common components
Bet365Response object is tasked to parse:
    "success": int
    "results": list

This module provides delegation for `InPlayEventsResponse`

The objects are accessible via dot notation or via `.get(..)`
"""

from typing import List, Union

from pybet365.response.base import (
    Bet365Response,
    StatsBase
)


class InPlayResult(dict):
    """Result Endpoint `results` array contents access.
    (e.g.)
        {
            "type": "CL",
            ...
            "CD": "1"
        }
    """

    def __init__(self, data: dict):
        """Constructor for InPlayResult."""
        super(InPlayResult, self).__init__(data)

    @property
    def type(self) -> str:
        """Access for `type`."""
        return self.get("type")


class InPlayEventsResponse(Bet365Response):
    """
    Response Object Facade for InPlay Events Endpoint.

    The object wraps the response and exposes dot notation access

    The top level accesses for `inplay` endpoint are:
        "success": int
        "results": list

    The `results` object is parsed into `InPlayResult` facades
    Say you have a parsed response from InPlayEvents Endpoint
    >>> response_object.results
    >>> [
    ...     {
    ...         "type":"CL",
    ...         "CD":"1",
    ...         "FF":"",
    ...         "ID":"1",
    ...         "IT":"OV_1_1_9",
    ...         "NA":"Soccer",
    ...         "OR":"0",
    ...         "PC":"3"
    ...        },
    ... ]

    >>> response_object.results[0].type
    >>> "67890"
    """

    def __init__(self, data):
        """Constructor for InPlayEventsResponse."""
        super(InPlayEventsResponse, self).__init__(data)
        self.stats = StatsBase(data)

    @property
    def results(self) -> Union[List[InPlayResult], None]:
        """Access for `results`."""
        if not self._results:
            return None

        parsed_results = []
        for record in self._results:
            parsed_results.append(InPlayResult(record))

        return parsed_results
