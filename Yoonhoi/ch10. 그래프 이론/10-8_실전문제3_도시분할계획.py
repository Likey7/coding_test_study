#최소비용으로 다 연결한다음 반으로 자른다. 
# 크루스칼


import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e = map(int,input().split())
parent = [i for i in range(v+1)]

edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()
last = 0

for edge in edges:
    cost,a,b = edge
    # 같다 == 사이클 발생한다. 
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
        last = cost
    
    
print(result - last)