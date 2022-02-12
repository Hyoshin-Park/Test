nums = [72, 69, 76, 76, 79]

#버블 정렬 처음부터 차례로 비교하는 것

print(f"not sorted nums: {nums}") #정렬 되기

length = len(nums) - 1

for i in range(length): #숫자 하나씩 순차적으로 비교하며 큰 숫자는 밀어내기
    for j in range(length - i):
        if nums[j] > nums[j+1]: #앞 숫자가 더 큰 경우
            # temp = nums[j] #변수 두개값 바꾸기
            # nums[j] = nums[j+1]
            # nums[j + 1] = temp

            nums[j], nums[j+1] = nums[j+1], nums[j] #파이썬 기능으로 자리 바꾸기

 # [2, 7, 10, 0, 21]
 # [2, 7, 0, 10, 21]
 # [2, 0, 7, 10, 21]
 # [0, 2, 7, 10, 21]




    print(f"sorted nums: {nums}")
