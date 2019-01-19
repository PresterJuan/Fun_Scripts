import random

print "Call it. Heads or Tails"

quarter = ["Heads", "Tails"]

guess = raw_input("> ")

result = random.choice(quarter)

if result == guess:
    print "You guessed correctly. It is %s" % result
else:
    print "Sorry it is %s" % result
