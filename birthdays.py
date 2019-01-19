from fractions import *

people = 20

days = 365

def birthday_odds(people,days):
    """Used to calculate the odds that two people share a same birthday in a room full of people."""
    odds_not_same_day = []
    while people != 0:
        odds_not_same_day.append(Fraction(days,365))
        days -= 1
        people -= 1
    print (odds_not_same_day)
    return float((1-reduce(lambda x,y: x*y, odds_not_same_day)))

if __name__ == "__main__":
    answer = birthday_odds(people,days)
    print (answer)
