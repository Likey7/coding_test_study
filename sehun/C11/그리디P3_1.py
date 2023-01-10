n = input()
d = list(map(int, input().split()))
group_num = 0
d.sort()

idx = 0

#공포도 1~ N까지 그룹 계산
for i in range(1, max(d)+1):
  if len(d) <= i:
    break

  while True:
    if max(d[:i]) <= i:
      del d[:i]
      group_num += 1
    else:
      break
    
print(group_num)


