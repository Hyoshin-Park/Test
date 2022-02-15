#118

def countNum():
    num = int(input("Input Number: "))
    return num


def orderNum():

    num = countNum()
    list = []
    for i in range(1, num + 1):
        list.append(i)
    return list


print(orderNum())

#119
import random

def compNum():
    lowerNum = int(input("Enter lower number: "))
    higherNum = int(input("Enter higher number: "))
    ranSam = random.randint(lowerNum, higherNum)

    return ranSam

def match():
    print("I am thinking of a number.....")
    askNum = int(input("What number are you thinking?: "))
    return askNum

def Befmain(ranSam, askNum):
    flag = True
    while flag:
        if ranSam == askNum:
            print("Correct, you win")
            flag = False
        elif ranSam > askNum:
            askNum = int(input("lower number! Try again!: "))
        elif ranSam < askNum:
            askNum = int(input("higher number! Try again!: "))

def main():
    ranSam = compNum()
    askNum = match()
    Befmain(ranSam, askNum)

main()

#120

import random

def add():
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)
    result = num1 + num2
    askNum = int(input(f"What is {num1} + {num2} = ? "))
    print(f"Your answer is {askNum}, The answer is {result}")
    total = (askNum, result)
    return total


def sub():
    num1 = random.randint(25, 50)
    num2 = random.randint(1, 25)
    result = num1 - num2
    askNum = int(input(f"What is {num1} - {num2} = ? "))
    print(f"Your answer is {askNum}, The answer is {result}")
    total = (askNum, result)
    return total

def check(askNum, result):

    if askNum == result:
        print("Correct")
    elif askNum != result:
        print(f"Incorrect, the answer is {result}")


def main():
    ask = int(input("1) addition \n2)Subtraction \nEnter 1 or 2: "))
    if ask == 1:
        askNum, result= add()
        check(askNum, result)
    elif ask == 2:
        askNum, result= sub()
        check(askNum, result)
    else:
        print("select 1 or 2 please")



main()

#121
