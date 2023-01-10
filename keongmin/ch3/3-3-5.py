# 내 풀이
import collections

N, M = map(int, input().split())
balls = list(map(int, input().split()))
nums = collections.defaultdict(int)

for i in balls:
    nums[i] += 1

result = 0
for ball in balls:
    N -= 1
    nums[ball] -= 1
    result += (N - nums[ball])

print(result)

# 책 풀이
n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11

for x in data:
    array[x] += 1

result = 0
for i in range(1, m + 1):
    n -= array[i]
    result += array[i] * n

print(result)