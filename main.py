print('Welcome to Tick-Tac-Toe!')

player_x = input('Player selecting x, please enter your name: ')
player_y = input('Player selecting o, please enter your name: ')

board = [" " for _ in range(9)]

def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")