# n이 주어짐 둘째 줄 부터 n+1 줄까지 삼각형
# 첫째 줄에 합이 최대가 되는 경로에 있는 수의 합

n = int(input())
dp = []
for _ in range(n):
  dp.append(list(map(int, input().split())))

for i in range(1,n):
  for j in range(len(dp[i])):

    if j == 0:

      dp[i][j] = dp[i][j] + dp[i-1][j]

    elif j == len(dp[i]) - 1: 

      dp[i][j] = dp[i][j] + dp[i-1][j-1]

    else:

      dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + dp[i][j]

print(max(dp[n-1]))