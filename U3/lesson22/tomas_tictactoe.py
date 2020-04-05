'''
Unit 3/End-of-unit-game
A tic-tac-toe game to be played with two players!

'''

import random
import os

def clearscreen():
	os.system('cls' if os.name == 'nt' else 'clear')

class tic_tac_toe:

	'''
	TODO: Set variables for whether or not the game is playing and the tic-tac-toe board
	'''
	def __init__(self):
		# Think about what each of these things should be at the very beginning, before the game has even started
		# TODO: set a variable to false for whether or not the game is currently being played
		self.game_is_playing =
		# TODO: create a list (size 9) of strings containing a single space to hold the pieces on the board
		self.board =

	'''
	TODO:
	1) Run a loop as long as the game is playing
	2) Inside, print the current board,
	3) Record the current player's move,
	4) Check if that player has won (after their move),
	5) Check if the board is full (after their move),
	6) and switch whose turn it is once their move is over
	'''
	def play(self):

		# Feel free to change the print statement below to show your own rules!"
		print("Welcome to Tic-Tac-Toe! Choose a player to be Player 1 and Player 2. Player 1 wil be x's, and player 2 will be o's.")
		print("Player 1 will go first.")

		# TODO: set the self.game_is_playing variable to True
		# TODO: create a variable called player and assign it with 1, this represents player 1's turn

		# TODO: Create a while loop runs as long as self.game_is_playing is True

			# TODO: using a class method, print the game board
			# TODO: print whose turn it is - remember you set this variable above
			# TODO: get the player's move (using another class method) # hint: use indices
			# TODO: record the player's move (using another method)
			# TODO: clear the screen using the global variable

			# TODO: Check if the player is a winner using a class method
				# print out the board using the class method
				# If so, print out that the player has one
				# Set self.game_is_playing to false so that the loop won't continue to run

			# TODO: Check if the board is now full
				# print out the board using the class method
				# If so, print out that there is a cat's game
				# Set self.game_is_playing to false

			# TODO: if no winners (and no cat's game), switch whose turn it is by assigning the player with the other player

	'''
	TODO: Replace the underlines with each "piece" of self.board
	# Don't worry too much about the other print statements!
	# When you start testing the game it will start to make sense
	We want it to be like this:
	1 | 2 | 3
	4 | 5 | 6
	7 | 8 | 9
	'''
	def print_board(self):
		print('   |   |')
		print(' ' + _____________ + ' | ' + _____________ + ' | ' +  _____________)

		print('-----------')
		print(' ' + _____________ + ' | ' + _____________ + ' | ' +  _____________)

		print('   |   |')
		print('-----------')

		print(' ' + _____________ + ' | ' + _____________ + ' | ' +  _____________)
		print('   |   |')

	'''
	TODO:
	1) Record where the player would like to move (spaces 1-9)
	2) Continue to record the player's move if they enter an invalid number
	   (i.e., a non-digit, OR a space that already has a piece on it)
	3) Return the player's VALID move
	'''
	def get_player_move(self):
		# TODO: create a variable called move and use the input() function to record the player's move

		# TODO: check if the player inputs a valid number 1-9, and ask the player for another number if not
		# hint: think about what is not a valid move and keep asking the player
		# ...to submit a new move WHILE the move is not a valid number 1-9

		# if it can be converted to an integer...
		while int(move) not in {1,2,3,4,5,6,7,8,9} or not self.space_is_free(int(move)):
			move = input("Please enter a valid move: ")

		# TODO: Finally, return the move (as an integer)

	'''
	TODO: Update the game board with the player's move
	'''
	def move(self, player, move): #update game board
		# TODO: Create a variable called piece and initialize it to an empty string
		# Set it to "x" if player is 1, and "o" if player is 2

		# TODO: move the player's piece you just created onto the board (using self.board)

	'''
	TODO: Check if the space on the board is free to move a piece there
		  ('move' is the space the player wants to move to)
	'''
	def space_is_free(self, move): #checks if a space on the board is free
		# TODO: return true if the board has an empty space where the player wants to move...
		# ... and false if there is a piece there

	'''
	TODO: Check if the board is full of pieces (to see if there is a cat's game)
	'''
	def board_is_full(self): #checks if the board is full
		# TODO: Loop through self.board
		# If any pieces are the empty string, return false. Otherwise, return true (meaning no spaces are emptys)

    # checks if a player makes 3 in a row
	def is_winner(self, player):
		piece = ""
		if player == 1:
			piece = "x"
		else:
			piece = "o"

		return ((self.board[6] == piece and self.board[7] == piece and self.board[8] == piece) or
		(self.board[3] == piece and self.board[4] == piece and self.board[5] == piece) or # across the middle
		(self.board[0] == piece and self.board[1] == piece and self.board[2] == piece) or # across the bottom
		(self.board[6] == piece and self.board[3] == piece and self.board[0] == piece) or # down the left side
		(self.board[7] == piece and self.board[4] == piece and self.board[1] == piece) or # down the middle
		(self.board[8] == piece and self.board[5] == piece and self.board[2] == piece) or # down the right side
		(self.board[6] == piece and self.board[4] == piece and self.board[2] == piece) or # diagonal
		(self.board[8] == piece and self.board[4] == piece and self.board[0] == piece)) # diagonal

	'''
	TODO: Switch whose turn it is
	'''
	def switch_player(self, player):
		# TODO: if the current player is 1, return 2
		# Otherwise, return 1


# TODO: run the game!
# Because we're using classes now, create an instance of the tic_tac_toe class...
# ... and then call the play method on it.
