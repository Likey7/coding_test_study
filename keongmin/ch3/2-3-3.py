# 내 풀이
N, M = map(int, input().split())

result = 0

for i in range(N):
    now = list(map(int, input().split()))
    result = max(result, min(now))

print(result)

# 책 풀이
N, M = map(int, input().split())

result = 0

for i in range(N):
    data = list(map(int, input().split()))
    min_value = 1001

    for a in data:
        min_value = min(min_value, a)

    result = max(result, min_value)

print(result)