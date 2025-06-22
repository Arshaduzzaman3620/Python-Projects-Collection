import pandas

# Load the CSV
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create phonetic dictionary
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Optional: print the dictionary to check
# print(phonetic_dict)

# Get user input and convert to phonetic code
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
