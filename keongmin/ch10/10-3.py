import heapq
import sys

input = sys.stdin.readline

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if parent[a] < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())

q = []
for _ in range(M):
    A, B, C = map(int, input().split())
    heapq.heappush(q, (C, A, B))

parent = [i for i in range(N + 1)]
result = []
while q:
    x, y, z = heapq.heappop(q)

    if find(parent, y) != find(parent, z):
        union(parent, y, z)
        result.append(x)

result.pop()
print(sum(result))
