# 정렬된 배열에서 특정 수의 개수 구하기 
import sys
f = sys.stdin.readline

n,m = map(int, input().split())
array = list(map(int, f().split()))

def bin_search(array,target, start, end):
    if start >end:
        #같을 때 까진 해야함
        return None
    mid = (start +end )//2
    
    if array[mid]==target:
        return mid
    elif array[mid]<target:
        return bin_search(array,target,mid+1,end )
    else:
        return bin_search(array,target,start,mid-1)
    return None

result = bin_search(array, m, 0, n-1)

def count_num(array, m, n):
    left, right = m , m
    while left>=0 and array[left]==array[m]:
        left -=1
        
    while right <=n-1 and array[right]==array[m]:
        right+=1
        
    return right-left -1


if result :# 값이 존재한다면 
    print(count_num(array,result,n))
else:
    print(-1)