counsel = [[3,  5,  1,  1,  2,  4,  2],
           [10, 20, 10, 20, 15, 40, 200]]
N = len(counsel[0])
dp = [0] * (N + max(counsel[0]))

for i in range(N-1, -1, -1):
    if counsel[0][i] + i > N:
        continue
    dp[i] = counsel[1][i] + dp[counsel[0][i] + i]

print(max(dp))

