"""
guter Seiteneffekt
"""

player_stat = {
    "bilbo": {
        "life": 100,
        "power": 22,
        "weapons": {"Stich"},
    },
    "gollum": {
        "life": 100,
        "power": 22,
        "weapons": set(),
    },
}


def add_life_points(player_name, life_points):
    player_stat[player_name]["life"] += life_points


# Aufruf verändert das Player-Stats Dicts
add_life_points("gollum", 42)
