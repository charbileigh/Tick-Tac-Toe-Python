print("Welcome to Tic-Tac-Toe!")

# Get player names (fall back to defaults if left blank)
player_x = input("Player selecting X, please enter your name: ").strip() or "Player X"
player_o = input("Player selecting O, please enter your name: ").strip() or "Player O"

# Game state
board = [None] * 9  # positions 0..8
current = "X"       # X always starts
names = {"X": player_x, "O": player_o}

# Winning triplets (by indices)
WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # cols
    (0, 4, 8), (2, 4, 6)               # diagonals
]

def cell_label(i):
    """Show X/O if taken, else the cell number (1–9)."""
    return board[i] if board[i] is not None else str(i + 1)

def display_board():
    """Pretty print the board with numbers for free cells."""
    print()
    print(f" {cell_label(0)} | {cell_label(1)} | {cell_label(2)} ")
    print("---+---+---")
    print(f" {cell_label(3)} | {cell_label(4)} | {cell_label(5)} ")
    print("---+---+---")
    print(f" {cell_label(6)} | {cell_label(7)} | {cell_label(8)} ")
    print()

def check_winner():
    """Return 'X' or 'O' if there is a winner, else None."""
    for a, b, c in WIN_LINES:
        if board[a] is not None and board[a] == board[b] == board[c]:
            return board[a]
    return None

def board_full():
    return all(cell is not None for cell in board)

# Main game loop
while True:
    display_board()
    # Prompt current player
    prompt = f"{names[current]} ({current}), choose a position (1–9): "
    try:
        choice = input(prompt).strip()
        # allow quick exit
        if choice.lower() in {"q", "quit", "exit"}:
            print("Game ended. Bye!")
            break

        pos = int(choice) - 1
        if pos < 0 or pos > 8:
            print("Please enter a number from 1 to 9.")
            continue
        if board[pos] is not None:
            print("That spot is already taken. Try another one.")
            continue

        # Make the move
        board[pos] = current

        # Check for win/tie
        winner = check_winner()
        if winner:
            display_board()
            print(f"🎉 {names[winner]} ({winner}) wins! GG!")
            break
        if board_full():
            display_board()
            print("It's a tie!")
            break

        # Switch player
        current = "O" if current == "X" else "X"

    except ValueError:
        print("Please enter a valid number (1–9), or 'q' to quit.")
