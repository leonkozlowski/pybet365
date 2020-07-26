"""Mock Objects for pytest."""
from tests.utils import load_json

from requests import HTTPError


class MockRequestsResponse(object):
    """MockRequestsResponse object."""

    def __init__(self, filepath: str, status: int = 200):
        self.status = status
        self._path = filepath

    def raise_for_status(self):
        if self.status != 200:
            raise HTTPError

        return None

    def json(self):
        return load_json(self._path)
