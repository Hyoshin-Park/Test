def dfs(x, y):
    if x <= -1 or x >= width or y <= -1  or y >= height:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x - 1, y)
        dfs(x, y- 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False



width, height = map(int, input().split())

graph = []

for i in range(width):
    graph.append(list(map(int, input().split())))

result = 0
for i in range(width):
    for j in range(height):
        if dfs(i ,j) == True:
            result += 1

print(result)
