from gpiozero import MCP3008
import serial
import time
import date

global Temp
global Hum
global volt
global RSratio
global Rs_R0
global datetoday
Temp = 0
gendate = date.today()
datetoday = str(gendate.day) + "." + str(gendate.month) + "." + str(gendate.year)
Hum = 0
volt = 0
RSratio = 0
Rs_R0 = 0
# unused in the current version
global LPG
global UVA
global UVB

LPG = 0
UVA = 0
UVB = 0

arduino = serial.Serial('COM4', 9600, timeout=.1)

def read_from_arduino():
    if arduino.inWaiting() > 0:
        line = arduino.readline().decode('utf-8').strip()
        return line

def read_from_analog(port):
    tempport = MCP3008(port)
    return tempport.value

while True:
    time.sleep(0.1)
    data = read_from_arduino().split(" ")
    match data[0]:
        case "Temp":
            Temp = data[3]
        case "Hum.":
            Hum = data[3]
        case "sensor_volt":
            volt = data[2]
        case "RS_ratio":
            RSratio = data[2]
        case "Rs/R0":
            Rs_R0 = data[2]
    MQ9 = read_from_analog(0)
    if Temp != 0 and Hum != 0 and volt != 0 and RSratio != 0 and Rs_R0 != 0:
        outputtext = "{\n"
        outputtext += " \"date\": \"" + datetoday + "\",\n"
        outputtext += " \"LPG\": " + LPG + ",\n"
        outputtext += " \"UVA\": " + UVA + ",\n"
        outputtext += " \"UVB\": " + UVB + ",\n"
        outputtext += " \"%\": " + Hum + ",\n"
        outputtext += " \"TEMP\": " + Temp + ",\n"
        outputtext += "}"
        try:
            with open("data.json", "a") as data:
                data.write(",\n" + str(outputtext))
        except:
            with open("data.json", "w") as data:
                data.write(str(outputtext))
