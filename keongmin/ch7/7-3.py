N, M = map(int, input().split())
items = list(map(int,input().split()))

start = 0
end = max(items)

result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0

    for item in items:
        now = item - mid
        if now > 0:
            total += now

    if total >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)