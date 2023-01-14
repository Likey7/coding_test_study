from collections import deque
import copy

def bfs():
    
    queue = deque()
    tmp_graph = copy.deepcopy(graph)
    # 시뮬레이션을 돌릴 떄 마다 새로운 큐와 새로운 그래프를 복사한다. 
    # 모든벽을 세우는 경우를 각각의 다른 탐색의 케이스로 봐야 함. 
    
    for i in range(N):
        for j in range(M):
            if tmp_graph[i][j]==2:
                queue.append((i,j))
    # 먼저 큐에다가 바이러스를 다 넣고 시작한다. 
    
    # queue 가 비기 전까지는             
    while queue:
        x,y = queue.popleft() # 큐에서 좌표를 하나 꺼낸다 바이러스 있는 위치 
        
        for i in range(4): # 해당 바이러스의 사방향을 다 확인할건데 
            nx = x +dx[i]
            ny = y +dy[i]
            
            # 범위를 벗어난 경우 패스
            if nx <0 or nx>=N or ny<0 or ny>=M:
                continue # 다른 방향 탐색
            # 만약 바이러스가 침범되지 않은 곳을 발견하면 전염시킽 후, 
            # 해당 칸도 이젠 바이러스 지역이므로 큐에 넣는다. 
            if tmp_graph[nx][ny]==0: # 확인할 떄 쓰는 그래프는 카피본이다. 
                tmp_graph[nx][ny]=2
                queue.append((nx,ny)) 
    
    # 그 때의 안전영역의 최댓값이 answer 가 된다.        
    global answer # 전체 시뮬레이션에서 공용되는 변수 
    
    cnt= 0
    for i in range(N):
        cnt +=tmp_graph[i].count(0)    
        # 그래프에서 바이러스를 다 퍼트린 다음 0의 개수를 센다    
    answer = max(answer, cnt)
    
def makeWall(cnt):
    if cnt ==3 : 
        #벽 세개를 세웠다면 bfs() 탐색 호출
        bfs()
        return
    
    # 벽을 세우는 과정이다. 
    # 매 칸을 다 탐색하면서 벽을 세우는 것은 마치 DFS>...
    # 일 단 세우고 안에서 또 세우고... 그래프는 전체 그래프를 사용하여서 하나로 쓴다. 
    # 해당 함수가 깊어져 봤자 cnt3 이 끝이다. 깊어진 곳에서 벽이 세개 세워졌으면 
    # 시뮬레이션을 돌린다. 
    # 그리고 끝나면 다시 벽 해체 
    

    for i in range(N):
        for j in range(M):
            if graph[i][j]==0:
                graph[i][j]=1
                makeWall(cnt+1)
                graph[i][j]=0        


N,M = map(int,input().split())
graph = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
          
for i in range(N):
    graph.append(list(map(int,input().split())))
    
answer = 0
makeWall(0)
print(answer)