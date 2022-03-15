N = int(input())
i = list(map(int, input().split()))

i.remove(max(i))

sum = sum(i)

print(sum)