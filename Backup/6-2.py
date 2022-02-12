nums = [4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9]

print(nums)
print(len(nums))

searchNums = int(input())
searchIdx = -1

nums.append(searchNums)

n=0
while True:
    if nums[n] == searchNums:
        if n != len(nums) - 1:
            searchIdx = n
        break

    n += 1

print(f"nums: {nums}")
print(f"length: {len(nums)}")
print(f"searchIdx: {searchIdx}")

if searchIdx < 0:
    print("not search Index")
else:
    print("Searched Index")



nums = [4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9]

print(nums)
print(len(nums))

searchNums = int(input())
searchIdxs = []

def searchNumber(tempNums):
    searchNums = int(input())
    searchIdxs = []

    tempNums.append(searchNums)

    n=0
    while True:
        if tempNums[n] == searchNums:
            if n != len(tempNums) - 1:
                searchIdxs.append(n)
            else:
                break

        n += 1

    return searchIdxs


print(f"nums: {nums}")
print(f"length: {len(nums)}")
print(f"searchIdxs: {searchIdxs}")

# if searchIdx < 0:
#     print("not search Index")
# else:
#     print("Searched Index")
