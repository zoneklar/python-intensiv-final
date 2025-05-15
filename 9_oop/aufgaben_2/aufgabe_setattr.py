"""
setattr (Schwer)
Wir haben eine Klasse LineItem gegeben. Erstelle LineItem-Objekte und speichere
sie in einer Liste line_items. Achte in __init__ darauf, dass die Werte in
**kwargs übergeben werden und erstelle dynamisch die Attribute.
Es muss __repr__ implementiert sein, wie unten gezeigt.
"""


class LineItem:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __repr__(self):
        value_list = ", ".join([f"{k}={v!r}" for k, v in vars(self).items()])
        return f"<{self.__class__.__name__}({value_list})>"


lines = [
    {"id": 3, "name": "Pencil Geha", "style": "bold", "color": "black"},
    {
        "id": 13,
        "name": "Pencil Geha Professional",
        "style": "bold",
        "color": "red",
    },
    {
        "id": 23,
        "name": "Parker Chef",
        "style": "thin",
        "color": "silver",
        "bevel": True,
    },
]

line_items = [LineItem(**item) for item in lines]
print(line_items)
