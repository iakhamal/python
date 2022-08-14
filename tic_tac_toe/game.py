

from player import random_computer_player, random_human_player


class tictactoe:
    #building the 3*3 game board using a single list
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        # keeping track of the winner 
        self.current_winner = None 

    def print_board (self ):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print (' | ' + ' | '.join(row)+'|')

    @staticmethod
    def print_board_numbeers ():
        number_board = [[str(i) for i in range (j*3 , (j+1)*3)] for j in range(3)]
        for row in number_board:
             print (' | ' + ' | '.join(row)+'|')

    def available_moves(self):
        moves = []
        for (i , x) in enumerate(self.board):
            if x == ' ':
                moves.append(i)
        return moves
    
    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares ( self):
        return len(self.available_moves())

       #defining the moves function
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            #checking for the winner
            if self.winner(square , letter ):
                self.current_winner = letter  
            return True
        return False

    def winner (self, square , letter ):
        #for the rows
        row_ind = square // 3
        row= self.board[row_ind*3: (row_ind+1)*3]
        if all([x== letter for x in row] ):
            return True 

        #for the columns
        col_ind = square % 3 
        column = [self.board [col_ind+i*3] for i in range(3)]
        if all([x == letter for x in column ]):
            return True

        #for the diagonals
        #these are the indexes of diagonal 0, 2 , 4, 6 ,8
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0 , 4 , 8]]  # left to right diagonal
            if all( [x == letter for x in diagonal1]):
                return True 

            diagonal2 = [self.board[i] for i in [0 , 4 , 6]]  # right to left diagonal
            if all( [x == letter for x in diagonal2]):
                return True 

        #if there is no winner 
        return False


def play(game , x_player , o_player ,print_game = True):
    if print_game :
        game.print_board_numbers()

    letter = 'x' #initializing the game with letter x
    #iterate while the game still has empty squares 
    while  game.empty_squares():
        if letter == 'o':
            square =  o_player.get_move(game)
        else : 
            square = x_player.get_move(game)

        if game.make_move(square , letter ):
            if print_game :
                print (letter + f'makes a move to the square{square}')
                game.print_board()
                print(' ')

            if game.current_winner :
                if print_game:
                    print (letter +" winner!")
                return letter 

            if letter == 'x':
                letter = 'o'
            else:
                letter = 'x' 
        if print_game :
            print ( 'it \'s a tie ')

if __name__ =='__main__':
    x_player = random_human_player('x')
    o_player = random_computer_player('o')
    t = tictactoe()
    play(t , x_player , o_player , print_game=True)


    
     