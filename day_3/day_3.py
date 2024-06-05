import day_3_sources as d3

print("Welcome to the treasure island. Your mission is to find a treasure.")

print(d3.island)
choice = input("You are on the crosroad. Do you want to go left or right?\n").lower()
if choice == "left":
	print(d3.river)
	choice = input("You reached the river. Do you want to wait for a boat or swim?\n").lower()
	if choice == "wait":
		print(d3.door)
		choice = input("You reached the red, blue and yellow door. Which one do you want to open?\n").lower()
		if choice == "red":
			print("That room is on fire. Game over!")
			print(d3.fire)
		elif choice == "blue":
			print("That room is full of beasts. Game over!")
			print(d3.beast)
		elif choice == "yellow":
			print("You found the treasure. You have won the game!")
			print(d3.treasure)
		else:
			print("Unrecognized answer. Game over!")
	elif choice == "swim":
		print("You were eaten by a crocodile. Game over!")
		print(d3.crocodile)
	else:
		print("Unrecognized answer. Game over!")
elif choice == "right":
	print("Bandits attacked you. Game over!")
	print(d3.bandit)
else:
	print("Unrecognized answer. Game over!")