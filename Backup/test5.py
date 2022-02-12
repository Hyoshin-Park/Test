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
