# 점수 N, 자릿수를 기준으로 점수 N을 반으로 나누어 왼쪽 합과 오른쪽 합의 값이 동일할때 럭키스트레이트
# 항상 짝수

N = int(input())

Nn = len(str(N))//2

F = str(N)[0:Nn]
S = str(N)[Nn:len(str(N))]

first = 0
second = 0

for i in F:
    first += int(i)

for i in S:
    second += int(i)

if first == second:
    print('LUCKY')
else:
    print('READY')