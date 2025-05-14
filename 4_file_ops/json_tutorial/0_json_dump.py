"""
Das Modul json.
- dump: => schreibe in Datei
- dumps: => schreibe als String
- load: lese Json-Datei ein
- loads: lese Json-String ein
"""

import json
from pathlib import Path

data = {
    "city": {
        "name": "Dortmund",
        "population": 654_000,
        "coords": (2, 5),
    }
}

# dumps String
json_dump = json.dumps(data)
print(json_dump, type(json_dump))
# Python Objekt aus Json erstllen
python_data = json.loads(json_dump)
print(python_data)


# dump in file
with open(Path(__file__).parent / "example.txt", mode="w", encoding="utf-8") as f:
    json.dump(data, f)
