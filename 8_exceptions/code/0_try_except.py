"""
Try except
"""

z = 3

try:
    int("a")  # ValueError
    result = z / 0  # ZeroDivisionError

except ZeroDivisionError as e:
    print("es ist ein Fehler aufgetreteten")
    print(f"Das e ist das Fehlerobjekt: {e}")
    # e.__traceback__.tb_lineno
except ValueError as e:
    print("Alarm! Value Error!")
    print(e)

print("Hier gehts weiter")
