n = input()
coin = list(map(int, input().split()))
coin.sort()

i=1

for j in coin:
  if i< j:
    break
  i += j

print(i)