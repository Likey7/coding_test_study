N, M = map(int, input().split())

temp = 0

for i in range(N):
  data = list(map(int, input().split()))
  temp = max(min(data),temp)

print(temp)