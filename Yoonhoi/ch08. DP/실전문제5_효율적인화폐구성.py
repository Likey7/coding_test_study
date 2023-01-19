N,M = map(int,input().split())
values = [int(input()) for _ in range(N)]

money = [10001]*(M+1)
money[0] =0


for i in range(N):
    for j in range(values[i], M+1):
        if money[j - values[i]] != 10001:
            money[j] = min(money[j],money[j-values[i]]+1)
        

if money[M] == 10001:
    print(-1)
else:
    print(money[M])