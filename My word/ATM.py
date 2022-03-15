N = int(input())
P = list(map(int, input().split()))


if N == 1:
    print(P[0])
else:
    P.sort()

    answer = 0
    sum = 0
    
    for i in range(N):
        sum += (answer + P[i])
        answer += P[i]


    print(sum)

