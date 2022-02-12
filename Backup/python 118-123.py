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
