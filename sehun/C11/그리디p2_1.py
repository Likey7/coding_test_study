# N, M, K 를 입력받는 코드
N, M, K = map(int, input().split())

#N개의 자연수 입력받기
data = list(map(int, input().split()))

data.sort()
first = data[N-1]
second = data[N-2]

result = 0

while True:
  for i in range(K):
    if M == 0:
      break
    result += first
    M -= 1

  if M == 0:
    break

  result += second
  M -= 1

print(result)