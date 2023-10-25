import sys

from lib.FlexUnlimited import FlexUnlimited
from lib.Log import Log
from lib.Firebase import FirebaseManager
from colasbots import ColasBots

if __name__ == "__main__":
    Log.info("***Amazon Flex Unlimited v2*** \n")
    flexUnlimited = FlexUnlimited()
    if (len(sys.argv) > 1):
        arg1 = sys.argv[1]
        if (arg1 == "getAllServiceAreas" or arg1 == "--w"):
            print("\n Your service area options:")
            print(flexUnlimited.getAllServiceAreas())
        elif (arg1 == "--sms"):
            print("\n Send SMS:")
            print(flexUnlimited.sendSMS("Esta es una prueba"))
        elif (arg1 == "--call"):
            print("\n Send CALL:")
            print(flexUnlimited.sendCALL())

        elif (arg1 == "--bots"):
            print("\n Get all active users:")
            firebase = FirebaseManager()
            usuarios = firebase.getUsers()
            for usuario in usuarios:
                print(usuario, "\n")
                # print(usuario["id"], "\n")
        elif (arg1 == "--run"):
            flexUnlimited.run()
        else:
            Log.error("Invalid argument provided.")
    else:
        # flexUnlimited.run()
        print("\n Select an option and restart. \n")
        print("--w Get all service areas \n")
        print("--sms Send SMS \n")
        print("--bots Get all active users \n")

        colas = ColasBots()
        colas.correrProcesos()
        # colas.funcion(5)
