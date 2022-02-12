N, M = map(int, input().split())
list = []
list1 = []
for i in range(M):
    num1, num2 = map(int, input().split())
    list.append([num1, num2])

print(list)

K = int(input())

for man, vote in list:
    list1.append(vote)


list2 = []
for l in list1:
    if list1.count(l) >= K:
        #print(f"{l} has been voted")
        list2.append(l)

for b in list2:
    count = {}
    for x, y in enumerate(list):
        for t in range(N):
            if b in y:
                count[x] += 1
            else:
                count[x] = 0

print(count)

#
# count0 = 0
# for x in range(len(list)):
#     if l in list[x][1]:
#         count0 += 1
#         print(f"{list[x][0]} 학생은 {count0}통")
