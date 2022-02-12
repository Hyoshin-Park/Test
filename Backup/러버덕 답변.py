#JYJ 1

x = 1
num_list = []
num_list1 = []
while x < 101:
    if x % 7 == 0:
        num_list.append(x)
    elif x % 9 == 0:
        num_list1.append(x)
    x += 1

print(f"7의 배수는: {num_list}")
print(f"9의 배수는: {num_list1}")

#JYJ 2

inputX = int(input("구구단을 실행할 숫자: "))
x = 0
while x <10 :

    result = inputX * x
    print("{} * {} = {}".format(inputX, x, result))
    x += 1

#Yoo 1

inputX = int(input("구구단을 실행할 숫자: "))

for n in range(1, 10):
    result = inputX * n
    print("{} * {} = {}".format(inputX, n, result))


#Yoo 2

n = int(input("출력할 숫자: "))

num = 1

while n >= num:
    print(num)
    num += 1

    
