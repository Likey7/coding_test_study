import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
m= int(input())
graph = [[INF]*(n+1) for i in range(n+1)]

for _ in range(m):
    #from, to, cost
    a,b,c = map(int,input().split())
    if graph[a][b] >c:
        graph[a][b]=c

for i in range(n+1):
    for j in range(n+1):
        if i ==j:
            graph[i][j]=0


for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])
            

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print('0', end = ' ')
        else:
            print(graph[a][b],end = ' ')
    print()