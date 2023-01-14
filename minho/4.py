# N개의 동전
# N개의 동전을 만들 수 없는 양의 정수 최솟값
# N = 5일때 3, 2, 1, 1, 9 만들 수 없는 최솟값은 8원

n = int(input())

won = list(map(int, input().split()))

won.sort()

result = 1

for i in won:
    if result < i:
        break
    result += i

print(result)