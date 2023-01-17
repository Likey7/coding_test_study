import sys
input = sys.stdin.readline
'''
def get_distance(x,points):
    here = points[x]
    last = points[:x]+points[x+1:]
    return sum([abs(here - one) for one in last])


def quick_sort(array):
    if len(array) <=1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <=pivot]
    right_side = [x for x in tail if x >pivot]
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
'''

N = int(input())
house = list(map(int,input().split()))
house.sort()
print(house[int((N-1)/2)])