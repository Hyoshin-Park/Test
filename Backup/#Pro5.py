def check(num1, num2, num3):
    total = num1 + num2 + num3
    for i in range(2, total):
        if total % i == 0 : return False
    return True

def solution(nums):
    answer = 0
    for i in range(0, len(nums) - 2):
        for j in range(i+1, len(nums) - 1):
            for k in range(j+1, len(nums)):
                if check(nums[i], nums[j], nums[k]):
                    answer += 1
    return answer