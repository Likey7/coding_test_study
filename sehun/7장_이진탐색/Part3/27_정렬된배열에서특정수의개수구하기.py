n, x = map(int, input().split())
number = list(map(int, input().split()))

from bisect import bisect_left, bisect_right

def count_num(number, left_v, right_v):
  ri = bisect_right(number, right_v)
  li = bisect_left(number, left_v)
  return ri - li

count = count_num(number, x, x)

if count == 0:
    print(-1)
else:
    print(count)