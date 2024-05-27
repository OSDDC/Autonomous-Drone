from gpiozero import MCP3008  # type: ignore
from time import sleep
import board  # type: ignore
import adafruit_sht31d  # type: ignore
import datetime
import os
import json

# sudo pip3 install adafruit-circuitpython-sht31d --break-system-packages

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sensor = adafruit_sht31d.SHT31D(i2c)

# Create an object called pot that refers to MCP3008 channel 0
MQ9pot = MCP3008(0)

def get_user_input(MQ9, Temp, Hum):
     # Read sensor values
    MQ9 = str(MQ9pot.value)
    Temp = str(sensor.temperature)
    Hum = str(sensor.relative_humidity)

    date = str(datetime.date.today().strftime("%d.%m.%Y"))

    # Convert sensor readings to appropriate types
    lpg = int(float(MQ9) * 1023)  # Assuming MQ9pot.value returns a float between 0 and 1
    percentage = int(Hum)
    temp = int(Temp)

    return {
        "date": date,
        "LPG": lpg,
        "%": percentage,
        "TEMP": temp
    }

def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as json_file:
            try:
                return json.load(json_file)
            except json.JSONDecodeError:
                return []
    else:
        return []

def save_data(filename, data):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main():
    filename = 'data.json'
    
    while True:
        
        # Load existing data
        data_list = load_data(filename)
        
        # Collect new data
        data = get_user_input(LPG, %, TEMP)
        
        # Add new data to list
        data_list.append(data)
        
        # Save updated data list
        save_data(filename, data_list)
        
        print("Daten wurden erfolgreich in data.json gespeichert.")
        
        sleep(30)

if __name__ == "__main__":
    main()
