# 첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
# 둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
# 빈 칸의 개수는 3개 이상이다.
# 새로 벽을 세워야 하는건 3개고 무조건 3개 넣어야함

N, M = map(int, input().split())

_map = []


for _ in range(N):
    _map.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

mapClone = [[0] * M for _ in range(N)]

def virus(i, j):
    
    for k in range(4):
        # 한 칸씩 이동함
        x = i + dx[k]
        y = j + dy[k]
        
        if x >= 0 and x < N and y >= 0 and y < M: # 범위 세팅
            if mapClone[x][y] == 0:
                mapClone[x][y] = 2
                virus(x, y)
                

# 3개씩 울타리를 치고 하나씩 다 돌아봄
def dfs(count):
    global result
    
    # 3개 울타리 설치되면 실행
    if count == 3:
        # mapClone에 세팅
        for i in range(N):
            for j in range(M):
                mapClone[i][j] = _map[i][j]
        
        # 바이러스 퍼트리기
        for i in range(N):
            for j in range(M):
                if mapClone[i][j] == 2:
                   
                    virus(i, j)

        score = 0
        for i in range(N):
            for j in range(M):
                if mapClone[i][j] == 0:
                    score += 1

        result = max(result, score)

    # 0인 얘들 울타리 치기
    for i in range(N):
        for j in range(M):
            if _map[i][j] == 0:
                _map[i][j] = 1
                
                dfs(count+1)
                _map[i][j] = 0
                count -= 1

dfs(0)
print(result)