# 치킨배달
import copy
# x,y 좌표의 집 기준으로 가장 짧은 치킨거리를 반환해주는 함수 
def find_shortest_distance(H_x,H_y,left):
    dis = 0
    #이때 line 은 치킨집 
    # 치킨집 돌면서 거리 리터 ㄴ
    # 이떄 치킨집은 지워진 후 치킨집 nCR
    min_dis = 999
    for (C_x,C_y) in left:
        dis = get_distance(H_x,H_y,C_x,C_y)
        min_dis = min(min_dis, dis)
    
    return min_dis
    
    
def get_distance(H_x,H_y,C_x,C_y):
    return abs(H_x-C_y)+abs(H_y-C_y)
# N  : ㄷ도시의 크기 , M, 최대 치킨집 개수 

N,M = map(int,input().split())
graph = []
chicken = []
house = []
distance = 0
min_distacne = 0





for i in range(N):
    line= list(map(int,input().split()))
    graph.append(line)
    #0 빈칸 1 집 2 치킨집 
    for j in range(N):
        if graph[i][j] ==2:
            chicken.append((i,j))
        elif graph[i][j]==1:
            house.append((i,j))

chicken_num = len(chicken)
end_num = chicken_num - M
# chicken 조합에서 chicken_num 개 만큼 뽑는다. 
import itertools


nCr = itertools.combinations(chicken, end_num)
nCr = list(nCr)


tmp_graph = copy.deepcopy(graph)
for line in nCr:
    for (x,y) in line:
        tmp_graph[x][y]=0
    # 조합 한번 수정 
    
    ################디버깅용
    #for line in tmp_graph:
    #    print(line)
    ####################3
    # 집 기준으로 최소 거리 찾고, 그거 다 더한다. 
    left_chickens = list(set(chicken) - set(line))  # 남은 치킨집
    for (x,y) in house:
        short = find_shortest_distance(x,y,left_chickens)
        distance+=short
    
    min_distance = min(min_distacne, distance)
        
print(min_distance)
