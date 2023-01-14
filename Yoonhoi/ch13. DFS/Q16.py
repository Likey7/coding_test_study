from collections import deque
import copy
def dfs():
    qu = deque()
    xgraph = copy.deepcopy(graph)
    
    # 바이러스를 일단 다 큐에 넣장
    for i in range(N):
        for j in range(M):
            if xgraph[i][j]==2:
                qu.append(i, j)
    
    while qu:
        x, y  = qu.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx >=N or ny<0 or ny>=M:
                continue
            
            if xgraph[nx][ny]==0:
                xgraph[nx][ny]=2
                qu.append((nx,ny))       
    
    # 큐가 끝났다는 건 할 수 있는 탐색이 다 끝난 것 아닌가! 
    # 이제 0의 개수를 센다. 
    
    cnt = 0
    for line in xgraph:
        cnt+=line.count(0)     
    
    global answer
    answer = max(answer,cnt)
            
            
            
dx = [-1,1,0,0] 
dy = [0,0,-1,1]       
        


def makeWall(cnt):
    if cnt ==3:
        dfs()
        return #탐색이 끝나면 해당 함수는 끝내야 한다
    # dfs 안에서 계속 탐색을 첨부터 하는 것
    for i in range(N):
        for j in range(M):
            if graph[i][j]==0:
                graph[i][j]=1
                makeWall(cnt+1)
                graph[j][j]=0
            

N,M = map(int,input().split())
graph = []

for i in range(N):
    line = list(map(int, input().split()))
    graph.append(line)

answer = 0    
makeWall(0)
print(answer)
        
    
    
    
