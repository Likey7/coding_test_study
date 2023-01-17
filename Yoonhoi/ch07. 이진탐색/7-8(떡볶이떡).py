import sys
f = sys.stdin.readline
n,m = map(int,input().split())

array = list(map(int, input().split()))
max_len = max(array)

def get_amount(array, cut):
    total = 0
    for x in array :
        if x>cut:
            total += (x-cut)
    return total 

# 이 경우 딱 맞을 수 없기 때문에 그냐 끝까지 서치를 하고, 작으면 왼쪽을 계속 더 자르고 넘치면 오른쪽에서 계속 더 자른다. 
# 끝까지 돌려서 마지막 답이 나옴, 
# while start < = end 라는 조건 같아도된다. 같은 항목 가리키는 경우 까지 탐색하는 것 
def bin_search(array, target, start, end):
    
    
    while start <=end :
        mid  = (start +end)//2
        amount = get_amount(array,mid)
        
        
        if amount <target : 
            end = mid-1
        else:
            result = mid
            start = mid +1
            
    return result
             
result = print(bin_search(array, m,0, len(array)))
    
    
bin_search(array, m, 0, max_len)
print(result)