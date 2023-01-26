INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]


# 자기 자신에게서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] =0
            
            
# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c
    
# 점화식에 따라 플루이드 위셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])
            

for a in range(1,n+1):
    for b in range(1,n+1):
        # 도달할 수 없는 경우 무한(infinity)출력
        if graph[a][b] ==INF:
            print("INFINITY", end = '')
        else:
            print(graph[a][b],end = '')
            
    print()