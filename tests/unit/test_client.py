"""Unit tests for `betfund_bet365.client` modules."""
import mock
import pytest
import requests

from requests import HTTPError

from unittest import TestCase

from pybet365.client.client import Bet365

from tests.mocks import MockRequestsResponse


class TestBet365(TestCase):
    """Unit tests for Bet365 Client."""

    def setUp(self) -> None:
        """Instantiate Bet365."""
        self.test_client = Bet365(
            api_host="you-will-never-guess",
            api_key="you-will-never-guess"
        )

    def test_constructor(self):
        """Unit test for `Bet365().__init__(...)`."""
        assert self.test_client.headers == {
            "x-rapidapi-host": "you-will-never-guess",
            "x-rapidapi-key": "you-will-never-guess",
        }
        assert self.test_client.base_url == (
            "https://bet365-sports-odds.p.rapidapi.com/{}/bet365/"
        )

    @mock.patch.object(requests, "get")
    def test_get_raises(self, mock_api_response):
        """Unit test for `._get(...)` raises."""
        mock_api_response.return_value = MockRequestsResponse(
            filepath=None, status=404
        )

        with pytest.raises(HTTPError):
            self.test_client._get(
                url_extras="failure", params={"oops": "sorry"}
            )

    @mock.patch.object(requests, "get")
    def test_upcoming_events(self, mock_api_response):
        """Unit test for `._get(...)` success."""
        mock_api_response.return_value = MockRequestsResponse(
            filepath="testData/upcoming_events_table_tennis.json"
        )

        result = self.test_client._get(
            url_extras="upcoming", params={"params": "dict"}
        )

        assert isinstance(result, dict)
