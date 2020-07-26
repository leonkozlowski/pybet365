"""Unit tests for `betfund_bet365.client` modules."""
from unittest import TestCase

from pybet365.response.base import (
    Bet365Response,
    MetaBase,
    PagerBase,
    ResultBase,
    StatsBase,
)

from tests.utils import load_json


class TestBet365Response(TestCase):
    """Unit tests for Bet365Response Facade."""

    def setUp(self) -> None:
        """Instantiate Bet365Response."""

        self.test_client = Bet365Response(
            load_json("testData/upcoming_events_table_tennis.json")
        )

    def test_success(self):
        """Unit test for `Bet365Response.success`."""
        result = self.test_client.success

        assert result == 1

    def test_results(self):
        """Unit test for `Bet365Response._results`."""
        result = self.test_client._results

        assert isinstance(result, list)
        assert len(result) == 1


class TestMetaBase(TestCase):
    """Unit tests for MetaBase Facade."""

    def setUp(self) -> None:
        """Instantiate MetaBase."""
        mock_meta = {
            "id": "10423098",
            "name": "Evgenii Kryuchkov",
            "image_id": "1238012",
            "cc": "Russia",
        }

        self.test_client = MetaBase(mock_meta)

    def test_id(self):
        """Unit test for `MetaBase.id`."""
        result = self.test_client.id

        assert result == "10423098"

    def test_name(self):
        """Unit test for `MetaBase.name`."""
        result = self.test_client.name

        assert result == "Evgenii Kryuchkov"

    def test_image_id(self):
        """Unit test for `MetaBase.name`."""
        result = self.test_client.image_id

        assert result == "1238012"

    def test_cc(self):
        """Unit test for `MetaBase.name`."""
        result = self.test_client.cc

        assert result == "Russia"


class TestPagerBese(TestCase):
    """Unit tests for PagerBase Facade."""

    def setUp(self) -> None:
        """Instantiate MetaBase."""
        mock_pager = {
            "page": 1,
            "per_page": 50,
            "total": 730
        }

        self.test_client = PagerBase(mock_pager)

    def test_page(self):
        """Unit test for `PagerBase.page`."""
        result = self.test_client.page

        assert result == 1

    def test_per_page(self):
        """Unit test for `PagerBase.page`."""
        result = self.test_client.per_page

        assert result == 50

    def test_total(self):
        """Unit test for `PagerBase.total`."""
        result = self.test_client.total

        assert result == 730


class TestResultBase(TestCase):
    """Unit tests for ResultBase Facade."""

    def setUp(self) -> None:
        """Instantiate ResultBase."""
        mock_result = {
            "id": "86576599",
            "sport_id": "1",
            "time": "15093049123",
            "time_status": "12312",
            "league": {
                "id": "10361086",
                "name": "Chivas Guadalajara"
            },
            "away": {
                "id": "10361085",
                "name": "Chivas Guadalajara Women"
            },
            "home": {
                "id": "10361086",
                "name": "Chivas Guadalajara Men"
            },
            "ss": None,
            "our_event_id": "2130836",
            "updated_at": "1581990232"
        }

        self.test_client = ResultBase(mock_result)

    def test_id(self):
        """Unit test for `ResultBase.id`"""
        result = self.test_client.id

        assert result == "86576599"

    def test_sport_id(self):
        """Unit test for `ResultBase.sport_id`"""
        result = self.test_client.sport_id

        assert result == "1"

    def test_time(self):
        """Unit test for `ResultBase.time`"""
        result = self.test_client.time

        assert result == "15093049123"

    def test_time_status(self):
        """Unit test for `ResultBase.time`"""
        result = self.test_client.time_status

        assert result == "12312"

    def test_time_league(self):
        """Unit test for `ResultBase.league`"""
        result = self.test_client.league

        assert isinstance(result, dict)

    def test_time_away(self):
        """Unit test for `ResultBase.time`"""
        result = self.test_client.away

        assert isinstance(result, dict)

    def test_time_home(self):
        """Unit test for `ResultBase.time`"""
        result = self.test_client.home

        assert isinstance(result, dict)

    def test_time_ss(self):
        """Unit test for `ResultBase.ss`"""
        result = self.test_client.ss

        assert result is None


class TestStatsBase(TestCase):
    """Unit tests for StatsBase Facade."""

    def setUp(self) -> None:
        """Instantiate StatsBase."""
        mock_stats = {
            "event_id": "2130389",
            "update_at": "1581990853",
            "update_dt": "2020-02-18 01:54:13",
        }

        self.test_client = StatsBase(mock_stats)

    def test_event_id(self):
        """Unit test for `StatsBase.event_id`."""
        result = self.test_client.event_id

        assert result == "2130389"

    def test_update_at(self):
        """Unit test for `StatsBase.update_at`."""
        result = self.test_client.update_at

        assert result == "1581990853"

    def test_update_dt(self):
        """Unit test for `StatsBase.update_dt`."""
        result = self.test_client.update_dt

        assert result == "2020-02-18 01:54:13"
