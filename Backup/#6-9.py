nums = [7, 4, 8, 9, 2, 1]

#삽입정렬: 정렬되어 있는 자료 배열과 비교해서 정렬 위치를 찾는 것.

#오름차순
for i1 in range(1, len(nums)): #맨 앞에서 시작할 필요없으니 인덱스1 부터
    i2 = i1 - 1
    cNum = nums[i1]

    while nums[i2] > cNum and i2 >= 0: #i2 가 지금 인덱스 1값보다 작으면 위치를 바꾼다를 실행
        nums[i2 + 1] = nums[i2]

        i2 -= 1

    nums[i2 + 1] = cNum
# [5, 10, 2, 1, 0]
# [2, 5, 10, 1, 0]
# [1, 2, 5, 10, 0]
# [0, 1, 2, 5, 10]

    print(nums)

#내림차순

nums = [0, 1, 5, 10, 2]

for i1 in range(1, len(nums)):
    i2 = i1 - 1
    cNum = nums[i1]

    while nums[i2] < cNum and i2 >= 0:
        nums[i2 + 1] = nums[i2]

        i2 -= 1

    nums[i2 + 1] = cNum
# [1, 0, 5, 10, 2]
# [5, 1, 0, 10, 2]
# [10, 5, 1, 0, 2]
# [10, 5, 2, 1, 0]


    print(nums)
