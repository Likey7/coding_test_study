#크루스칼 최소신장트리
import sys
input = sys.stdin.readline



def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] =b

n,m = map(int,input().split())

graph = [[0]*(n+1) for i in range(n+1)]
parent = [i for i in range(n+1)]
edges = []
total=0
for _ in range(m):
    x,y,z = map(int,input().split())
    # x,y  양방향 길이 zz
    graph[x][y],graph[y][x] = z,z
    edges.append((z,x,y))
    total+=z

edges.sort()
result = 0
for edge in edges:
    cost, a, b  = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
print(total - result)