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

n, m = 7, 8

parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i

for i in range(m):
    operation, a, b = map(int, input().split())

    if operation == 0:
        union_parent(parent, a, b)
    
    if operation == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")