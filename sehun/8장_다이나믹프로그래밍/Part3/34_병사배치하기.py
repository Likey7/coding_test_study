# #병사의 수가 최대가 되어야하고 내림차순 정렬
# n = int(input())
# soldier = list(map(int, input().split()))

# d = [0] * n
# count = 0

# #그냥 무지성 작은수나오면 빼볼까
# for i in range(n-2, -1, -1):
#   if soldier[i] < soldier[i+1]:
#     count+= 1
  
# print(count)

########################################
########################################
#최장증가수열 (LIS 알고리즘?)

n = int(input())
soldier = list(map(int, input().split()))

d = [1] * n

#LIS사용
for i in range(1, n):
  for j in range(0, i):
    if soldier[j] < soldier[i]:
      d[i] = max(d[i], d[j]+1)

#총병사수 - 사용할병사수 = 열외병사수
print(n-max(d))


