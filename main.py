from os import system
from time import sleep
import random
from hangman_art import stages, logo
from hangman_words import word_list

def playGame():
	answer = random.choice(word_list).upper()
	placeholder = "_" * len(answer)
	lives = 6
	print(logo)
	while lives != 0 and not did_player_win(answer, placeholder):
		
		print(f"Currently: {placeholder}\n")
		guess = input("Guess a letter: ").upper()
		system('cls')

		if guess in answer:
			placeholder = updatePlaceholder(placeholder, answer, guess)
			print(f"Correct!")
		else:
			print(f"Wrong!")
			lives -= 1
		print(f"Lives: {lives}")		
		print(stages[lives])
		

	if lives == 0:
		print(f"You didn't guess the word \"{answer}\". Better luck next time!\n")
	else:
		print(f"Congratulations! You guessed the word \"{answer}\"")
	sleep(10)


def updatePlaceholder(placeholder, answer, guess):
	placeholder_list = list(placeholder)
	for i in range(len(answer)):
		if answer[i] == guess:
			placeholder_list[i] = guess
	placeholder = ''.join(placeholder_list)
	return placeholder

def did_player_win(answer, placeholder):
	if answer == placeholder:
		return True
	return False

playGame()		