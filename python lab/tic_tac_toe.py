board = [' '] * 9

def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

player = 'X'

for _ in range(9):
    print_board()
    pos = int(input(f"Player {player}, Enter position (1-9): ")) - 1

    if board[pos] == ' ':
        board[pos] = player
        player = 'O' if player == 'X' else 'X'
    else:
        print("Position already occupied.")

print_board()