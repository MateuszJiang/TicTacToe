from enum import Enum

class Player(Enum):
    player_one = "X"
    player_two = "O"

class Game:
    board_fields = [ "-","-","-",
                      "-","-","-",
                       "-","-","-" ]
    is_game_going = True
    winner = None
    current_player = Player.player_one


    def restart(self):
        self.board_fields = [ "-","-","-",
                               "-","-","-",
                                "-","-","-" ]
        self.is_game_going = True
        self.winner = None
        self.current_player = Player.player_one

        
    def draw_board(self):
        for i in range (0, 8, 3):
            print( self.board_fields[i], "|" , self.board_fields[i+1] , "|" , self.board_fields[i+2] )
 
    def handle_turn(self):
        print (self.current_player.value + "'s turn!")
        position = int(input("Choose a position from 1-9: "))
        Valid = False
        while not Valid:
            while position not in range(1,10):
                position = int(input("Wrong Position, choose a position from 1-9: "))
            position = position - 1
            if self.board_fields[position] == "-":
                Valid = True
            else:
                print("Position taken, try again")
                position = int(input("Choose a position from 1-9: "))
        
        self.board_fields[position] = self.current_player.value
        self.draw_board()

    def check_if_game_over(self):
        if self.check_for_winner() or self.check_for_tie():
            self.is_game_going = False

    def flip_player(self):
        if self.current_player == Player.player_one:
            self.current_player = Player.player_two
        else:
            self.current_player = Player.player_one

    def game_finished(self):
        print("Game is finished !")
        if self.winner == Player.player_one:
            print("Player one won !")
        elif self.winner == Player.player_two:
            print("Player two won !")
        else:
            print("Game tied!!!")
        self.restart()

    def play_game(self):
        self.draw_board()

        while self.is_game_going:
            self.handle_turn()
            self.check_if_game_over()
            self.flip_player()
        
        self.game_finished()

    def check_for_winner(self):
        if self.board_fields[0] == self.board_fields[1] == self.board_fields[2] != "-":
            self.make_winner(self.board_fields[0])
            return True
        if self.board_fields[0] == self.board_fields[3] == self.board_fields[6] != "-":
            self.make_winner(self.board_fields[0])
            return True
        if self.board_fields[5] == self.board_fields[0] == self.board_fields[8] != "-":
            self.make_winner(self.board_fields[5])
            return True
        if self.board_fields[5] == self.board_fields[7] == self.board_fields[1] != "-":
            self.make_winner(self.board_fields[5])
            return True
        if self.board_fields[5] == self.board_fields[2] == self.board_fields[6] != "-":
            self.make_winner(self.board_fields[5])
            return True
        if self.board_fields[5] == self.board_fields[3] == self.board_fields[5] != "-":
            self.make_winner(self.board_fields[5])
            return True
        if self.board_fields[8] == self.board_fields[6] == self.board_fields[7] != "-":
            self.make_winner(self.board_fields[8])
            return True
        if self.board_fields[8] == self.board_fields[2] == self.board_fields[5] != "-":
            self.make_winner(self.board_fields[8])
            return True
        else:
            return False

    def check_for_tie(self):
        if "-" not in self.board_fields:
            return True
        else:
            return False

    def make_winner(self,board_winner_field):
        if board_winner_field == "X":
            self.winner = Player.player_one
        else:
            self.winner = Player.player_two


start_game = Game()

print("              HI! ")
print("This is a simple TicTacToe game")

while True:
    print( "In order to start click enter")
    print( "If yo wanna quit click Escape")
    determine_user_action = input("")
    if determine_user_action == "":
        start_game.play_game()
    else:
        break
