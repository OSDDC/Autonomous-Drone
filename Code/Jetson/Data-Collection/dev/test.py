import json
import os
import datetime

# Funktion, um manuelle Eingaben zu sammeln
def get_user_input():
    # Datum eingeben
    date = str(datetime.date.today().strftime("%d.%m.%Y"))
    
    # LPG Wert eingeben
    lpg = int(input("Geben Sie den LPG Wert ein: "))
    
    # Prozentwert eingeben
    percentage = int(input("Geben Sie den Prozentwert ein: "))
    
    # Temperatur eingeben
    temp = int(input("Geben Sie die Temperatur ein: "))
    
    return {
        "date": date,
        "LPG": lpg,
        "%": percentage,
        "TEMP": temp
    }

# Überprüfen, ob die Datei existiert und Daten laden, falls vorhanden
if os.path.exists('data.json'):
    with open('data.json', 'r') as json_file:
        try:
            data_list = json.load(json_file)
        except json.JSONDecodeError:
            data_list = []
else:
    data_list = []

# Benutzereingaben sammeln
data = get_user_input()

# Neue Daten zur Liste hinzufügen
data_list.append(data)

# Daten in die JSON-Datei schreiben
with open('data.json', 'w') as json_file:
    json.dump(data_list, json_file, indent=4)

print("Daten wurden erfolgreich in data.json gespeichert.")
