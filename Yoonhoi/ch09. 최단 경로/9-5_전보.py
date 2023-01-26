import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
# n : node <=30000 / m : edge  <=200000/ c : start point
n,m,c = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

######################################

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    
    while q : 
        dist,now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        
        #최단거리 갱산할 경우에만주변노드 확인한다. 
        for i in graph[now]:
            cost =dist +i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    
dijkstra(c)

count = 0
max_distance =0
for d in distance:
    if d!=INF:
        count +=1
        max_distance = max(max_distance,d)
        
print(count-1, max_distance)

  
# 출력값    
# c에서 도달할 수 잇는 전체 노드 개수 
# 최단길이 중 제일 긴 것 


