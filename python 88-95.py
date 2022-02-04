#88

from array import*

nums = array("i", [])

for i in range(0, 5):

    intnum = int(input("Enter five number"))
    nums.append(intnum)

nums = sorted(nums)
nums.reverse()
print(nums)

#89

nums = array("i", [10, 15, 20, 25, 30])

for i in nums:
    print(i)

#90

nums = array("i", [])

n = 0
while n < 5:
    num = int(input("Enter number"))
    if num >= 10 and num <= 20:
        nums.append(num)
        n += 1
    else:
        print("Outside the range")
        continue
print("Thank you")
for i in nums:
    print(i)

#91

nums = array("i", [10, 10, 20, 20, 30])

print(nums)

inputNums = int(input("Choose a number: "))

#for value in nums:
#    if value not in inputNums:
#        print("That is not on the list")
#    else:
print(nums.count(inputNums))

#92

num1 = array("i", [])
num2 = array("i2", [5, 10, 15, 20, 25])

for i in range(0, 3):
    inputNums = int(input("Enter three numbers: "))
    num1.append(inputNums)

num1.extend(num2)
for i in num1:
    print(i)

#93

from array import*

num1 = array("i", [])
num2 = array("i2", [])

for i in range(0, 5):
    inputNums = int(input("Enter five numbers: "))
    num1.append(inputNums)

print(sorted(num1))

chooseNum = int(input("Pick one number: "))

num1.remove(chooseNum)
num2.append(chooseNum)

print(num1); print(num2)

#94

nums = array("i", [5, 10, 15, 20, 25])

print(nums)

flag = True

while flag:
    chooseNum = int(input("Pick one number: "))
    if chooseNum in nums:
        print(f"The numbers position is {nums.index(chooseNum)}")
        flag = False

    else:
        print("Pick a number in a array")
        continue

#95

nums = array("i", [5.14, 10.12, 15.14, 20.12, 25.15])

num = int(input("Enter a number between 2 and 5: "))
flag = True
while flag:
    if num < 2 and num > 5
        print("Out of range!!!!")
        num = int(input("Enter a number between 2 and 5: "))
    else:
        for i in nums:
            print(i / num)
        flag = False


from array import*
import math

nums = array("i", [])

for i in range(0, 5):
    inputNums = float(input("Enter number with xx.xx: "))

num = int(input("Enter a number between 2 and 5: "))
flag = True
while flag:
    if num < 2 and num > 5:
        print("Out of range!!!!")
        num = int(input("Enter a number between 2 and 5: "))
    else:
        break

for i in nums:
    print(round(i / num, 2))
