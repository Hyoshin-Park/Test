#JYJ 1

width = int(input("Enter width: "))
length = int(input("Enter length: "))

square = lambda width, length:width * length
squareArea = square(width, length)
print(squareArea)

#JYJ 2

import math

print(math.fab(-4.5))
print(math.ceil(-4.5))
print(math.floor(-4.5))
print(math.trunc(-4.5))

#Yoo 1

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
