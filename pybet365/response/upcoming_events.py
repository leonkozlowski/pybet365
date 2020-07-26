"""
Facade for `upcoming_events` Delegation

Bet365 API Responses contain 2 common components
Bet365Response object is tasked to parse:
    "success": int
    "results": list

This module provides delegation for `UpcomingEventsResponse`

The objects are accessible via dot notation or via `.get(..)`
"""

from typing import List, Union

from pybet365.response.base import (
    Bet365Response,
    PagerBase,
    ResultBase
)


class UpcomingEvent(ResultBase):
    """
    Component for dot notation access of `results` from UpcomingEvent Endpoint.

    (e.g.)
    >>> data = {
    ...   "id":"86576599",
    ...   "sport_id":"1",
    ...   "away":{
    ...       "id":"10361085",
    ...       "name":"Chivas Guadalajara Women"
    ...    },
    ...    "ss": None,
    ...    "our_event_id":"2130836",
    ...    "updated_at":"1581990232"
    ... }

    >>> UpcomingEvent(data).id
    >>> "86576599"

    >>> UpcomingEvent(data).away.id
    >>> "10361085"
    """

    def __init__(self, data: dict):
        """Constructor for UpcomingEvent."""
        super(UpcomingEvent, self).__init__(data)

    @property
    def our_event_id(self) -> str:
        """Access for `our_event_id`."""
        return self.get("our_event_id")

    @property
    def updated_at(self) -> str:
        """Access for `updated_at`."""
        return self.get("updated_at")


class UpcomingEventsResponse(Bet365Response):
    """
    Response Object Facade for UpcomingEvents Endpoint.

    The object wraps the response and exposes dot notation access

    The top level accesses for `upcoming` endpoint are:
        "success": int
        "pager": dict
        "results": list

    The `results` object is parsed into `UpcomingEvent` facades
    Say you have a parsed response from UpcomingEvents Endpoint
    >>> response_object.results
    >>> [
    ...   {
    ...     "id": "12345",
    ...     "our_event_id":"2294461",
    ...     "updated_at": "1586461906"
    ...   },
    ... ]

    >>> response_object.results[0].our_event_id
    >>> "2294461"

    >>> response_object.results[0].updated_at
    >>> "1586461906"
    """

    def __init__(self, data):
        """Constructor for UpcomingEventsResponse."""
        super(UpcomingEventsResponse, self).__init__(data)
        self.pager = PagerBase(data.get("pager"))

    @property
    def results(self) -> Union[List[UpcomingEvent], None]:
        """Access for `results`."""
        if not self._results:
            return None

        parsed_results = []
        for record in self._results:
            parsed_results.append(UpcomingEvent(record))

        return parsed_results
