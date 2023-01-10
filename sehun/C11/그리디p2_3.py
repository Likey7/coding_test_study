N, K = map(int, input().split())
count = 0

# #최대한 K로 나누는 방향을 추구(그리디)
# while True:
#   #N이 1이면 루프중지
#   if N == 1:
#     break

#   #K로 나눠지면 나누고 안된다면 -1하기
#   if N % K == 0:
#     N = N / K
#     count += 1
#   else:
#     N -= 1
#     count += 1
# print(count)

while True:
  temp = N%K
  count += temp
  N -= temp

  if N<K:
    break

  N = N//K
  count+=1

count +=(N-1)
print(count)

  

  
