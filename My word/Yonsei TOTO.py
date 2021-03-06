sub, score = map(int, input().split())

cnt = 0

cnt_list = []

for i in range(sub):
    apply, capa = map(int, input().split())
    score_list = list(map(int, input().split()))
    if apply < capa:
        cnt_list.append(1)
    else:
        score_list.sort(reverse=True)
        cnt_list.append(score_list[capa-1])
        

cnt_list.sort()

for i in range(sub):
    if score - cnt_list[i] >= 0:
        score -= cnt_list[i]
        cnt += 1
    
print(cnt)

###



import sys
input = sys.stdin.readline


def getMinMileage(p, l, nums):
    minMileageIndex = p - l
    if minMileageIndex < 0:
        return 1
    else:
        nums.sort()
        return nums[minMileageIndex]


def getMaxClassCount(m, mileages):
    maxClassCount = 0
    mileages.sort()

    for mileage in mileages:
        m -= mileage
        if m < 0:
            break

        maxClassCount += 1

    return maxClassCount


if __name__ == '__main__':
    n, m = map(int, input().split())
    mileages = []

    # input / set mileages
    for i in range(n):
        p, l = map(int, input().split())
        nums = list(map(int, input().split()))

        mileages.append(getMinMileage(p, l, nums))

    # spend mileages / output
    maxClassCount = getMaxClassCount(m, mileages)
    print(maxClassCount)











