INF = 1e9

N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

X, K = map(int, input().split())

# input ----------------------------------

# 소개팅 장소 최소거리
for i in range(1, N + 1):
    graph[1][K] = min(graph[1][K], graph[1][i] + graph[i][K])

# 방문 장소 최소거리
for i in range(1, N + 1):
    graph[1][X] = min(graph[1][X], graph[1][i] + graph[i][X])


if graph[1][K] + graph[1][X] >= INF:
    print(-1)
else:
    print(graph[1][K] + graph[1][X])

