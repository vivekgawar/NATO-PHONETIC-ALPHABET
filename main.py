import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

stop_program = 0
while stop_program == 0:
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
        print(output_list)
        stop_program = 1
    except KeyError as error:
        print("Sorry, only letters in the alphabet please.")
        stop_program = 0
