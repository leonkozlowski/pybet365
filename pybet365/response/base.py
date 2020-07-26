"""
Facade `BaseResponse Object` Delegation

Bet365 API Responses contain 2 common components
Bet365Response object is tasked to parse:
    "success": int
    "results": list

Further delegation for facade access to responses are subclassed

`InPlayFilterResponse`
`InPlayOddsResponse`
`PreMatchOddsResponse`
`PreMatchOddsResponse`
`InPlayEventsResponse`
`UpcomingEventsResponse`

The objects are accessible via dot notation or via `.get(..)`
"""
from typing import Union


class Bet365Response(dict):
    """Base ResponseObject creator for Bet365 API Response."""

    def __init__(self, data: dict):
        """Constructor for Bet365Response."""
        super(Bet365Response, self).__init__(data)

    @property
    def success(self) -> int:
        """Access for `success`."""
        return self.get("success")

    @property
    def _results(self) -> Union[list, None]:
        """Access for `results`."""
        # NOTE: This is overloaded hence the `_*`
        return self.get("results")


class FiResultBase(dict):
    """
    Component for dot notation for "FI" based objects.

    (e.g.)
    >>> data = {
    ...     "FI":"87967884",
    ...     "event_id":"12312412",
    ...     "main": {...}
    ... }

    >>> FiResultBase(data).fi
    >>> "87967884"
    """

    def __init__(self, data: dict):
        """Constructor for FiResultBase."""
        super(FiResultBase, self).__init__(data)

    @property
    def fi(self) -> str:
        """Access for `fi`."""
        return self.get("FI")

    @property
    def event_id(self) -> str:
        """Access for `event_id`."""
        return self.get("event_id")

    @property
    def main(self) -> dict:
        """Access for `main`."""
        return self.get("main")


class MetaBase(dict):
    """
    Component for dot notation for objects with "id" and "name".

    (e.g.)
    >>> data = {
    ...     "id":"10037409",
    ...     "name":"Mexico Liga MX Femenil"
    ... }

    >>> MetaBase(data).id
    >>> "10037409"
    """

    def __init__(self, data: dict):
        """Constructor for MetaBase."""
        super(MetaBase, self).__init__(data)

    @property
    def id(self) -> str:
        """Access for `id`."""
        return self.get("id")

    @property
    def name(self) -> str:
        """Access for `name`."""
        return self.get("name")

    @property
    def image_id(self) -> str:
        """Access for `image_id`."""
        return self.get("image_id")

    @property
    def cc(self) -> str:
        """Access for `cc`."""
        return self.get("cc")


class PagerBase(dict):
    """
    Component for dot notation access of `pager` object in API Response.
    (e.g.)
    >>> data = {
    ...     "page": 1,
    ...     "per_page": 50,
    ...     "total": 730
    ... }

    >>> PagerBase(data).page
    >>> 1

    >>> PagerBase(data).per_page
    >>> 50
    """

    def __init__(self, data: dict):
        """Constructor for PagerBase."""
        super(PagerBase, self).__init__(data)

    @property
    def page(self) -> Union[int, None]:
        """Access for `page`."""
        return self.get("page")

    @property
    def per_page(self) -> Union[int, None]:
        """Access for `per_page`."""
        return self.get("per_page")

    @property
    def total(self) -> Union[int, None]:
        """Access for `total`."""
        return self.get("total")


class ResultBase(dict):
    """
    Component for dot notation access of `results` from any Endpoint.

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

    >>> ResultBase(data).id
    >>> "86576599"

    >>> ResultBase(data).away.id
    >>> "10361085"
    """

    def __init__(self, data: dict):
        """Constructor for ResultBase."""
        super(ResultBase, self).__init__(data)

    @property
    def id(self) -> str:
        """Access for `id`."""
        return self.get("id")

    @property
    def sport_id(self) -> str:
        """Access for `sport_id`."""
        return self.get("sport_id")

    @property
    def time(self) -> str:
        """Access for `time`."""
        return self.get("time")

    @property
    def time_status(self) -> str:
        """Access for `time_status`."""
        return self.get("time_status")

    @property
    def league(self) -> MetaBase:
        """Access for `league`."""
        return MetaBase(self.get("league"))

    @property
    def home(self) -> MetaBase:
        """Access for `home`."""
        return MetaBase(self.get("home"))

    @property
    def away(self) -> MetaBase:
        """Access for `away`."""
        return MetaBase(self.get("away"))

    @property
    def ss(self) -> str:
        """Access for `ss`."""
        return self.get("ss")


class StatsBase(dict):
    """
    Component for dot notation access of `stats` from any Endpoint.

    (e.g.)
    >>> data = {
    ...     "event_id":"2130389",
    ...     "update_at":"1581990853",
    ...     "update_dt":"2020-02-18 01:54:13"
    ... }

    >>> StatsBase(data).event_id
    >>> "2130389"

    >>> StatsBase(data).update_at
    >>> "1581990853"
    """

    def __init__(self, data: dict):
        """Constructor for StatsBase."""
        super(StatsBase, self).__init__(data)

    @property
    def event_id(self) -> str:
        """Access for `event_id`."""
        return self.get("event_id")

    @property
    def update_at(self) -> str:
        """Access for `update_at`."""
        return self.get("update_at")

    @property
    def update_dt(self) -> str:
        """Access for `update_dt`."""
        return self.get("update_dt")
