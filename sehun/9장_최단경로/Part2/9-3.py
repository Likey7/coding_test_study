#플로이드 워셜 알고리즘

INF = int(1e9)

n = int(input())
m = int(input())

#2차원 리스트(그래프표현)을 만들고 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

#자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
  for b in range(1, n+1):
    if a==b:
      graph[a][b] = 0

#각 간선 정보 입력받아 그 값으로 초기화
for _ in range(m):
  #A에서 B로 가는 비용은 C라고 설정
  a, b, c = map(int, input().split())
  graph[a][b] = c

#점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

#수행된 결과를 출력
for a in range(1, n+1):
  for b in range(1, n+1):
    #도달할수 없는경우 무한출력
    if graph[a][b] == INF:
      print("INF")
    else:
      print(graph[a][b], end=' ')
  print()