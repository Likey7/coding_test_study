import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)


for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    
    
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는  0 이라고 설정하여 큐에 삽입한다. 
    heapq.heappush(q, (0,start))    # 여기서 거리, 시작점을 넣는다. 거리를 앞에 너어야 행 
    distance[start] =0 # 거리를 저장하는 리스트도 존재함. 여기서도 0으로 넣어주 
    
    # 큐가 비기 전 까지!
    while q:
        dist, now = heapq.heappop(q) #우선순위가 높은(거리가 짧은) 
        # 처리된 적이 있던 노드라면 무시! 한다는 뜻, 
        # 거리를 볼 필요가 없는게, 처리가 된 노드라면 무조건 같거나 최단거리일 것임. 
        if distance[now] < dist: # 만약 우선순위 거리가, 지금 노드의 거리보다 길면 반복문 다음 순서로. , 
            continue
        # dist 는 현재 노드까지 걸리는 거리인데 disctanc
        
        # 처리된 적이 없는 노드라면,
        # 지금 그래프에서 갈수 있는 곳ㄷㄹ graph[now]
        # 하나씩 보면서 cost를 계산한다. 그건 그래프에 저장해뒀던 c 거리 
        # i[1] == c == 지금 위치에서 다음 노드까지 걸리는 거리 
        # dist 는 시작점 기준으로 현재 노드까지 걸리는 거리 더한게 코스트 
        for i in graph[now]:
            cost = dist + i[1]
            
            # 만약에 그 코스트가 기존에 그 노드까지 가는 거리보다 짧다면~ 
            if cost < distance[i[0]]:
                distance[i[0]] = cost  # 거리 갱신 최단거리고 
                heapq.heappush(q,(cost,i[0])) #그리고 지금 새로 방문하는 그 노드에 대한 정보도 큐에 삽입
                
            # 이 과정을 현재 노드에서 갈 수 있는 넥스트 노드마다 확인한다는 것. 
                
dijkstra(start)

for i in range(1, n+1):
    if distance[i]==INF:
        print('INFINITY')
    else:
        print(distance[i])
        