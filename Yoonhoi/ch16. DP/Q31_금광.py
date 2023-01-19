from collections import deque 

def get_max_gold(n,m,graph):
    max_gold =None
    
    # d[i,j]=[1,m]] = max (j = [1,n]
    # ,d[i-1][j-1] , d[i][j-1], d[i+1][j] ) + gold[i][j] 

    
    
    
    return max_gold

T = int(input())

for _ in range(T):
    n,m = map(int,input().split())
    nums = deque(list(map(int,input().split())))
    graph = [[0 for col in range(m+1)] for row in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1,):
            graph[i][j] = nums.popleft()
    
    max_gold = get_max_gold(n,m,graph)        
    print(max_gold)
    
