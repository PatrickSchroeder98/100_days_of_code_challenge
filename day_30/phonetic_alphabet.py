import pandas

data = pandas.read_csv("../day_26/nato_phonetic_alphabet.csv")
dic = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input("Provide a word: ")
    try:
        codes = [dic[letter.upper()] for letter in word]
    except KeyError:
        print("Error! Provide only letters!")
        generate_phonetic()
    else:
        print(codes)


generate_phonetic()
