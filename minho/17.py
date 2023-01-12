# 첫째 줄에 자연수 N, K가 공백을 기준으로 구분되어 주어진다. 
# (1 ≤ N ≤ 200, 1 ≤ K ≤ 1,000) 
# 둘째 줄부터 N개의 줄에 걸쳐서 시험관의 정보가 주어진다. 
# 각 행은 N개의 원소로 구성되며, 해당 위치에 존재하는 바이러스의 번호가 공백을 기준으로 구분되어 주어진다. 
# 단, 해당 위치에 바이러스가 존재하지 않는 경우 0이 주어진다. 또한 모든 바이러스의 번호는 K이하의 자연수로만 주어진다. 
# N+2번째 줄에는 S, X, Y가 공백을 기준으로 구분되어 주어진다. (0 ≤ S ≤ 10,000, 1 ≤ X, Y ≤ N)

# S초 뒤에 (X, Y)의 바이러스를 출력 없으면 0 출력

from collections import deque

N, K = map(int, input().split())

graph = []
data = []

for i in range(N):
    graph.append(list(map(int, input().split())))

    for j in range(N):
        if graph[i][j] > 0:
            data.append((graph[i][j], 0, i, j))

data.sort()


S, X, Y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


q = deque(data)

while q:
    print(q)
    virus, time, x, y = q.popleft()

    if S == time:
        break
    
    # 하나씩 이동하면서 전염시킴 가장 낮은 것 부터 정렬해서
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx < N and ny < K:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, time+1, nx, ny))
        
    
print(graph)
print(graph[X-1][Y-1])