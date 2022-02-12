def mSort(ns, asc=True):

    if len(ns) < 2:
        return ns


    midIdx = len(ns) // 2
    leftNums = mSort(ns[0:midIdx], asc=asc)
    rightNums = mSort(ns[midIdx:len(ns)], asc=asc)

    mergeNums = []
    leftIdx = 0
    rightIdx = 0
    while leftIdx < len(leftNums) and rightIdx < len(rightNums):

        if asc:
            if leftNums[leftIdx] < rightNums[rightIdx]:
                mergeNums.append(leftNums[leftIdx])
                leftIdx += 1
            else:
                mergeNums.append(rightNums[rightIdx])
                rightIdx += 1
        else:
            if leftNums[leftIdx] > rightNums[rightIdx]:
                mergeNums.append(leftNums[leftIdx])
                leftIdx += 1
            else:
                mergeNums.append(rightNums[rightIdx])
                rightIdx += 1

    mergeNums = mergeNums + leftNums[leftIdx: ]
    mergeNums = mergeNums + rightNums[rightIdx: ]

    return mergeNums


import random as rd

rNums = rd.sample(range(1, 101), 10)

print(f"not sorted rNums: {rNums}")
print(f"sorted rNums ASC: {mSort(rNums)}")
print(f"sorted rNums DESC: {mSort(rNums, asc=False)}")
