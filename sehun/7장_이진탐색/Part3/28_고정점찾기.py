n = int(input())
number = list(map(int, input().split()))

def binary_search(number, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if number[mid] == mid:
        return mid
    elif number[mid] > mid:
        return binary_search(number, start, mid - 1)
    else:
        return binary_search(number, mid + 1, end)

idx = binary_search(number, 0, n-1)

if idx == None:
  print(-1)
else:
  print(idx)