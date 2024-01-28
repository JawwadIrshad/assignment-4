#Python Program to count unique values inside a list
def count_unique(list):
    return len(set(list))

my_list = [1, 2, 3, 4, 2, 3, 5, 6]
print(" unique values inside the list is:", count_unique(my_list))
