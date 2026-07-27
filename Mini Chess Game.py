# create 6x6 board

pieces = {
    "WK": [7,4],
    "WQ": [7,3],
    "WR": [7,0],
    "WB": [7,2],
    "WN1": [7,1],
    "WN2": [7,6],

    "BK": [0,4],
    "BQ": [0,3],
    "BR": [0,7],
    "BB": [0,5],
    "BN": [0,6],
    "BP": [1,4],
}


# Create board
def update_board():
    board = [["." for _ in range(8)] for _ in range(8)]

    for piece, position in pieces.items():
        row, col = position
        board[row][col] = piece

    return board


# Display board
def show_board():
    board = update_board()

    print("\n  0  1  2  3  4  5  6  7")

    for i, row in enumerate(board):
        print(i, " ".join(f"{square:>2}" for square in row))


# Move piece
def move_piece(player):

    piece = input("Enter piece: ").upper()

    if piece not in pieces:
        print("Piece does not exist")
        return

    if player == "White" and not piece.startswith("W"):
        print("You can only move white pieces")
        return

    if player == "Black" and not piece.startswith("B"):
        print("You can only move black pieces")
        return

    new_row = int(input("Enter destination row (0-7): "))
    new_col = int(input("Enter destination column (0-7): "))

    if new_row < 0 or new_row > 7 or new_col < 0 or new_col > 7:
        print("Invalid location")
        return


    # Check for captures
    for enemy, position in list(pieces.items()):
        if position == [new_row, new_col]:

            if enemy[0] != piece[0]:
                print(piece, "captured", enemy)
                del pieces[enemy]

            else:
                print("You cannot capture your own piece")
                return


    # Move piece
    pieces[piece] = [new_row, new_col]


# Save game
def save_game():

    with open("savegame.csv", "w", newline="") as file:
        writer = csv.writer(file)

        for piece, position in pieces.items():
            writer.writerow([piece, position[0], position[1]])

    print("Game saved!")


# Load game
def load_game():

    global pieces
    pieces = {}

    try:
        with open("savegame.csv", "r") as file:

            reader = csv.reader(file)

            for row in reader:
                pieces[row[0]] = [int(row[1]), int(row[2])]

        print("Game loaded!")

    except FileNotFoundError:
        print("No saved game found")


# Count pieces
def piece_count():

    white = 0
    black = 0

    for piece in pieces:

        if piece.startswith("W"):
            white += 1
        else:
            black += 1

    print("White pieces:", white)
    print("Black pieces:", black)


# Check winner
def check_game():

    if "WK" not in pieces:
        print("Black wins!")
        return False

    if "BK" not in pieces:
        print("White wins!")
        return False

    return True


# Main Game Loop

turn = "White"

while True:

    show_board()
    piece_count()

    print("\nMenu")
    print("1. Move Piece")
    print("2. Save Game")
    print("3. Load Game")
    print("4. Quit")

    choice = input("Choose option: ")


    if choice == "1":

        move_piece(turn)

        if not check_game():
            break

        if turn == "White":
            turn = "Black"
        else:
            turn = "White"


    elif choice == "2":
        save_game()


    elif choice == "3":
        load_game()


    elif choice == "4":
        print("Game ended")
        break


    else:
        print("Invalid choice")