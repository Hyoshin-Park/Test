file = open("Names.txt", "a")

for i in range(0, 5):
    name = input("Enter five name")
    file.write(name + "\n")
file.close()
