N = int(input())
work = []

emptyList = [0] * 1001

for i in range(N):
    work.append(list(map(int, input().split())))


work.sort(reverse=True, key=lambda x : x[1])

score =0 

#### 다시 도전 


for lists in work:
    for j in range(lists[0], 0, -1):
        if emptyList[j] == 0:
            emptyList[j] = 1
            score += lists[1]
            break

print(score)


