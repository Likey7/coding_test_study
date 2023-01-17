
n = int(input())

graph = []
data = []
teacher = 0

for i in range(n):
    # 표 만들기
    graph.append(list(input().split()))
    teacher += graph[i].count('T')

# 이동할애
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 선생님의 위치를 주고 네방향 + 끝까지 하는걸 만들어야함
# e w s n
def watch(x, y):

    for i in range(4):
        
        if i == 0: # n 북쪽
            direction = 'n'
        elif i == 1: # e 동쪽
            direction = 'e'
        elif i == 2: # s 남쪽
            direction = 's'
        elif i == 3: # w 서쪽
            direction = 'w'

        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx < n and ny < n and graph[nx][ny] != 'O':
            if graph[nx][ny] == 'S':
                return True
            else:
                for _ in range(n):
                    nx+=dx[i]
                    ny-=dy[i]
                
                    if x >= 0 and y >= 0 and x < n and y < n and graph[x][y] != 'O':
                        if graph[x][y] == 'S':
                            return True
                
                check = move(nx, ny, direction) # 학생 만나면 False
                # 학생
                if  check: # 학생을 만났다면? 
                    return False

    
    return True

def move(x, y, direction):
    for _ in range(n):
        if direction == 'n': # n 북쪽
            x -= 1
        elif direction == 's': # s 남쪽
            x += 1
        elif direction == 'e': # e 동쪽
            y += 1
        elif direction == 'w': # w 서쪽
            y -= 1
        
        if x >= 0 and y >= 0 and x < n and y < n and graph[x][y] != 'O':
            if graph[x][y] == 'S':
                return True # 실패 학생 만남 
                
    return False # 장애물, 학생 또는 벽 만나지 않음

    
def dfs(count):

    global answer

    # 장애물 3개 설치하면 멈추기
    if count == 3:
        cnt = 0
        # 선생님 감시
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'T':
                   
                    # 장애물 설치했고 선생님이 체크함 통과가 되면 바로 종료
                    if watch(i, j): # 발견했으면 True
                        cnt += 1
        
        if cnt == teacher:
            answer = True

        return
        

    # X인 얘들 장애물 설치
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                count += 1
                dfs(count)
                graph[i][j] = 'X'
                count -= 1

answer = False
dfs(0)
if  answer:
    print('YES')
else:
    print('NO')