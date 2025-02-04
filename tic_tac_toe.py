import random

# Tic-Tac-Toe Board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")

# Function to check for a win
def check_winner(player):
    win_patterns = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_patterns)

# Function for AI move (random)
def ai_move():
    empty_cells = [i for i in range(9) if board[i] == " "]
    if empty_cells:
        return random.choice(empty_cells)
    return None

# Main game loop
def play_game():
    print("Tic-Tac-Toe AI Game")
    print_board()

    for turn in range(9):
        if turn % 2 == 0:
            move = int(input("Enter your move (0-8): "))
        else:
            move = ai_move()
            print(f"AI chooses: {move}")

        if board[move] == " ":
            board[move] = "X" if turn % 2 == 0 else "O"
        else:
            print("Invalid move, try again.")
            continue

        print_board()

        if check_winner("X"):
            print("You win!")
            return
        elif check_winner("O"):
            print("AI wins!")
            return

    print("It's a draw!")

play_game()