def create_alphabet_file(file_path, letters_per_line):
    with open(file_path, 'w') as file:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(0, len(alphabet), letters_per_line):
            file.write(alphabet[i:i+letters_per_line] + '\n')

file_path = 'alphabet.txt'
letters_per_line = 7
create_alphabet_file(file_path, letters_per_line)
print("Alphabet file created successfully!")

