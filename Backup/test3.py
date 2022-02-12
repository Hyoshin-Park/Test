from itertools import*
import math


num1 = int(input())

k = 1
count = 0
num_list = []
for i in permutations([1, num1], num1):
    num_list.append(i)
print(num_list)
    for j in i:
        if i[j] - j <= k:
            count += 1

print(count)
