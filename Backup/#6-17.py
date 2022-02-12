class MaxAlgorithm: #최대값 알고리즘


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

nums = [1, 3, 7, 6, 7, 7, 7, 12, 12, 17]

maxAlo = MaxAlgorithm(nums) #nums의 최대값 구하기

maxAlo.setMaxIdxAndNum()
maxNum = maxAlo.getMaxNum() #maxNum을 가져와서 17가져오기

print(maxNum)# 17

indexes = [ 0 for i in range(maxNum + 1)]
# 최대값보다 하나 큰 인덱스만큼 0으로  리스트 만들기

print(indexes)

for n in nums:#nums를 indexes에 넣어주며 갯수만큼 더하는 과정
    indexes[n] = indexes[n] + 1

print(indexes)

maxAlo = MaxAlgorithm(indexes)#indexes에서의 맥스값 구하기
maxAlo.setMaxIdxAndNum()
maxNum = maxAlo.getMaxNum()
maxNumIdx = maxAlo.getMaxNumIdx()#그 맥스값의 인덱스 구하기

print(f"maxnum: {maxNum}")
print(f"maxnumIdx: {maxNumIdx}")

print(f"{maxNumIdx} happened {maxNum} times")
