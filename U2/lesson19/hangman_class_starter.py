
#Unit 3/End of unit project - hangman
from random import *

class hangman:

	def __init__(self):
		self.answer = "secret" # SET THE HANGMAN WORD HERE (secret is just an example)
		self.wrong_guesses = 0 # number of wrong guesses made by the player
		self.answer_letters = {i for i in self.answer} # set of letters in the answer -> {'s','e','c','r','t'}
		self.correct_letters = set() # guessed leters in the word
		self.incorrect_letters = set() # guesses letters not in the word
		self.board = ['''
  +----+
  |    |
       |
       |
       |
       |
==========''','''
  +----+
  |    |
  O    |
       |
       |
       |
==========''','''
  +----+
  |    |
  O    |
  |    |
       |
       |
==========''','''
  +----+
  |    |
  O    |
 /|    |
       |
       |
==========''','''
  +----+
  |    |
  O    |
 /|\   |
       |
       |
==========''','''
  +----+
  |    |
  O    |
 /|\   |
 /     |
       |
==========''','''
  +----+
  |    |
  O    |
 /|\   |
 / \   |
       |
==========''']

	'''
	TODO:
	1) Set variables for the number of incorrect guesses, the letters in the answer (hint: use a set!),
	 the correct letters the player has guessed, and the incorrect letters the player has guessed
	2) Write a loop to deal with each guess (hint: use a while loop!)
	3) In each loop iteration, print the current hangman drawing and record the player's guess
	'''
	def play(self):
		print "Welcome to hangman! Your opponent has chosen the secret word, \n and you will have to guess it before the hangman is drawn out. \nThis means you get 5 wrong guesses and a final chance to guess the whole word.\n Good luck!"
		print "The word is " + str(len(self.answer)) + " letters long.\n"

		while self.wrong_guesses < 6: # users get 6 total WRONG guesses

			# TODO: call print_hangman() to print correct hangman picture

			# TODO: record the player's guess using input()

			if not self.valid_guess(guess):
				# TODO: print out that the guess was not valid!
				continue
			# if guess is valid, check if player has guessed it before
			if guess in self.correct_letters or guess in self.incorrect_letters:
				print("You already guessed that letter!\n")
		        # re-enters while loop after execution
			else:
			# if not, record the guess by calling record_guess()

			# TODO: within the else statement, check if the player's correct guesses match the letters in the answer
			# (hint: compare the sets)
				# if so, call user_won() then break out of the loop

  		# If we exit the loop the user has lost
  		# TODO: call print_hangman()
		# TODO: if the number of wrong guess >= 6, call computer_won()

	def print_hangman(self):
		print(self.board[self.wrong_guesses]) # print current hangman drawing
		current_word = "\n"
		# look through answer, print out letters in the answer player has guessed correctly
		for i in self.answer:
			if i in self.correct_letters:
				current_word += i
			else:
				current_word += "_"
		print(current_word + "\n")

	'''
	TODO:
	1) Check if a guess is valid (i.e., only 1 character long, not a non-digit)
	'''
	def valid_guess(self, guess):
		# TODO: return false if the length of the guess is not 1

		# TODO: check if the guess is a digit by calling guess.isdigit(), return false if it is

		# TODO: return true

	'''
	TODO:
	1) If the player's guess is in the answer, add the guess to the correct letters
	2) Otherwise, add the guess to the incorrect letters and add 1 to the wrong_guesses variable
	3) Return the number of wrong guesses
	'''
	def record_guess(self, guess):
		if guess in self.answer:
			# TODO: if so, add letter to the set of correct letters guessed
		else:
			# TODO: otherwise, add it to the self.incorrect_letters
			self.wrong_guesses += 1 # increment number of wrong guesses
			print("Sorry, that letter isn't in the word.")


	'''
	TODO:
	1) Print out that the player has won and include the answer
	'''
	def user_won(self):

	'''
	TODO:
	1) Print out that you have won (include what the answer was!)
	'''
	def opponent_won(self):


# TODO: Run the game! Initialize an object of the class and call play()
