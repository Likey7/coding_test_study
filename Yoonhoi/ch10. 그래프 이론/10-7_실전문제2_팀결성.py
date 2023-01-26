
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
'''

def is_same(parent,a,b):
    if find_parent(parent,a) ==find_parent(parent,b):
        return True
    else:
        return False
'''


n,m = map(int,input().split())

parent = [i for i in range(n+1)]

for _ in range(m):
    op,a,b = map(int,input().split())
    if op: # ==1
        # 같은 팀 여부 확인 
        if find_parent(parent,a) ==find_parent(parent,b):
            print('YES')
        else:
            print('NO')
    else:
        # # 합치기 실행
        union_parent(parent,a,b)
        