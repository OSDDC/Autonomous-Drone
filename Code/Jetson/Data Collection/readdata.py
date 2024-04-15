#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import time
import simplejson as json

# Serielle Verbindung zum Arduino (angepasst auf den entsprechenden Port)
ser = serial.Serial('/dev/ttyACM0', 9600)

# Puffer für die empfangenen Daten
buffer = ""

while True:
    try:
        # Lese eine Zeile von der seriellen Schnittstelle
        buffer = ser.readline()
        print(buffer)  # Zeige den empfangenen Puffer an
        data = json.loads(buffer)  # Parsen der JSON-Daten

        # Extrahiere die untergeordneten Werte
        CO = data["CO"]
        LPG = data["LPG"]
        UVA = data["UVA"]
        UVB = data["UVB"]
        Hum = data["Hum"]
        Temp = data["Temp"]

        print("Wert für 'CO':", CO)
        print("Wert für 'LPG':", LPG)
        print("Wert für 'UVA':", UVA)
        print("Wert für 'UVB':", UVB)
        print("Wert für 'Hum':", Hum)
        print("Wert für 'Temp':", Temp)

        # Schreibe die Daten in eine .json-Datei
        with open("arduino_data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

    except json.JSONDecodeError:
        print("Fehler: Ungültige oder unvollständige Nachricht")

    # Warte eine kurze Zeit, um den Arduino genügend Zeit zum Senden zu geben
    time.sleep(0.1)
