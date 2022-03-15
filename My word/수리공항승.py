# N, L = map(int, input().split())
# loc = list(map(int, input().split()))

# loc.sort()

# start = 0
# cnt = 0
# list = []

# for i in loc:
#     if list == []:
#         list.append(i)
#     else:
#         if abs(list[num] - i) > L:
#             cnt += 2
#         elif abs(list[num] - i) <= L:
#             cnt += 1
#         elif i == loc[-1]:
#             if abs(loc[-1] - loc[-2]) <= L:
#                 cnt += 1
#         num += 1
# print(cnt)



N, L = map(int, input().split())
loc = list(map(int, input().split()))

loc.sort()

start = 0
cnt = 0

for location in loc:
    if start < location:
        start = location + L - 1
        cnt += 1
print(cnt)