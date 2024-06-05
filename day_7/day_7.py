import random as r
import day_7_sources as d7

def view():
	for j in display:
		print(j, end=" ")
	print()
	print(d7.ascii[mistakes])

print(d7.logo)

chosen_word = d7.words[r.randint(0,len(d7.words)-1)]

display = []
for char in chosen_word:
	display.append("_")
mistakes = 0

view()

gameOn = True

while gameOn:
	guess = input("Choose the letter:\n").lower()
	isNotCorrect = True

	if guess in display:
		print("You already guessed this letter!")
		view()
		continue

	for i in range(0, len(chosen_word)):
		if guess == chosen_word[i]:
			display[i] = chosen_word[i]
			isNotCorrect = False
			print("Good guess!")

	if isNotCorrect:
		mistakes = mistakes + 1
		print("The letter was not in the word. You lost one point!")

	view()

	if "_" not in display:
		print("You have won the game!")
		print(d7.medal)
		gameOn = False
	elif mistakes == 6:
		print("You have lost the game!")
		gameOn = False