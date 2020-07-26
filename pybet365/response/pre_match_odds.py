"""
Facade for `pre_match_odds` Delegation

Bet365 API Responses contain 2 common components
Bet365Response object is tasked to parse:
    "success": int
    "results": list

This module provides delegation for `PreMatchOddsResponse`

The objects are accessible via dot notation or via `.get(..)`
"""

from typing import List, Union

from pybet365.response.base import (
    Bet365Response,
    FiResultBase
)


class PreMatchOddsResponse(Bet365Response):
    """
    Response Object Facade for Result Endpoint.

    The object wraps the response and exposes dot notation access

    The top level accesses for `upcoming` endpoint are:
        "success": int
        "results": list

    The `results` object is parsed into `FiResultBase` facades
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
        """Constructor for PreMatchOddsResponse."""
        super(PreMatchOddsResponse, self).__init__(data)

    @property
    def results(self) -> Union[List[FiResultBase], None]:
        """Access for `events`."""
        if not self._results:
            return None

        parsed_results = []
        for record in self._results:
            parsed_results.append(FiResultBase(record))

        return parsed_results
