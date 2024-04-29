# Complete Project Details: https://RandomNerdTutorials.com/raspberry-pi-analog-inputs-python-mcp3008/
# https://learn.adafruit.com/adafruit-sht31-d-temperature-and-humidity-sensor-breakout/python-circuitpython


from gpiozero import PWMLED, MCP3008
from time import sleep
import board
import adafruit_sht31d

# sudo pip3 install adafruit-circuitpython-sht31d

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sensor = adafruit_sht31d.SHT31D(i2c)

#create an object called pot that refers to MCP3008 channel 0
MQ9pot = MCP3008(0)

def main():
    while True:
        MQ9 = str(MQ9pot.value)
        Temp = str(sensor.temperature)
        Hum = str(sensor.relative_humidity)
    
        print(MQ9)
        print(Temp)
        print(Hum)
            
        if MQ9 != 0 and Temp != 0 and Hum != 0:
            outputtext = "{\n"
            outputtext += " \"LPG\": " + MQ9 + ",\n"
            outputtext += " \"Temp\": " + Temp + ",\n"
            outputtext += " \"Hum\": " + Hum + ",\n"
            outputtext += "}"
        try:
            with open("data.json", "a") as data:
                data.write(",\n" + str(outputtext))
        except:
            with open("data.json", "w") as data:
                data.write(str(outputtext))

        sleep(5)

if __name__ == "__main__":
    main()