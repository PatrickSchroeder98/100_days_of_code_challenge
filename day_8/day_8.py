import day_8_source as d8


def crypt(message, shift, encrypt):
	A = [d8.alphabet, d8.alphabetUpper]
	s = ""
	for char in message:
		if char.isupper():
			a = A[1]
		else:
			a = A[0]

		if char not in a:
			s = s + char
			continue

		if encrypt:
			n = a.index(char) + shift
		else:
			n = a.index(char) - shift
			
		if n >= len(a) or n < 0:
			s = s + a[n % len(a)]
		else:
			s = s + a[n]
	return s


def app():
	direction = ""
	
	while direction != "encode" and direction != "decode":
		direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

	message = input("Type message:\n")
	shift = int(input("Type the value of shift:\n"))
	if direction == "encode":
		print( "Your encrypted message is: " + crypt(message, shift, True))
	else:
		print( "Your decrypted message is: " + crypt(message, shift, False))
	
	choice = ""
	while choice != "yes" and choice != "no":
		choice = input("Continue? Type 'yes' to continue, type 'no' to exit:\n").lower()
		
	if choice == "yes":
		app()


print(d8.caesar + d8.cipher)
app()
