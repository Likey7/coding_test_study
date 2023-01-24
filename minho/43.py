# 집의 수 N
# 도로의 수 M
# M 개의 줄에 걸쳐 X,Y,Z가 주어짐
# X에서 Y로 양방향 도로가 있고 그 길의 길이가 Z임


def find_parent(parent, x):

    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)

edges = []
result = 0

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    x, y, z = map(int, input().split())

    edges.append((z, x, y))

edges.sort()
total = 0

for edge in edges:
    cost, a, b = edge
    total += cost
    
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(total-result)
