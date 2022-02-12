shoe_dict = {"Nike":{"age":23, "shoeSize":255},
"Adidas":{"age":25, "shoeSize":265},
"Puma":{"age":15, "shoeSize":220},
"Newbalance":{"age":27, "shoeSize":280}}

askDel = input("What do you want to delete?(A name): ").capitalize()

del shoe_dict[askDel]

for i in shoe_dict:
    print(shoe_dict[i])
