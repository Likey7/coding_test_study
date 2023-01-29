# 첫째 줄에는 지도의 세로의 크기 M과 가로의 크기 N이 빈칸을 사이에 두고 주어진다. 
# 이어 다음 M개 줄에 걸쳐 한 줄에 N개씩 위에서부터 차례로 각 지점의 높이가 빈 칸을 사이에 두고 주어진다. 
# M과 N은 각각 500이하의 자연수이고, 각 지점의 높이는 10000이하의 자연수이다.
import sys

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

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


                
M, N = map(int, sys.stdin.readline().split())
parent = [[False] * N for i in range(M)]

graph = []
for i in range(M):
    graph.append(list(map(int, sys.stdin.readline().split())))

