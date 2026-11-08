import json
from pathlib import Path

DATA = Path("data")
DATA.mkdir(exist_ok=True)


def load(name):
    path = DATA / f"{name}.json"
    if path.exists():
        return json.loads(path.read_text())
    return []


def save(name, records):
    path = DATA / f"{name}.json"
    path.write_text(json.dumps(records, indent=2))