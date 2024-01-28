 #generate a dictiomary
num= int(input("Type a number: "))

num_Dict = {}
for i in range(1, num+1):
    num_Dict[i] = i*i

print("Dictionary:",num_Dict)