
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = 1
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append((b, 1))
  graph[b].append((a, 1))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)



node = 0
dis = 0

result = []

for i in range(1, n+1):
  if dis < distance[i]:
    node = i
    dis = distance[i]
    result = [node]
  elif dis == distance[i]:
    result.append(i)

print(node, dis, len(result))