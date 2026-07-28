# creating the starting postions for the chess pieces
import csv

from Mini_Chess_Game_AI import turn

pieces = dict(WK=[7, 4], WQ=[7, 3], WR=[7, 0], WB=[7, 2], WN=[7, 1], BK=[0, 4], BQ=[0, 3], BR=[0, 7], BB=[0, 5],
              BN=[0, 6], BP={1, 4})

# Create board
def show_board(i=None):
    board = [["."for i in range(8)] for j in range(8)]

    for piece in pieces:
        row, col = pieces[piece]
        board[row][col] = pieces[piece]
        board[row][col] = piece

        print("\n 0 1 2 3 4 5 6 7 ")
        for row in range(8):
            print(i,board[i])

# Move Chess Piece
        def move_piece(turn):
            piece = input("Piece: ").upper()

            if piece in pieces:
                print("invalid piece")
                return
            if turn == "white" and piece[0] != "W":
                print("Move a white piece")
                return

        if turn == "Black" and piece[0] != "B":
                print("Move a black piece")
                return

def move_piece(player):
    piece = input("Enter piece: ")

    row = int(input("Row: "))
    col = int(input("Column: "))

    if row not in range(8) or col not in range(8):
        print("Invalid move")
        return

    for p in list(pieces):

        if pieces[p] == [row, col]:

            if p[0] == piece[0]:
                print("Can't capture your own piece")

                return

            print(piece, "captured", p)

            del pieces[p]

    pieces[piece] = [row, col]

def save_game(winner=None):

    with open("savegame.csv", "w", newline="") as file:
        writer = csv.writer(file)

        for piece, position in pieces.items():
            writer.writerow([piece, position[0], position[1]])

    def load_game():

        global pieces

        pieces = {}

        try:

            with open("savegame.csv") as file:

                reader = csv.reader(file)

                for row in reader:
                    pieces[row[0]] = [int(row[1]), int(row[2])]

        except:

            print("No save file")

        def winner():
            if "WK" not in pieces:
                print("Black Wins!!")
                return True

            if "BK" not in pieces:
                print("White Wins!!")
                return True

            return False

    turn = "White"

    while True:

        show_board()

        print("\n1.Move")

        print("2.Save")

        print("3.Load")

        print("4.Quit")

        choice = input("Choice: ")

        if choice == "1":

            move_piece(turn)

            if winner():
                break

            turn = "Black" if turn == "White" else "White"



        elif choice == "2":

            save_game()



        elif choice == "3":

            load_game()



        elif choice == "4":

            break



        else:

            print("Invalid option")