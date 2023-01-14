# N x N 크기의 복도
# 막히기 전까지 4방향으로 모두 볼 수 있음 끝까지
# 선생님 있으면 T 학생 S 장애물 O
# 장애물을 정확히 3개 설치 모두 피할수 있으면 YES 아니면 NO
# 첫째 줄에 자연수 N이 주어진다. 
# (3 ≤ N ≤ 6) 
# 둘째 줄에 N개의 줄에 걸쳐서 복도의 정보가 주어진다. 
# 각 행에서는 N개의 원소가 공백을 기준으로 구분되어 주어진다. 
# 해당 위치에 학생이 있다면 S, 선생님이 있다면 T, 아무것도 존재하지 않는다면 X가 주어진다.
# 단, 전체 선생님의 수는 5이하의 자연수, 전체 학생의 수는 30이하의 자연수이며 항상 빈 칸의 개수는 3개 이상으로 주어진다.

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
                check = move(nx, ny, direction)
                if check:
                    return True
    
    return False

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
                return True
                
    return False

    
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
                    if not watch(i, j):
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