#플로이드로 도착cost가 가장 높은게 최상위노드고 도착cost가 없는게 말단노드
#이걸 순위로 나열했을때 중복된 cost가 있는 노드들은 등수판별불가고 나머지는 가능

n, m= map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
  for b in range(n+1):
    if a==b:
      graph[a][b] = 0

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1

for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


result = 0

#?
for a in range(1, n+1):
  count = 0
  for b in range(1, n+1):
    if graph[a][b] != INF or graph[b][a] != INF:
      count += 1
  if count == n:
    # print(n)
    result += 1
print(result)

# #수행된 결과를 출력
# for a in range(1, n+1):
#   for b in range(1, n+1):
#     #도달할수 없는경우 무한출력
#     if graph[a][b] == INF:
#       print("INF", end=' ')
#     else:
#       print(graph[a][b], end=' ')
#   print()

