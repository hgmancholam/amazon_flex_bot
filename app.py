import sys
from lib.FlexUnlimited import FlexUnlimited
from lib.Log import Log

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
      print(flexUnlimited.sendSMS())
    else:
      Log.error("Invalid argument provided.")
  else:
    flexUnlimited.run()