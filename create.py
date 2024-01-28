import os

def create_file(file):
    with open(file, 'w') as file:
        file.write("my name is jawwad.\n")
        file.write("I am 20 year's old.\n")
        file.write("I love python programming.\n")

def read_file_to_list(file):
    with open(file, 'r') as file:
        lines = file.readlines()
    return lines
file = 'python.txt'
create_file(file)

lines_list = read_file_to_list(file)

print("Content of file as list:")
for line in lines_list:
    print(line.strip())

os.remove(file)
print(f"{file} has been removed.")
