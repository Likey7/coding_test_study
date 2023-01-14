# 19. 연산자 끼워넣기  
# https://data-flower.tistory.com/72
# # 최대와 최소의 값 
# DFS

n= int(input())
data = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())


max_value = -1e9
min_value = 1e9


def dfs(i,arr):
    if i==n: 
        max_val = max(max_value,arr)
        min_val = min(min_value, arr)
    else:
        if add >0:
            add -=1
            dfs(i+1, arr+data[i])
            add+=1
        if sub >0:
            sub-=1
            dfs(i+1, arr - data[i])
            sub+=1
        if mul > 0:
            mul-=1
            dfs(i+1, arr* data[i])
            mul+=1
        if div > 0:
            div-=1
            dfs(i+1, int(arr/data[i]))
            div+=1
dfs(1,data[0])
print(max_value)
print(min_value)