def dfs(graph, v, visited):
    visited[v] = True
    
    print(v, end=' ')

    #i는 노드
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

visited = [False] * 9

dfs(graph, 1, visited)

