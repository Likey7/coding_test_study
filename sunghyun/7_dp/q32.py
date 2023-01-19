import copy

tree = [[7],
        [3,8],
        [8,1,0],
        [2,7,4,4],
        [4,5,2,6,5]]

dp = copy.deepcopy(tree)
for i in range(len(dp)):
    for j in range(len(dp[i])):
        dp[i][j] = 0


dp[0][0] = tree[0][0]

for i in range(1, len(dp)):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = tree[i][j] + dp[i-1][j]
        elif j == len(dp[i]) - 1:
            dp[i][j] = tree[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = tree[i][j] + max(dp[i-1][j], dp[i-1][j-1])

result = max(dp[len(tree)-1])
print(result)