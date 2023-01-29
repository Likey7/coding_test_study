# N 학생수 
# M 두 학생의 성적을 비교한 횟수
# M 개의 줄에 A, B기 주어짐 A가 B보다 낮다는걸 의미

n, m = map(int, input().split())

INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):

        if a == b:
            graph[a][b] = 0

for _ in range(m):

    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


result = 0

for a in range(1, n+1):
    cnt = 0
    for b in range(1, n+1):
        if graph[a][b] != INF or graph[b][a] != INF:
            cnt += 1
    
    if cnt == n:
        result += 1

print(result)