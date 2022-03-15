N = int(input())
tree = list(map(int, input().split()))

max = 0
num = 0

tree.sort(reverse=True)

for date, trees in enumerate(tree):
    if max == 0:
        max = int(date) + int(trees) + 1
    else:
        num = int(date) + int(trees) + 1
        if num > max:
            max = num 

print(max + 1)