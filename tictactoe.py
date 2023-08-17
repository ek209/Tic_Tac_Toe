


class TicTacToe():
    def __init__(self):
        self.board = [[" " for num in range(0,3)] for num in range(0,3)]
        self.turn = "O"
        self.game_over = False
        self.show_board()


    #Creates the lines between the board to show it
    #TODO Cleanup code
    def show_board(self):
        board_str = '_ 0|1|2\n'
        for row_num in range(0, len(self.board)):
            board_str += str(row_num) + '|'
            for item in range(0, len(self.board[row_num])):
                board_str += self.board[row_num][item]
                if item < len(self.board[row_num]) - 1:
                    board_str += '|'
            board_str += '\n'
            if row_num < len(self.board) -1:
                board_str += '- - - -\n'
        print(board_str)

    #Checks turn, adds marker if square isnt taken already then changes turn
    def add_marker(self, x, y):
        try:
            if self.board[y][x] != 'X' and self.board[y][x] != 'O':
                self.board[y][x] = self.turn
                self.check_board_state()
                if not self.game_over:
                    if self.turn == 'O':
                        self.turn = 'X'
                    elif self.turn == 'X':
                        self.turn = 'O'
                else:
                    print(f"{self.turn}'s win")
            #Reprompts for move
            else: 
                print(f'{x} {y} has already been taken, please select another square.')
        except IndexError:
            print('Move out of range')
        if not self.game_over:
            print(f"Turn: {self.turn}'s")
        self.show_board()
    
    def check_board_state(self):
        self.check_column_win()
        self.check_row_win()
        self.check_diaganol_win()
        self.check_tie()

    def check_row_win(self):
        for row in self.board:
            if row == ['O','O','O'] or row == ['X', 'X', 'X']:
                self.game_over = True
    
    def check_column_win(self):
        for num in range(0,len(self.board)):
            column = [self.board[0][num], 
                    self.board[1][num], 
                    self.board[2][num]]
            if column == ['O', 'O', 'O'] or column == ['X', 'X', 'X']:
                self.game_over = True
    
    def check_diaganol_win(self):
        diags = [[self.board[0][0], 
                 self.board[1][1], 
                 self.board[2][2]],
                 [self.board[2][0], 
                 self.board[1][1], 
                 self.board[0][2]]]
        if ['O', 'O', 'O'] in diags or ['X', 'X', 'X'] in diags:
            self.game_over = True
    
    def check_tie(self):
        count = 0
        for row in self.board:
            for column in row:
                if column == 'X' or column == 'O':
                    count += 1
        if count == 9:
            self.turn = 'Cat'
            self.game_over = True

