from bisect import bisect_left, bisect_right

def count_by_range(array, left_val, right_val):
    right_index = bisect_right(array, right_val)
    left_index = bisect_left(array, left_val)

    return right_index - left_index

n, x = map(int, input().split())
array = list()

count = count_by_range(array, x, x)

if count == 0:
    print(-1)

else:
    print(count)

    