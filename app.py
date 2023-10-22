import sys
from lib.FlexUnlimited import FlexUnlimited
from lib.Log import Log
from lib.Firebase import FirebaseManager

if __name__ == "__main__":
    Log.info("***Amazon Flex Unlimited v2*** \n")
    flexUnlimited = FlexUnlimited()
    firebase = FirebaseManager()
    if (len(sys.argv) > 1):
        arg1 = sys.argv[1]
        if (arg1 == "getAllServiceAreas" or arg1 == "--w"):
            print("\n Your service area options:")
            print(flexUnlimited.getAllServiceAreas())
        elif (arg1 == "--sms"):
            print("\n Send SMS:")
            print(flexUnlimited.sendSMS())
        elif (arg1 == "--bots"):
            print("\n Get all active users:")
            print(firebase.getUsers())
        else:
            Log.error("Invalid argument provided.")
    else:
        flexUnlimited.run()
