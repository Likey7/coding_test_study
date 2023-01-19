n, m = map(int, input().split())
money = [int(input()) for _ in range(n)]

d = [10001] * 10001
d[0] = 0

for i in range(1, m+1):
  for k in money:
    if i-k != 10001:
      d[i] = min(d[i],d[i-k]+1)

if d[m] == 10001:
  print(-1)
else:
  print(d[m])
