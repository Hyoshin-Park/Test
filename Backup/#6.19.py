import random

nums = random.sample(range(0, 50), 20)

print(nums)
inputNum = int(input("input number"))

nearNum = 0
minNum = 50

for n in nums: # inputNum와의 차이를 구하기
    absNum = abs(n - inputNum)# abs는 절대값

    if absNum < minNum: #가장 작은 차이를 구하는 과정
        minNum = absNum #가장 작은 숫자를 찾을 때까지 새로운걸 대입
        nearNum = n

print(f"{nearNum}")
