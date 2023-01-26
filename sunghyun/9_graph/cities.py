#크루스칼 에서 가장 큰 간선 자르기.

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]

v, e = 7, 12

parent = [0] * (v+1)

edges = []
result = 0


for i in range(1, v + 1):
    parent[i] = i

