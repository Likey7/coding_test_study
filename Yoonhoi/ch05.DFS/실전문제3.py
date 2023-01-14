# DFS

N, M  = map(int, input().split())

graph = []
for i in range(N):
    graph.append( list(map(int,input()) ))
    
visited = [ [ 0 for _ in range(M)] for _ in range(N) ]
print(graph)

def DFS(x,y):
    if x<0 or x>=N or y<0 or y>=M : 
        return  
    # 주어진 범위를 벗어나는 경우에는 즉시 종료 
    if graph[x][y]==0:
        graph[x][y] = 1
        DFS( x+1,y)
        DFS(x, y+1)
        DFS( x-1,y)
        DFS( x, y-1)
        return True
    
    

result =0

for i in range(N):
    for j in range(M):
        if DFS(i,j)==True :
            result+=1
            
print(result)