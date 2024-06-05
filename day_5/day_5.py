import random as r

print("Welcome to password generator!")

letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "1234567890"
symbols = """+×÷=/_<>[]!@#$%^&*()-'":;,?`~\|{}"""
 
all = [letters, numbers, symbols]

length = int(input("How long should the password be?"))

numChar = int(input("How much characters should it contain?\n"))
numNum = int(input("How much numbers should it contain?\n"))
numSym = int(input("How much symbols should it contain?\n"))

if length < numChar + numNum + numSym:
	print("Error! Too much characters.")
	exit()

password = ""
list = []

while list.count(0) < numChar or list.count(1) < numNum or list.count(2) < numSym:
	password = ""
	list = []
	
	for i in range(0, length):
		n = r.randint(0, 2)
		m = r.randint(0, len(all[n])-1)
		password = password + all[n][m]
		list.append(n)
	
		
print("Your password has been generated:")
print(password)
		