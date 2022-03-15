num = input().split("-")

lists = []

for i in num:
    cnt = 0
    s = i.split("+")
    for j in s:
        cnt += int(j)
    lists.append(cnt)
first = lists[0]
for k in range(1, len(num)):
    first -= lists[k]

print(first)