from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    new = [int(i) for i in input()]
    graph.append(new)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, a, b):
    q = deque([(a, b)])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

    return graph[N - 1][M - 1]

print(bfs(graph, 0, 0))