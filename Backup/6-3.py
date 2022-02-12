nums = [4, 10, 22, 5, 0, 17, 7, 11, 9, 61, 88]

print(f"nums: {nums}")

nums.sort()

print(nums)
searchNums = int(input())
searchIdx = -1

staIdx = 0
endIdx = len(nums) - 1
midIdx = (staIdx + endIdx) // 2
midVal = nums[midIdx]

while searchNums <= nums[len(nums) - 1] and searchNums >= nums[0]:

    if searchNums == nums[len(nums) - 1]:
        searchIdx = len(nums) - 1
        break

    if searchNums > midVal:
        staIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = nums[midIdx]

    elif searchNums < midVal:
        endIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = nums[midIdx]

    elif searchNums == midVal:
        searchIdx = midVal
        break

print(f"searchIdx: {searchIdx}")
