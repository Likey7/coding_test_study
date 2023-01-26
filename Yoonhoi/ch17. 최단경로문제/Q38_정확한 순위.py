n,m = map(int,input().split())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]


for _ in range(m):
    low,high = map(int,input().split())
    graph[low][high] = 1
'''
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0
'''

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k],graph[k][j])

count=0      
for k in range(1,n+1):
    low = graph[k].count(INF)
    high = 0
    for i in range(1,n+1):
        if graph[i][j]==INF:
            high +=1
    if (n-low-high+1)==0:
        count+=1


print(count)
        
        
        