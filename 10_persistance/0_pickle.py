"""
Problem:
- Nur pythonwelt
- potentiell gefährlich beim Ent-Picklen


Alternative:
https://pypi.org/project/dill/

"""

from pathlib import Path
import pickle


class A:
    def __init__(self, a, b):
        print(a, b)


liste = [A(1, 2), A(33, 33)]

# erzeugt bytes-Objekt
print(pickle.dumps(liste))

# Liste in Pickle umwandeln
with open(Path(__file__).parent / "test.pk", mode="wb") as f:
    pickle.dump(liste, f)


# Ent-Picklen (nur machen bei vertrauenswürdiger Quelle)
with open(Path(__file__).parent / "test.pk", mode="rb") as f:
    python_code = pickle.load(f)
    print(python_code)
