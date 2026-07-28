# IS 3020 Final Project

## Student and Project Information

- Student name: DeArius Boykin
- GitHub username: deariusboykin
- Project title: Mini Chess Game
- Application purpose: Python-based chess learning application created for beginners who want to learn the game in a simple and easy way. It helps new players understand the basic rules, how each chess piece moves, and simple strategies, making it easier to build confidence and enjoy learning chess.

## How to Run the Application

Explain the required Python version, required files, and the exact steps for starting the application in PyCharm.

# The program requires Python 3.x and the main Python file where the code of the Mini Chess Game is stored. It also uses savegame.csv which is generated during the process of game saving.

# In order to launch the program in PyCharm:

# Open the project folder in PyCharm.
# Choose Python 3.x interpreter.
# Open the Mini Chess Game .py file.
# Press the green Run button or right-click the file and choose Run from the context menu.
# Play the game using the console menu.

## Major Features

List the major user-facing features implemented in the final application.

# The key functionalities offered by the Mini Chess Game application are as follows:

# Showing an 6x6 chess board with the location of pieces.
# Enabling players to move their pieces.
# Checking the turns such that each player moves his/her pieces.
# Taking opponent’s pieces.
# Calculating the number of pieces remaining on the board for both white and black pieces.
# Storing the current status of the game.
# Loading the stored game.
# Recognizing whether the player has won by taking the opponent’s king.
# Giving menu for moving, saving, loading, and quitting the game.

## Python Concepts Used

Explain how the application uses functions, collections, conditionals, loops, file persistence, and exception handling.

# Functionality is used in this program to structure the processes such as moving pieces, displaying the chessboard, and storing the game.
# Piece positions are stored in a dictionary, whereas conditions and loops are used to manage moves, turns, and game play.
# File management uses a CSV file for storing and retrieving games, avoiding any errors.

## Data Files

Describe each CSV or JSON file and provide a brief explanation of its fields.

# The application uses a single CSV file savegame.csv to store the saved games. Each entry in the file is a chess piece and its position.
# Fields:
# Piece: The name of the chess piece (such as WK for White King).
# Row: Row number at which the chess piece resides.
# Column: Column number at which the chess piece resides.
# The CSV file is used for saving the game state.

# Testing Summary

Describe the major scenarios tested, including invalid input and file-related errors.

#The major tests included moving legal pieces, moving illegal pieces, capturing opponent’s pieces, and win tests.
# Other tests that were carried out include input tests for wrong piece types and out-of-bounds board coordinates.
# The file test included saving a game, loading a saved game, and error handling of missing save file.

## AI Use

Complete `AI_USAGE.md` and summarize the most important AI-assisted improvements here.

# AI technology was utilized in debugging, explanations about the Python language, and structuring the code.
# Some of the areas where AI proved helpful include moves validation, save/load functionality, and displaying the board.
# The suggestions were evaluated before implementation.