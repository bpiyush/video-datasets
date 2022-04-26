"""Input/output helpers."""
import json


def load_json(path: str) -> dict:
    """Loads a json file."""
    with open(path, "r") as f:
        return json.load(f)