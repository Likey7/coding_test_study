#100만개 이하면 걍 완전탐색 사용하면 된대
#이건 86400개밖에 안되서 완전탐색사용
N = int(input())
count = 0

for i in range(N+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i)+str(j)+str(k):
        count += 1

print(count)