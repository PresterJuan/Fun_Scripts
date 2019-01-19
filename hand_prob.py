"""
The goal of this is to check your probability of getting a pair at different points of the game.
"""
from fractions import *
diff_cards = 2

first = Fraction(44,50)
second = Fraction(43,49)
third = Fraction(42,48)
fourth = Fraction(41,47)
fifth = Fraction(40,46)

pre_flop = first * second * third * fourth * fifth
print ('preflop odds of NOT getting a pair %s' %str(float(pre_flop)))

odds_on_flop = first * second * third
print ('odds of NOT getting pair on the flop %s' %str(float(odds_on_flop)))

odds_after_flop = fourth * fifth
print ('odds of NOT getting pair in the last two cards %s' %str(float(odds_after_flop)))
odds_on_river = fifth
print ('odds of NOT getting pair on the river %s' %str(float(odds_on_river)))
