x = [1,3,1,5]

dp = [0] * (len(x)+2)

dp[0] = x[0]
dp[1] = max(x[0], x[1])

for i in range(2, len(x)):
    dp[i] = max(x[i-1], x[i-2] + x[i])

print(dp[len(x) - 1])