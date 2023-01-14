# Q 17. 경쟁적 전염

###############
# 입력

from collections import deque

N, K  = map(int, input().split())
graph = []

for i in range(N):
    line = list(map(int,input().split()))
    graph.append(line)
# S초 후의 (X, Y) 에 존재하는 바이러스 종류는? 
S,X,Y = map(int, input().split())



virus = [[] for _ in range(K+1)]
# 바이러스의 번호 K 이하의 자연수
for i in range(N):
    for j in range(N):
        if graph[i][j]!=0:
            virus[graph[i][j]].append((i,j))
            
print(virus)


                      
###########

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# BFS 가까운 것 부터 que
# 함수를 쓰면 dfs 인데 move 함수를 만들어벌엿...
def move(x,y,S):
    
    
    que = deque()
    que.append((x,y))
    
    for i in range(S):
        for i in range(4):
            nx = x +dx[i]
            ny = y+dy[i]
            if nx<0 or nx>N-1 or ny<0 or ny>N-1: 
                continue   
            if graph[nx][ny] <=graph[x][y]:
                continue
            elif graph[nx][ny]==0 :
                for i in range(4):
                    graph[nx][ny] = graph[x][y]
                    que.append((nx,ny))
                    move(nx,ny,S-1)

# 1,2,3,4 전염 순서를 위해 
# 각각의 시작점을 먼저 체크한 다음
# 1,2,3, ,,, s까지 돌린다? 

for row in graph:
    print(row)
    
print(move(X,Y,S))