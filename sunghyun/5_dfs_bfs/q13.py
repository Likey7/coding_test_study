from itertools import combinations

graph = [[0, 0, 1, 0, 0],
         [0, 0, 2, 0, 1],
         [0, 1, 2, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 0, 2]]
n = len(graph)
current_chicken = []
houses = list()

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            current_chicken.append((i, j))
        if graph[i][j] == 1:
            houses.append((i,j))

distances = [None] * len(houses)
def delete_chicken(m):

    # 현재 있는 치킨집에서 게속 운영할 m개의 매장 조합
    for data in combinations(current_chicken, m):
        
        #m개의 매장에 대해 치킨 거리 조사
        for x, y in data:

def distance(x, y):
    for house in houses:


