from fractions import *

print "Enter the number of players"
dice = 5 * int(raw_input(" "))

while dice > 1:
    print "Enter the number of dice you have."
    your_dice = int(raw_input(" "))
    expected_number = Fraction(1,3) * float(dice - your_dice)
    print "The number of dice is %d and you can expect there to be %d + any dice that match in your hand." % (dice, expected_number)
    dice = dice - 1
