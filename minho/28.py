import sys


N = int(input())

data = list(map(int, input().split()))

def binary_search(data, start, end):

    while start <= end:
        mid = (start + end) // 2
        
        if data[mid] == mid:
            return mid
        elif data[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
        
    return -1

# 이미 정렬된 값이라 사용해도 됨
result = binary_search(data, 0, N-1)
print(result)