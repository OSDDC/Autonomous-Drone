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

def get_sensor_data():
    # Read sensor values
    MQ9 = MQ9pot.value
    Temp = sensor.temperature
    Hum = sensor.relative_humidity

    date = datetime.date.today().strftime("%d.%m.%Y")

    # Convert sensor readings to appropriate types
    lpg = int(MQ9 * 1023)  # Assuming MQ9pot.value returns a float between 0 and 1
    percentage = round(Hum)
    temp = round(Temp)

    return {
        "date": date,
        "LPG": lpg,
        "Hum": percentage,
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
        data = get_sensor_data()
        
        # Add new data to list
        data_list.append(data)
        
        # Save updated data list
        save_data(filename, data_list)
        
        formatted_data = (
        f"Measurement Data:\n"
        f"Date: {data['date']}\n"
        f"LPG Level: {data['LPG']} ppm\n"
        f"Humidity: {data['Hum']}%\n"
        f"Temperature: {data['TEMP']}°C"
        )
        
        print("Daten wurden erfolgreich in data.json gespeichert.")
        print(formatted_data)
        
        sleep(30)

if __name__ == "__main__":
    main()
