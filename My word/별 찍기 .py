num1 = int(input("Enter a number"))

for i in range(1, num1 + 1):
    print("*" * i)

    num = int(input("Enter a test number: "))


    for i in range(1, num + 1):
        num1 = int(input("Enter a number"))
        num2 = int(input("Enter a number1"))
        number = num1 + num2
        print(f"Case #{i}: {num1} + {num2} = {number} "  )



num1 = int(input("Enter a number"))

for i in range(1, num1 + 1):
    print(" " * (num1 - i) + "*" * i)
