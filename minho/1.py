# 모험가 N명 공포도 X인 모험가는 반드시 X명 이상으로 구성한 모험가만 가능
# N 명의 모험가 정보가 주어졌을때 여행을 떠날 수 있는 그룹 수의 최댓값
# N = 5 // 2 3 1 2 2 = 2개의 그룹 // 123 그룹 1 22 그룹 2 총 2
# 공포도는 N이하의 자연수

N = int(input())

A = []
for _ in range(N):
    A.append(int(input()))

A.sort(reverse=True)

if A[0] == N:
  print(1)
else:
  B = 0
  C = len(A)

  while True:
    
    C = C-A[0]
    del A[0:A[0]]
    B += 1

    if C <= 0:
        break

  print(B)
