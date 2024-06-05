import random as r

gameOn = True 
names = ["rock", "paper", "scissors"]

while gameOn:
	choice = -1
	while choice > 2 or choice < 0:
		print("What do you choose - rock, paper or scissors (0, 1 or 2)?")
		choice = int(input())
	print(f"You have chosen {names[choice]}")
	n = r.randint(0, 2)
	print(f"Your opponent have chosen {names[n]}")
	
	if choice == n:
		print("Tie!")
	elif choice == 0 and n == 2:
		print("You win!")
	elif n == 0 and choice == 2:
		print("You lose!")
	elif n > choice:
		print("You lose!")
	else:
		print("You win!")
	
	j = input("Type 'y' to play again.\n ")
	if j != "y":
		gameOn = False 
	