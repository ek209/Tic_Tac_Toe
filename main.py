from tictactoe import TicTacToe

game = TicTacToe()
while not game.game_over:
    try:
        x = int(input('COLUMN: '))
        y = int(input('ROW:'))
        if type(x) != int or type(y) != int:
            raise ValueError
        game.add_marker(x,y)
    except ValueError:
        print('Must be integer!')
    