# nxm금광
# 테스트 T
# n x m 이 공백으로
# n x m 의 매장된 금 개수

T = int(input())

# 풀이 확인하고 품..

for _ in range(T):

    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    map = []
    index = 0
    for x in range(N):
        map.append(data[index:index+M])
        index += M
    
    for j in range(1, M):
        for i in range(N):
            
            if i == 0:
                left_up = 0
            else:
                left_up = map[i-1][j-1]
            
            if i == (N-1):
                left_down = 0
            else:
                left_down = map[i+1][j-1]

            left = map[i][j-1]
            map[i][j] = map[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(N):
        result = max(result, map[i][M-1])

    print(result)