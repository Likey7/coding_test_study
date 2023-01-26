import heapq
n,m = map(int,input().split())
INF = int(1e9)
graph = [[] for i in range((n+1))]
distance = [INF] *(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))
    
def dijkstra(start):
    q = 0
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist +i[1]
        if cost < distance[i[0]]:
            distance[i[0]] =  cost
            heapq.heappush(q,(cost, i[0]))
            
dijkstra(1)

hut_distance = min(distance)
hut_index = distance.index(hut_distance)
hut_count = distance.count(hut_distance)

print(hut_index, hut_distance, hut_count)