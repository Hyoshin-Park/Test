#103

shoe_dict = {"Nike":{"age":23, "shoeSize":255},
"Adidas":{"age":25, "shoeSize":265},
"Puma":{"age":15, "shoeSize":220},
"Newbalance":{"age":27, "shoeSize":280}}

for i in shoe_dict:
    print(f"Age is {shoe_dict[i]['age']}")


#104

shoe_dict = {"Nike":{"age":23, "shoeSize":255},
"Adidas":{"age":25, "shoeSize":265},
"Puma":{"age":15, "shoeSize":220},
"Newbalance":{"age":27, "shoeSize":280}}

askDel = input("What do you want to delete?(A name): ").capitalize()

del shoe_dict[askDel]

for i in shoe_dict:
    print(shoe_dict[i])


#102

dict = {}

for i in range(0, 4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoeSize = int(input("Enter shoeSize: "))
    dict[name] = {'Age': age, 'Shoe size': shoeSize}

askName = input("Enter name: ")
print(dict[askName])

#103

dict = {}

for i in range(0, 4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoeSize = int(input("Enter shoeSize: "))
    dict[name] = {'Age': age, 'Shoe size': shoeSize}


for name in dict:
    print(name,':', dict[name]["Age"])


#104

dict = {}

for i in range(0, 4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoeSize = int(input("Enter shoeSize: "))
    dict[name] = {'Age': age, 'Shoe size': shoeSize}


nameDel = input("What do you want to delete?: ")
del dict[nameDel]

for name in dict:
    
    print(name, dict[name])
