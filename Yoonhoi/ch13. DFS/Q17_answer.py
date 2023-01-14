# https://www.acmicpc.net/problem/18405
# https://data-flower.tistory.com/71
from collections import deque
################################3
n,k = map(int,input().split())

graph=[]
data = []

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        
        if graph[i][j] != 0: # 0 아니면 바이러스 
            data.append((graph[i][j],0, i, j)) #바이러스 종류, 시간, 위치 
            
data.sort() # 맨처음 초기 바이러스 
q = deque(data)

S,X,Y = map(int,input().split())
s = 0 # time
##################################

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while q: # 큐가 비었거나 
    virus,cnt, x, y  = q.popleft()
    
    if cnt == S:
        break
    # 시간이 다 되었을 떄
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx <n and 0<=ny < n:
            if graph[nx][ny]==0: # 바이러스가 없으면 
                graph[nx][ny] = virus
                q.append((virus, cnt+1, nx, ny))

print(graph[X-1][Y-1])