import random

MyNumber = random.randrange(0,100)

YourNumber = int(input("What number are you guessing?\r\n"))

if (YourNumber == MyNumber):
  print("Good job!")
else:
  print("Bad job.  It was " + str(MyNumber) + "!")