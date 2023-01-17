n, c = map(int, input().split())
home = [int(input()) for _ in range(n)]
home.sort()


start = 1 
end = home[-1] - home[0] 
result = 0

while(start <= end):
    mid = (start + end) // 2 
    value = home[0]
    count = 1
    for i in range(1, n): 
        if home[i] >= value + mid:
            value = home[i]
            count += 1
    if count >= c: 
        start = mid + 1
        result = mid 
    else:
        end = mid - 1



print(result)