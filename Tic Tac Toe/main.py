import random


class Board:

    def __init__(self):
        row1 = ["_", "_", "_"]
        row2 = ["_", "_", "_"]
        row3 = ["_", "_", "_"]
        self.board = [row1, row2, row3]

    def clear_board(self):
        row1 = ["_", "_", "_"]
        row2 = ["_", "_", "_"]
        row3 = ["_", "_", "_"]
        self.board = [row1, row2, row3]
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])

    def show_board(self):
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])

    def player_move(self, player_type):
        valid_move = False
        while not valid_move:
            row = int(input("row: "))
            column = int(input("column: "))
            if self.board[row][column] == '_':
                if player_type == 'x':
                    self.board[row][column] = 'x'
                else:
                    self.board[row][column] = 'o'
                valid_move = True
            else:
                print("Not valid move. Try again.")
        print("player move")
        self.show_board()

    def com_move(self, player_type):
        if player_type == 'x':
            com = 'o'
        else:
            com = 'x'
        valid_move = False
        while not valid_move:
            row = random.randint(0, 2)
            column = random.randint(0, 2)
            if self.board[row][column] == '_':
                self.board[row][column] = com
                print()
                print("com move")
                self.show_board()
                print()
                valid_move = True

    def check_win_rows(self, player):

        if player == 'x':
            com = 'o'
        else:
            com = 'x'

        for row in range(0, 3):
            if self.board[row][0] == player and self.board[row][1] == player and self.board[row][2] == player:
                return player
            if self.board[row][0] == com and self.board[row][1] == com and self.board[row][2] == com:
                return com
        return "na"

    def check_win_columns(self, player):

        if player == 'x':
            com = 'o'
        else:
            com = 'x'

        for column in range(0, 3):
            if self.board[0][column] == player and self.board[1][column] == player and self.board[2][column] == player:
                return player
            if self.board[0][column] == com and self.board[1][column] == com and self.board[2][column] == com:
                return com
        return "na"


def play_game():

    response = input("Play as (x) or (o)? ").lower()

    while response != 'x' and response != 'o':
        print("Please select x or o")
        response = input("Play as (x) or (o)? ").lower()

    if response == 'x':
        player = response
        com = 'o'
    else:
        player = response
        com = 'x'

    game_board = Board()
    win = False

    while not win:

        game_board.player_move(player)
        game_board.com_move(player)

        column_response = game_board.check_win_columns(player)
        row_response = game_board.check_win_rows(player)

        if column_response == player or row_response == player:
            print(f"{player} wins!")
            play_again = input("Play again? (y) or (n): ").lower()

            if play_again == 'y':
                game_board.clear_board()
                win = False
            else:
                win = True

        if column_response == com or row_response == com:
            print(f"{com} wins!")
            play_again = input("Play again? (y) or (n): ").lower()

            if play_again == 'y':
                game_board.clear_board()
                win = False
            else:
                win = True


if __name__ == '__main__':
    play_game()
