def copy_file(my_file, computer_file):
    with open(my_file, 'r') as source:
        with open(computer_file, 'w') as computer:
            for line in source:
                computer.write(line)

my_file = 'python.txt'
computer_file = 'banoqabil.txt'

with open(my_file, 'w') as file:
    file.write("This is the content of my_file.")

copy_file(my_file, computer_file)
print("File contents copied successfully!")

import os
os.remove(my_file)
os.remove(computer_file)


