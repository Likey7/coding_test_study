s = list(map(int, input()))
temp = 3

mem = [0, 0]
for i in s:
  if temp != i:
    mem[i] +=1
    temp = i

print(min(mem))

