# 내 풀이
N, K = map(int, input().split())

result = 0
while N != 1:
    if N % K != 0:
        N -= 1
    else:
        N //= K

    result += 1

print(result)

# 책 풀이
n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break

    result += 1
    n //= k

result += (n - 1)
print(result)