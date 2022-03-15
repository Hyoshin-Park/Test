N = int(input())

cow_list = []

for i in range(N):
    a, b = map(int, input().split())
    cow_list.append([a, b])

print(cow_list)