mine = [[1,3,3,2],
        [2,1,4,1],
        [0,6,4,7]]

n = len(mine)
m = len(mine[0])
dp = [[0 for col in range(m)] for row in range(n + 2)]
dp[1][0] = 1
dp[2][0] = 2
dp[3][0] = 0
# i i i i 
# i i i i 
# i i i i

for i in range(1, m):
    for j in range(1, n+1):
        dp[j][i] = mine[j-1][i] + max(dp[j-1][i-1], dp[j][i-1], dp[j+1][i-1])
result = max(dp[1][m-1], dp[2][m-1], dp[3][m-1])

print(result)
