N = int(input())
K = list(map(int, input().split()))

dp = [0 for _ in range(1001)]

dp[0] = K[0]
dp[1] = max(K[0], K[1])

for i in range(2, N):
    dp[i] = max(dp[i - 1], K[i] + dp[i - 2])

print(max(dp))