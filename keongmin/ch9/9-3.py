from collections import defaultdict
import heapq

INF = 1e9

N, M, C = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))

visited = [False] * (N + 1)
distance = [INF] * (N + 1)

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        d, n = heapq.heappop(q)
        visited[n] = True

        if distance[n] < d:
            continue

        for i in graph[n]:
            cost = d + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(C)
print(visited.count(True) - 1, end=" ")
time = 0
for d in distance:
    if d < INF:
        time = max(time, d)
print(time)