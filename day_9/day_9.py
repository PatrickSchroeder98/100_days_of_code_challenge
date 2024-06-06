# The program needs to be run in Windows terminal, the IDE console will not be cleared
import os
import day_9_sources as d9
def bid():
	askOn = True 
	dict = {}
	
	while askOn:
		name = input("What is your name?\n")
		isNotOK = True
		while isNotOK:
			try:
				bid = int(input("What is your bid?\n$"))
			except:
				print("Error! This is not a number.")
			else:
				isNotOK = False
		dict.update({name: bid})
		choice = input("Type yes if there are other people who want to bid.\n").lower()
		os.system('cls')
		
		if choice != "yes":
			askOn = False
	return dict


def calc(dict):
	temp = ["", 0]
	for key in dict:
		if temp[1] < dict[key]:
			temp[0] = key
			temp[1] = dict[key]
	return temp


print(d9.gavel)
print("Welcome to secret auction!")
dict = bid()
s = calc(dict)
print(f"Auction wins {s[0]}, who bid {s[1]}$!")

