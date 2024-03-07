# Complete Project Details: https://RandomNerdTutorials.com/raspberry-pi-analog-inputs-python-mcp3008/

from gpiozero import PWMLED, MCP3008
from time import sleep
import date



global Temp
global Hum
global LPG
global UVA
global UVB

global volt
global RSration
global Rs_R0

global datetoday

#create an object called pot that refers to MCP3008 channel 0
pot = MCP3008(0)

#create a PWMLED object called led that refers to GPIO 14
led = PWMLED(14)

def mq9():
    while True:
        if(pot.value < 0.001):
            led.value = 0
        else:
            led.value = pot.value
        print(pot.value)
        sleep(0.1)