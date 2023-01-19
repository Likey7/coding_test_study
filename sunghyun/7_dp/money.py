n = [3,5,7]
m = 50

dp = [10001] * (m+1)

for i in range(m):
    if i % n[i]:
        dp[i] = 