# BFS 큐를 사용해서 가까운 것 부터 탐색합니다. 
# 앞에서부터 순탐~~

from collections import deque

def BFS(graph, start, visited):
    queue = deque([start])
    
    visited[start] = True
    
    while queue:
        v = deque.popleft()
        print(v,end = '')
        
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [ []
         , [2,3,8]
         , [1,7]
         , [1,4,5]
         , [3,5]
         , [3,4]
         , [7]
         , [2,6,8]
         ,[1,7]
         ]



visited = [False] *9

BFS(graph,1,visited)