datas = [3, 2, 5, 7, 9, 1, 0, 8, 6, 4]



searchDatas = int(input("Enter number: "))
searchIdx = -1

n = 0
while True:

        if n == len(datas):
            searchIdx = -1
            break

        elif datas[n] == searchDatas:
            searchIdx = n
            break

        n += 1

print(f"searchIdx: {searchIdx}")
