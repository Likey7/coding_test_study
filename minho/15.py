# 첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다. 
# (2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N)
# 둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어진다. 
# 이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미다. (1 ≤ A, B ≤ N) 단, A와 B는 서로 다른 자연수이다.
from collections import deque

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    
    data = list(map(int, input().split()))
    graph[data[0]].append(data[1])

distance = [-1] * (N + 1)
distance[X] = 0
# print(distance)
q = deque([X])

while q:
    v = q.popleft()
    
    for i in graph[v]:
        if distance[i] == -1:
            distance[i] = distance[v] + 1
            q.append(i)

checks = 0

for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        checks = 1

if checks == 0:
    print(-1)