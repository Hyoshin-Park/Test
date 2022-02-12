class cal:
    def add(n1, n2):
        return n1 + n2

    def sub(n1, n2):
        return n1 - n2

    def mul(n1, n2):
        return n1 * n2

    def div(n1, n2):
        return n1 / n2

num1 = int(input("Enter number: "))
num2 = int(input("Enter number2: "))

print(cal.add(num1, num2))
print(cal.sub(num1, num2))
print(cal.mul(num1, num2))
print(cal.div(num1, num2))
