import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
dic = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Provide a word: ")

codes = [dic[letter.upper()] for letter in word]

print(codes)
