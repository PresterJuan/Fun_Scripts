import random

dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]

print "When you're ready for the next roll press any button.\nWhen you're ready to quit. Type stop and press enter."


while True:
    x = raw_input()
    if x != "Stop" and x != "stop":
        print (random.choice(dice1) + random.choice(dice2))
    else:
        break
