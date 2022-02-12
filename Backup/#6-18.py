class MaxAlgorithm:

    def __init__(self, ns):
        self.nums = ns
        self.maxNum = 0
        self.maxNumIdx = 0

    def setMaxIdxAndNum(self):
        self.maxNum = self.nums[0]
        self.maxNumIdx = 0

        for i, n in enumerate(self.nums):
            if self.maxNum < n:
                self.maxNum = n
                self.maxNumIdx = i

    def getMaxNum(self):
        return self.maxNum

    def getMaxNumIdx(self):
        return self.maxNumIdx

import random

scores = []

for i in range(100):
    rn = random.randint(71, 100)
    if rn != 100: rn = rn - (rn % 5)
    scores.append(rn)

print(scores)

#최댓값

maxAlo = MaxAlgorithm(scores)

maxAlo.setMaxIdxAndNum()
maxNum = maxAlo.getMaxNum()

print(maxNum)

#인덱스 리스트 생성

indexes = [ 0 for i in range(maxNum + 1)]

print(indexes)

#인덱스 리스트에 빈도 저장

for n in scores:
    indexes[n] = indexes[n] + 1

print(f"index = {indexes}")

n= 1

while True:

    maxAlo = MaxAlgorithm(indexes)
    maxAlo.setMaxIdxAndNum()
    maxNum = maxAlo.getMaxNum()
    maxNumIdx = maxAlo.getMaxNumIdx()

    if maxNum == 0:
        break

    print(f"{maxNumIdx} happened {maxNum} times\t", end="")
    print(" + " * maxNum)

    indexes[maxNumIdx] = 0

    n += 1
