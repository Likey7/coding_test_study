n, m = map(int, input().split())
parent = [0] * (n+1)

#자기자신 부모로 초기화
for i in range(1, n+1):
  parent[i] = 1

def find_paraent(parent, x):
  if parent[x] != x:
    parent[x] = find_paraent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_paraent(parent, a)
  b = find_paraent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

for i in range(n):
  data = list(map(int, input().split()))
  for j in range(n):
    if data[j] == 1:
      union_parent(parent, i+1, j+1)

plan = list(map(int, input().split()))

result = True


#결과확인하기
temp = find_paraent(parent, plan[0])
for i in range(len(plan)):
  if temp != find_paraent(parent, plan[i]):
    result = False
    break

if result == True:
  print("yes")
else:
  print("no")