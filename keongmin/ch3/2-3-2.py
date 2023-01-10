# 내 풀이
N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse=True)

first = nums[0]
second = nums[1]

result = 0
cnt = 0
for i in range(M):
    if cnt >= K:
        result += second
        cnt = 0
        continue

    cnt += 1
    result += first

print(result)

# 책 풀이
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)