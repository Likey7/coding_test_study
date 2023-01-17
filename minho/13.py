# 첫째 줄에 N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)이 주어진다.
# 둘째 줄부터 N개의 줄에는 도시의 정보가 주어진다.
# 도시의 정보는 0, 1, 2로 이루어져 있고, 0은 빈 칸, 1은 집, 2는 치킨집을 의미한다. 
# 집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재한다. 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.

N, M = map(int, input().split()) # 

_map = []
home = []
chicken = []

for i in range(N):
    _map.append(list(map(int, input().split())))

    for j in range(N):
        
        if _map[i][j] == 2:
            chicken.append((i, j))

        if _map[i][j] == 1:
            home.append((i, j))


totalA = []
for i in home:
    result = 0
    x, y = i

    for j in chicken:
        cx, cy = j

        total = abs(x - cx) + abs(y - cy)
        
        if result == 0:
            result = total
        totalA.append(result)
        if result > total:
            result = total
            


print(totalA)
print(result)
