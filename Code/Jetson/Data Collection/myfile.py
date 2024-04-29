# Complete Project Details: https://RandomNerdTutorials.com/raspberry-pi-analog-inputs-python-mcp3008/

from gpiozero import PWMLED, MCP3008
from time import sleep



#create an object called pot that refers to MCP3008 channel 0
pot = MCP3008(0)

#create a PWMLED object called led that refers to GPIO 14
led = PWMLED(14)


while True:
    print(pot.value)
    sleep(5)



    if pot.value != 0:
        outputtext = "{\n"
        outputtext += " \"LPG\": " + pot.value + ",\n"
        outputtext += "}"
    try:
        with open("data.json", "a") as data:
            data.write(",\n" + str(outputtext))
    except:
        with open("data.json", "w") as data:
            data.write(str(outputtext))