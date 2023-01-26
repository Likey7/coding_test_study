# 테스트를 돌려 볼 수 없어서 확인은 안되는데 
# 일단 그래프를 다 채우고, 거기서 0이 아닌 것을 확인하는 방법으로 진행했다. 
# 해설에서는 
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
plan = list(map(int,input().split()))


for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] =min(graph[i][j], graph[i][k]+graph[k][j])

def is_connected(arr,start,end):
    if arr[start][end]!=0:
        return True
    return False
    
def main():
    for i in range(m-1):
        start,end = plan[i], plan[i+1]
        if not is_connected(graph,start,end):
            print('NO')
            return 
    print('YES')
    
