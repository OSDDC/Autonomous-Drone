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
global location
global CO
global NO2
global C2H50H
global H2
global NH3
global CH4
global C3H8
global C4H10
global LPG
global GPL
global UVA
global UVB
location = "uknown"
CO = 0
NO2 = 0
C2H50H = 0
H2 = 0
NH3 = 0
CH4 = 0
C3H8 = 0
C4H10 = 0
LPG = 0
GPL = 0
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
    if Temp != 0 and Hum != 0 and volt != 0 and RSratio != 0 and Rs_R0 != 0:
        outputtext = "{\n"
        outputtext += " \"date\": \"" + datetoday + "\",\n"
        outputtext += " \"ort\" : \"" + location + "\", \n"
        outputtext += " \"CO\": " + CO + ",\n"
        outputtext += " \"NO2\": " + NO2 + ",\n"
        outputtext += " \"C2H50H\": " + C2H50H + ",\n"
        outputtext += " \"H2\": " + H2 + ",\n"
        outputtext += " \"NH3\": " + NH3 + ",\n"
        outputtext += " \"CH4\": " + CH4 + ",\n"
        outputtext += " \"C3H8\": " + C3H8 + ",\n"
        outputtext += " \"C4H10\": " + C4H10 + ",\n"
        outputtext += " \"LPG\": " + LPG + ",\n"
        outputtext += " \"GPL\": " + GPL + ",\n"
        outputtext += " \"UVA\": " + UVA + ",\n"
        outputtext += " \"UVB\": " + UVB + ",\n"
        outputtext += " \"%\": " + Hum + ",\n"
        outputtext += " \"TEMP\": " + Temp + ",\n"
        outputtext += "}"
        print(str(outputtext))
