# https://www.acmicpc.net/problem/2887
from collections import deque
import sys
input = sys.stdin.readline

'''
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
'''

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
NINF = int(-1e9)
INF = int(1e9)

n = int(input())
nodes = []

for _ in range(n):
    nodes.append(list(map(int,input().split())))
    
graph = [[INF]*(n+1) for _ in range(n+1)]
distance = []

for i, from_node in enumerate(nodes):
    x1,y1,z1 = from_node[0],from_node[1],from_node[2]
    for j, to_node in enumerate(nodes):
        x2,y2,z2 = to_node[0],to_node[1],to_node[2]

        if i==0 or j==0:
            continue
        elif i==j:
            graph[i][j] = 0
        else:
            dist= min(graph[i][j], min(abs(x1-x2), abs(y1-y2),abs(z1-z2)))
            graph[i][j] =dist
            graph[j][i] = dist
            distance.append((dist,i,j))

# 여기까지 하면 1차 거리 입력 (한 점에서 다른 거리 이동)

parent = [i for i in range(n+1)]
distance.sort()
result= 0

for edge in distance:
    cost,a,b = edge
    # 같다 == 사이클 발생한다. 
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
        last = cost
