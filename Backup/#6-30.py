def qSort(ns, asc=True):

    if len(ns) < 2:
        return ns


    midIdx = len(ns) // 2
    midVal = ns[midIdx]


    smallNums = []
    sameNums = []
    bigNums = []

    for n in ns:
        if n < midVal:
            smallNums.append(n)
        elif n == midVal:
            sameNums.append(n)
        else:
            bigNums.append(n)

    if asc:
        return qSort(smallNums, asc=asc) + sameNums + qSort(bigNums, asc=asc)
    else:
         return qSort(bigNums, asc=asc) + sameNums + qSort(smallNums, asc=asc)


import random as rd

rNums = rd.sample(range(1, 100), 10)
print(rNums)

print(qSort(rNums))
print(qSort(rNums, asc=False))
