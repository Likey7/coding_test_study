# 이 경우에는 왼- > 오 , 위 -> 아래 로 향하는 것만 가능할떄 가능


def main():
    n = int(input())
    graph = []
    for _ in range(n+1):
        costs = list(map(int,input().split()))
        graph.append(costs)
    
    for a in range(n):
        for b in range(n):
            if a==0 and b==0:
                continue
            elif a==0:
                graph[a][b] = graph[a-1][b] + graph[a][b]
            elif b==0 : 
                graph[a][b] = graph[a][b-1] + graph[a][b]
            else:
                graph[a][b] = min(graph[a-1][b],graph[a][b-1]) + graph[a][b]
                
    print(graph[n-1][n-1])
    


T = int(input())

for _ in range(T):
    main()
    
    