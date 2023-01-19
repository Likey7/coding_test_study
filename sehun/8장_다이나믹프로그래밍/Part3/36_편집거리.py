a = list(input())
b = list(input())
n = len(a)
d = [1] * n

#LIS 변형...?
for i in range(1, n):
  for j in range(0, i):
    if a[j] < a[i]:
      d[i] = max(d[i], d[j]+1)

print(n - max(d))