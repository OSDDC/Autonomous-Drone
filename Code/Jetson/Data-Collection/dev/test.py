# Complete Project Details: https://RandomNerdTutorials.com/raspberry-pi-analog-inputs-python-mcp3008/

#from gpiozero import PWMLED, MCP3008
from time import sleep
import datetime

datetoday = str(datetime.date.today())


#create an object called pot that refers to MCP3008 channel 0
while True:
    MQ9 = input("Enter the number for the variable(LPG):" )
    Temp = input("Enter the number for the variable(Temp):" )
    Hum = input("Enter the number for the variable(Hum):" )

    print('Your input was(LPG)=' + MQ9)
    print('Your input was(Temp)=' + Temp)
    print('Your input was(Hum)=' + Hum)

    answer = input("Do you want to continue? (yes/no): ").lower()
    if answer == "yes":
        print("Continuing...")
        # Put your code here that you want to execute if "yes" is entered

        if MQ9 != 0:
            outputtext = "{\n"
            outputtext += " \"date\": \"" + datetoday + "\",\n"
            outputtext += " \"LPG\": " + MQ9 + ",\n"
            outputtext += " \"Temp\": " + Temp + ",\n"
            outputtext += " \"Hum\": " + Hum + "\n"
            outputtext += "}"
        try:
            with open("data.json", "a") as data:
                data.write(",\n" + str(outputtext))
        except:
            with open("data.json", "w") as data:
                data.write(str(outputtext))

    elif answer == "no":
        print("Exiting...")
        break  # This will exit the loop and end the program
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")