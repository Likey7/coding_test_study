import sys
f = sys.stdin.readline

n = int(input())
store = list(map(int, f().rstrip().split()))
store.sort()
m = int(input())
customer = list(map(int, f().rstrip().split()))

print(n,m)
print(store)
print(customer)

def bin_search(array, target, start, end):
    while start <= end:
        mid = (start + end) //2
        if array[mid] ==target:
            return mid
        elif array[mid]>target:
            end = mid-1
        else : 
            start = mid+1
    return None

for item in customer:
    result = bin_search(store, item, 0, len(store)-1)
    if result!=None:
        print('yes',end = ' ')
    else:
        print('no',end = ' ')