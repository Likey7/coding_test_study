N, M = map(int, input().split())
graph = []

for _ in range(N):
    new = [int(i) for i in input()]
    graph.append(new)

def dfs(graph, x, y):
    if x < 0 or x >= N or y < 0 or y >= M or graph[x][y] == 1:
        return

    graph[x][y] = 1

    dfs(graph, x + 1, y)
    dfs(graph, x - 1, y)
    dfs(graph, x, y + 1)
    dfs(graph, x, y - 1)


result = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            dfs(graph, i, j)
            result += 1

print(result)