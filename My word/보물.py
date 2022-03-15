# 왜 틀린지 모름

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sortA = sorted(A)
sortB = sorted(B, reverse=True)

idx_list = []

sum = 0

A_list = [0] * N
for i in range(N):
    idx_list.append(B.index(sortB[i]))

for j in range(N):
    A_list[idx_list[j]] = sortA[j]

for l in range(N):     
    sum += B[l] * A_list[l]

print(sum)

## 정답

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum = 0

for i in range(N):
    sum += min(A) * max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))
print(sum)
