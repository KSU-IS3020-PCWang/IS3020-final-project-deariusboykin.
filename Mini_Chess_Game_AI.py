# Dictionary
# The Dictionary Stores Each Chess Piece And Its Current Position On The Board.
# The Key Is The Piece Name (WK, BK, etc.).
# The Value Is a List Containing The Row and Column.
import csv

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


# This Function Creates and Displays the Chess Board
# update_board()
# Creates an empty 6x6 chess board.
# It loops through every piece in the dictionary and places
# each one in its correct position.
# Finally, it returns the completed board.

def update_board():
    board = [["." for _ in range(8)] for _ in range(8)]

    for piece, position in pieces.items():
        row, col = position
        board[row][col] = piece

    return board


# Display Board
# Calls update_board() To Get The Current Board.
# Prints The Column Numbers And Each Row So The Player
# Can See Where Every Piece Is Located.

def show_board():
    board = update_board()

    print("\n  0  1  2  3  4  5  6  7")

    for i, row in enumerate(board):
        print(i, " ".join(f"{square:>2}" for square in row))


# move_piece(player)
# Lets The Current Player Choose a Piece To Move.
# Checks If The Piece Exists.
# Makes Sure The Player Only Moves Their Own Pieces.
# Gets the new row and column from the user.
# Checks That The New Location Is On The Board.
# If An Enemy Piece Is On That Square, It Is Captured.
# Finally, Updates The Piece's Position In The Dictionary.

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


    # Check For Captures
    ## Remove The Captured Piece From The Dictionary.

    for enemy, position in list(pieces.items()):
        if position == [new_row, new_col]:

            if enemy[0] != piece[0]:
                print(piece, "captured", enemy)
                del pieces[enemy]

            else:
                print("You cannot capture your own piece")
                return


    # Move Piece
    # Update The Selected Piece With Its New Position.

    pieces[piece] = [new_row, new_col]


# Save Game
# Saves Every Piece And Its Position To a CSV file.
# This Lets The Player Continue The Game Later.

def save_game():

    with open("savegame.csv", "w", newline="") as file:
        writer = csv.writer(file)

        for piece, position in pieces.items():
            writer.writerow([piece, position[0], position[1]])

    print("Game saved!")


# Load game
# Opens The Saved File And Rebuilds The Pieces Dictionary.
# If No Save File Exists, An Error Message Is Displayed.

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


# Count Pieces
# Counts How Many White And Black Pieces Are Still On The Board.
# Displays The Totals After Each Turn.

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
# Checks If Either King Has Been Captured.
# If a Kng Is Missing, The Game Ends And a Winner Is Announced.

def check_game():

    if "WK" not in pieces:
        print("Black wins!")
        return False

    if "BK" not in pieces:
        print("White wins!")
        return False

    return True


# Main Game Loop
# Runs The Game Until The Player Quits Or a King Is Captured.
# Shows The Board, Displays The Menu,
# And Lets Players Move, Save, Load, Or Quit.

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

    # The Game Is Now Ready To Play.
    # Players Can Choose A Piece, Enter a Move,
    # And Take Turns Until A Winner Is Found.