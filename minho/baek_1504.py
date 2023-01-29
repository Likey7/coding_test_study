# 첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. 
# (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000) 
# 둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데,
#  a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다. 
# (1 ≤ c ≤ 1,000) 
# 다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다. 
# (v1 ≠ v2, v1 ≠ N, v2 ≠ 1) 
# 임의의 두 정점 u와 v사이에는 간선이 최대 1개 존재한다.

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

u, v = map(int, input().split())

def dijkstra(start):

    q = []

    distance = [INF] * (n + 1)

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        
        # 0     1
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            
            #3      0      3
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


n_distance = dijkstra(1)
u_distance = dijkstra(u)
v_distance = dijkstra(v)

a = n_distance[u] + u_distance[v] + v_distance[n]
b = n_distance[v] + v_distance[u] + u_distance[n]

result = min(a, b)
print(result if result < INF else -1)

# print(distance)
# print(distance[n])
