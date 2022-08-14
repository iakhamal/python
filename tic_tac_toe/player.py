import math 
import random
class player:
    def __init__(self, letter  ):
        self.letter= letter   # is the player is o or x player 
    
    def get_move(self, game):
        pass

class random_computer_player(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class random_human_player(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self , game):
        valid_square = False
        value = None 
        while not valid_square :
            square = input(self.player + '\'s turn.Input move (0-9):')
            try :
                value = int (square)
                if value not in game.available_moves():
                    raise ValueError
                valid_square = True 
            except ValueError:
                print ("invalid input try again")

        return value 
    
 