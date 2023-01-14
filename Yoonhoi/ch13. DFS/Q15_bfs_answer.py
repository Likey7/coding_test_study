# bfs / linked list
# 못풀어서 해답 찾아봄
# https://steadily-worked.tistory.com/646

from collections import deque
n, m, k, x = map(int,list(input().split()))
path  = [ [] for _ in range(n+1)]
# 도로의 거리를 재서 기록하는 그래포
distance = [0] * (n+1)
visited = [False]*(n+1)

# 도로 개수 만큼 인풋 받음
for _ in range(m):
    a,b = tuple(map(int,input().split()))
    path[a].append(b)

def bfs(start):
    answer = []
    qu = deque([start])
    visited[start] = True
    distance[start] = 0
    
    while qu :
        check = qu.popleft() 
        for i in path[check]:
            if not visited[i]:
                visited[i] = True
                qu.append(i)
                distance[i] = distance[check]+1
                if distance[i]==k:
                    answer.append(i)
    if len(answer)==0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i,end = '\n')
    
bfs(x)