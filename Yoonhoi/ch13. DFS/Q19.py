n = int(input())
data = list(map(int,input().split()))
plus, minus, div, mul = map(int,input().split())

min_value = +1e9
max_value = -1e9

def DFS(i, arr):
    if i==n: # 연산지를 다 채웠다면!
        min_value = min(min_value,arr)
        max_value = max(max_value,arr)
    else:
        if plus>0:
            plus-=1
            DFS(i+1,arr+data[i])
            plus+=1
        if minus>0:
            minus-=1
            DFS(i+1,arr-data[i])
            minus+=1
        if div>0:
            div-=1
            DFS(i+1,arr*data[i])
            div+=1
        if mul>0:
            mul-=1
            DFS(i+1,int(arr/data[i]))
            mul+=1
    
    
    
    
DFS(1,data[0])
print(min_value)
print(max_value)