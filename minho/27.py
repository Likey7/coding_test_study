import sys
from bisect import bisect_left, bisect_right

N, x = sys.stdin.readline().split()

data = sys.stdin.readline().split()

# 이미 정렬된 값이라 사용해도 됨
right = bisect_right(data, x)
left = bisect_left(data, x)


cnt = right - left

if not cnt:
    print('-1')
else:
    print(cnt)