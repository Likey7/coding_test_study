N, M = map(int, input().split())

parent = [i for i in range(N + 1)]

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(M):
    d, a, b = map(int, input().split())

    if d == 0:
        union(parent, a, b)
    elif d == 1:
        result_a = find(parent, a)
        result_b = find(parent, b)

        if result_a == result_b:
            print('YES')
        else:
            print('NO')
