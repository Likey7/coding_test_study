# 고정점 찾기 

import sys
f = sys.stdin.readline

n = int(input())
array = list(map(int, f().split()))

def bin_search(array,start,end):
    if start>end:
        return None
    mid = (start+end)//2
    
    if array[mid] ==mid:
        return mid
    elif array[mid]<mid:
        return bin_search(array,mid+1,end)
    else:
        return bin_search(array,start,mid-1)

fix = bin_search(array,0,n-1)


if fix:
    # 고정점은있어도 한개
    print(fix)
else:
    print(-1)