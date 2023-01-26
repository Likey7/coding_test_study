# N x N 크기의 공간 물고기 M마리 상어 1마리
# 크기가 같으면 못먹음 무조건 작아야함
# 아기 상어 크기는 처음에 2
# 크기가 1인 물고기 두마리 먹으면 3으로 바뀜(자기랑 같은 양이 됐을때 1증가)

from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

pos = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            pos.append(i)
            pos.append(j)

cnt = 0

def bfs(x, y):
    visited = [[0] * N for _ in range(N)]
    queue = deque([[x,y]])
    cand = []

    visited[x][y] = 1

    while queue:
        i, j = queue.popleft()

        for idx in range(4):
            ii, jj = i + dx[idx] , j + dy[idx]

            if 0 <= ii and ii < N and 0 <= jj and jj < N and visited[ii][jj] == 0:
				
                if graph[x][y] > graph[ii][jj] and graph[ii][jj] != 0:
                    visited[ii][jj] =  visited[i][j] + 1
                    cand.append((visited[ii][jj] - 1, ii, jj))
                elif graph[x][y] == graph[ii][jj]:
                    visited[ii][jj] =  visited[i][j] + 1
                    queue.append([ii,jj])
                elif graph[ii][jj] == 0:
                    visited[ii][jj] =  visited[i][j] + 1
                    queue.append([ii,jj])
                    
	
    return sorted(cand, key = lambda x: (x[0], x[1], x[2]))


i, j = pos
size = [2, 0]

while True:
    graph[i][j] = size[0]
    cand = deque(bfs(i,j))
    
    if not cand:
        break
        
    step, xx, yy = cand.popleft()
    cnt += step
    size[1] += 1
    
    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    graph[i][j] = 0
    i, j = xx, yy
        
print(cnt)