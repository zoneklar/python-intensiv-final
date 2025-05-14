"""
Der else-Block wird immer ausgeführt, wenn kein Fehler aufgetreten ist.
"""

import requests


try:
    x = "hallo"
    p = int("u")  # Tritt ValueError auf, wird der else-Zweig nicht ausgeführt
except ValueError as e:
    print("Value Error ist aufgetreten")
else:
    print("es ist keine Exception ausgelöst worden.")


def show_temperature(latitude=52.52, longitude=13.34) -> None:
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        "&hourly=temperature_2m"
    )

    try:
        response = requests.get(url, timeout=3)
    except requests.exceptions.RequestException as e:
        print(f"API ERROR {e=}")
    else:
        # Else Zweig, es ist keine Exception aufgetreten
        data = response.json()
        temp_now = data["hourly"]["temperature_2m"][0]
        print(f"Die Temperatur ist {temp_now}")


show_temperature()
show_temperature(latitude=0)
