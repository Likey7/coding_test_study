#개선된 다익스트라 알고리즘 소스코드

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
#시작 노드를 입력받기
start = int(input())
#각 노드에 연결된 노드정보 담는 리스트
graph = [[] for i in range(n+1)]
#최단거리 테이블 모두 무한 초기화
distance = [INF] * (n+1)

#모든 간선 정보를 입력
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append(b, c)

def dijkstra(start):
  q = []
  #시작노드로 가기위한 최단경로 0설정 큐삽입
  heapq.heappush(q, (0, start))
  distance[start] = 0
  
  #q가 비어있지 않다면
  while q:
    dist, now = heapq.heappop(q)
    #가장 최단거리가 짧은 노드에 대한 정보 꺼내기

    #현재 노드가 처리된적이 있는 노드라면 무시
    if distance[now] < dist:
      continue
    #현재 노드와 연결된 다른 인접한 노드들을 확인
    for i in graph[now]:
      cost = dist+i[1]
      #현재노드를 거쳐서 다른노드로 이동하는 거리가 더 짧은경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

#다익스트라 알고리즘 실행
dijkstra(start)

#모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
  if distance[i] == INF:
    print("INF")
  else:
    print(distance[i])

  
