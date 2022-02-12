#105


file = open("Number.txt", "a")
file.write("1\n")
file.write("2\n")
file.write("3\n")
file.write("4\n")
file.write("5\n")
file.close()

#106

file = open("Names.txt", "a")

for i in range(0, 5):
    name = input("Enter five name")
    file.write(name + "\n")
file.close()

#107

file = open("Names.txt", "a")

for i in range(0, 5):
    name = input("Enter five name")
    file.write(name + "\n")
file.close()

file = open("Names.txt", "r")
print(file.read())

file.close()

#108

file = open("Names.txt", "a")

name = input("Enter name")
file.write(name)
file.close()

file = open("Names.txt", "r")
print(file.read())

file.close()

#109

print("1) Create a new file \n2) Display the file")
print("3) Add a new item to the file \nMake a selection 1,2 or 3: ")

choice = int(input("Enter number: "))

if choice == 1:
    sub = input("Enter subject to create: ")
    file = open("Subject.txt", "w")
    file.write(sub)
    file.close()

elif choice == 2:
    file = open("Subject.txt", "r")
    print(file.read())
    file.close()

elif choice == 3:
    sub = input("Enter subject to create: ")
    file = open("Subject.txt", "a")
    file.write(f"\n{sub}")
    file.close()
    file = open("Subject.txt", "r")
    print(file.read())
    file.close()
