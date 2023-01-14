import sys 
from collections import deque
f = sys.stdin.readline

N,M = map(int, f().split())

graph =[]
virus = []
for i in range(N):
    line = list(map(int,f().split()))
    graph.append(line)
    for j in line:
        if graph[i][j]!=0 : 
            virus.append(graph[i][j],0,i,j)
S,X,Y = map(int,f().split())
    
dx=[-1,1,0,0]
dy=[0,0,1,-1]
    
virus.sort()
virus = deque([virus])


#BFS

while virus : 
    num, time, x ,y  = virus.popleft()
    
    if time ==S:
        break
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if nx<0 or nx>=N or ny<0 or ny>0:
            if graph[nx][ny]==0:
                graph[nx][ny]=num
                virus.append((num,time+1,nx, ny))
        

print(graph[N-1][N-1])