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

#집들로 부터의 치킨거리 
distances = [[None] * m] * len(houses) 

def delete_chicken(m):

    # 현재 있는 치킨집에서 게속 운영할 m개의 매장 조합
    for chicken in combinations(current_chicken, m):
        
        for r2, c2 in houses:
            dist_list = []
            for r1, c1 in chicken:
                dist_list.append = abs(r1 - r2) + abs(c1 - c2)
            
            

        #m개의 매장에 대해 치킨 거리 조사
        for x, y in data:

# 치킨집과 집들의 거리
def distance(r1, c1):
    for house in houses:
        r2, c2 = house
        dist = abs(r1 - r2) + abs(c1 - c2)




