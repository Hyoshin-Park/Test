num = int(input())

num = 1000 - num 
count = 0

list = [500, 100, 50, 10, 5, 1]

for nums in list:
    count += num // nums
    num %= nums


print(count)