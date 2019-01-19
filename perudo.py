"""Exactly like perudo with dice, but on the computer."""

dice_results = {}
num_dice = {}
player_order = {}
current_dice_stmt = []
num_players = 0
current_player = 0
previous_player = 0

class playa(object):

    def __init__(self,name,order,num_dice):
        self.name = name
        self.order = order
        self.num_dice = dice

    def say_num_dice(dice, num_dice):
        current_dice_stmt = [(dice,num_dice)]

    def call_bs():
        questionable_num_dice = current_dice_stmt[0][1]
        dice = current_dice_stmt[0][0]
        if questionable_num_dice < (dice_results[dice] + dice_results[1]):
            num_dice[current_player] -= 1
        else:
            num_dice[previous_player] -= 1

def start_hand():
    try:
        if prior == num_players:
            prior = 0
        current = prior + 1
    except:
        pass
    #I stopped here

def set_up():
    while True:
        print ('Set up your game. Type the name of the player. If you are done adding players type break')
        name = raw_input(" ")
        name.lower()
        if 'break' in name:
            break
        else:
            pass
        print ('Type the order of the player in the game. Keep it to 1,2,3 etc.')
        order = int(raw_input(" "))
        num_dice[name.upper()] = 5
        player_order[name.upper()] = order
        num_players += 1

if __name__ == '__main__':
    set_up()
    print (num_dice)
    print (player_order)
