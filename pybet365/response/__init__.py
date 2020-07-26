"""Response namespace."""

from .base import (
    Bet365Response,
    FiResultBase,
    MetaBase,
    PagerBase
)

from .in_play_events import (
    InPlayEventsResponse,
    InPlayResult
)

from .pre_match_odds import PreMatchOddsResponse

from .result import (
    Result,
    ResultEvent,
    ResultResponse
)

from .upcoming_events import (
    UpcomingEvent,
    UpcomingEventsResponse
)

__all__ = [
    "Bet365Response",
    "FiResultBase",
    "InPlayEventsResponse",
    "InPlayResult",
    "MetaBase",
    "PagerBase",
    "PreMatchOddsResponse",
    "Result",
    "ResultEvent",
    "ResultResponse",
    "UpcomingEvent",
    "UpcomingEventsResponse"
]
