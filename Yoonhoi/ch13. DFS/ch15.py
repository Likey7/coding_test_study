from collections import deque
import sys

f = sys.stdin.readline

N, M, K, X = list(map(int, f().split()))
graph = [[] for _ in range(M+1)]

for i in range(M):
    a,b = (map(int,f().split()))
    graph[a].append(b)
    
answer = []
qu = deque([X])
visited = [False]*(N+1)
distance = [0]*(N+1)


while qu:
    new = qu.popleft()
    for x in graph[new]:
        if visited[x]==False:
            visited[x]=1
            qu.append(x)
            distance[x] =distance[new]+1
         
            if distance[x]== K:
                answer.append(x)
    
    if len(answer)==0:
        print(-1)
    else :
        answer.sort()
        for a in answer:
            print(a)
            
            
        
            
            
    