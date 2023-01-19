dp = []
dp.append(1)

n = 1000

for i in range(n):
    if len(dp) > n:
        dp.sort()
        print(dp[n])
        break
    to_multi = dp[i]
    multi_2 = to_multi * 2
    multi_3 = to_multi * 3
    multi_5 = to_multi * 5
    multi = [multi_2, multi_3, multi_5]
    for mt in multi:
        if mt in dp:
            continue
        dp.append(mt)
    



