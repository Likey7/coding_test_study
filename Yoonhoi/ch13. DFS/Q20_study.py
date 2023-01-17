from collections import deque


def simulation():
    teachers = deque()
    for i in range(N):
        for j in range(N):
            if graph[i][j]=='T':
                teachers.append((i,j)) 
    
    global flag 
    flag = False # 학생 아직 본적 없으니 초기화
    while teachers :
        x,y = teachers.popleft()
        for i in range(4):
            flag = search(x,y, dx[i],dy[i]) 
            if flag :  
                return False # 나왔으면 실패
    # while 문 안에서 플래그에 한번도 안걸렸ek -> 학생을 못봤다는 건데  그럼 성공이니까 True
    return True
    
            
dx = [0,1,0,-1]
dy = [-1,0,1,0]   
flag = 0

# 이 함수는 시작점 기준으로 특정 방향으로 탐색하면서
# flag ==True 를 찾는 것이 목적 
def search(x, y, dx, dy):
    global flag
    nx = x +dx
    ny = y +dy
    if ( 0<=nx<N ) and (0<=ny<N): # 범위 벗어나지 않을 때
        if graph[nx][ny]=='S':
            # 학생 찾았다면 해당 맵은 내 목적과 다르니까 더이상 볼 필요가 없음 
            return True
        elif graph[nx][ny] =='O':
            return False  # 장애물을 만난다면 해당 방향으로는더이상 갈 수 없기 때문에 search 함수를 종료 (다음턴에 dx, dy 바뀌어서 들어옴. )
        else:    # xgraph[nx][ny]=='T' or xgraph[nx][ny]=='X:# 빈 벽이거나 선생님 넘어서도 다 볼 수 있어서 해당방향 계속 진행
            return search(nx,ny,dx,dy) # 이쪽 방향으로는 가능성이 있거든 
    return False

    

def makeWall(cnt): # True 가 리턴되었단건데 
    if cnt==3:
        return simulation() # 해당 시뮬레이션 성공? 
    else:
        for i in range(N):
            for j in range(N):
                if graph[i][j]=='X':
                    graph[i][j]='O'
                    result = makeWall(cnt+1)
                    if result: # 해당 벽이 성공했다면 
                        return True
                    graph[i][j]='X'
        return False
    


N = int(input())
graph = []

for i in range(N):
    graph.append(list(input().split()))


result = makeWall(0)  # True 
if result: #True
    print('YES')
else:
    print('NO')