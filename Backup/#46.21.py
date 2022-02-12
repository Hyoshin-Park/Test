import random

nums = random.sample(range(0,100), 10)

print(nums)
total = 0
for n in nums:
    total += n

avg = total / len(nums)

print(avg)

#50이상 90이하들의 평균

import random

nums = random.sample(range(0,100), 30)

print(nums)

for n in nums:
    if n >= 50 and n <= 90:
        total += n

avg = total / len(nums)

print(round(avg, 2))

#정수들의 평균

nums = [3.14, 4, 52, 4.2, 5.43, 11, 34]

targetNums = []

total = 0

for n in nums:
    if n - int(n) == 0: #실수는    "if n - int(n) != 0"
        total += n
        targetNums.append(n)


avg = total / len(targetNums)
print(targetNums)
print(round(avg, 2))
