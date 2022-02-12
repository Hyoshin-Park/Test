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
