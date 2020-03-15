
#Unit 3/End of unit project - hangman
from random import *

class hangman:

	def __init__(self):
		self.answer = "secret" # SET THE HANGMAN WORD HERE
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

	def play(self):
		print("Welcome to hangman! Your opponent has chosen the secret word,\n and you will have to guess it before the hangman is drawn out. \nThis means you get 5 wrong guesses and a final chance to guess the whole word.\n Good luck!")
		print("The word is " + str(len(self.answer)) + " letters long.\n")

		while self.wrong_guesses < 6: # users get 6 total WRONG guesses

			# print current letters and hangman picture
			self.print_hangman()
			guess = input("Guess a letter: ")
			if not self.valid_guess(guess):
				print("Guess was not valid!")
				continue # re-enter while loop

			# if guess is valid, check if player has guessed it before
			if guess in self.correct_letters or guess in self.incorrect_letters:
				print("You already guessed that letter!\n")
		        # re-enters while loop after execution

		    # if we've made it this far (guess was valid, not previously guessed), record guess
			else:
				self.record_guess(guess)
				# if the letters guessed are the same letters as in the word, the player won!
				if self.correct_letters == self.answer_letters:
					self.user_won()
					break

		# if user has 6 incorrect guesses, the opponent won!
		self.print_hangman()
		if self.wrong_guesses >= 6:
			self.opponent_won()

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

	def valid_guess(self, guess):
		if len(guess) != 1 or guess.isdigit():
			return False
		return True

	def record_guess(self, guess):
		if guess in self.answer:
			self.correct_letters.add(guess) # add letter to set of correct letters guessed
		else:
			self.incorrect_letters.add(guess) # add letter to set of incorrect letters guessed
			self.wrong_guesses += 1 # increment number of wrong guesses
			print("Sorry, that letter isn't in the word.")

	def user_won(self):
		print("You won! The word is " + self.answer)

	def opponent_won(self):
		print("Your opponent beat you! The word was " + self.answer)

# run game
hangman = hangman()
hangman.play()
