"""Script for automatic writing letters with names listed in file."""

with open("./Input/Letters/starting_letter.txt") as f1:
    str1 = f1.read()

with open("./Input/Names/invited_names.txt") as f2:
    str2 = f2.read()

str1 = str1.split("[name]")
str2 = str2.split("\n")

for name in str2:
    str3 = str1[0] + name + str1[1]
    path = "./Output/ReadyToSend/letter_for_" + name + ".txt"
    with open(path, mode="w") as f3:
        f3.write(str3)
