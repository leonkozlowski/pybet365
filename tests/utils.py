"""Test utility modules."""
import json
import os


def load_json(filepath: str):
    """Load `*.json` test file."""
    if not filepath:
        return None

    abs_path = _resolve_relative_path(filepath)
    with open(abs_path) as f:
        raw_json = f.read()

        return json.loads(raw_json)


def _resolve_relative_path(filepath: str):
    """Resolve relative import path."""
    if not filepath:
        return None

    inf_path = os.path.join(os.path.dirname(__file__), filepath)

    return inf_path
