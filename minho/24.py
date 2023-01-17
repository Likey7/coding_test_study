# 특정 위치에 위치 했을때 최소값이 되는지

N = int(input())

data = list(map(int, input().split()))

data.sort()

print(data[(N-1)//2])

