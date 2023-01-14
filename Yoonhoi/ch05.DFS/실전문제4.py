# 최소 칸의 개수를 구해라!
# BFS

N, M  = map(int, input().split())

graph = []
for i in range(N):
    graph.append( list(map(int,input()) ))
print(graph)
dx = [-1, 1, 0,0]
dy = [0,0,-1,1]

from collections import deque
def BFS(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        print(queue)
        x,y = queue.popleft()
        print(x,y)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dx[i]
            
            if nx<0 or ny <0 or nx >=N or ny >=M :
                continue 
            if graph[nx][ny]==0:
                continue
            
            # 갈 수 있는 경우, 처음 방문일 때 갔다는 것 기록한다. 
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y] +1 # 한칸 갈 때마다 몇걸음 왔는지 기록한다. 
                queue.append((nx,ny))
                print('해당 방향은 끝남. ')
    for row in graph:
        print(row)        
    return graph[N-1][M-1]


print(BFS(0,0))