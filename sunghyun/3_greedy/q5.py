def bowling(m,lst):
    result = 0
    count = [None] * m
    for i in range (m):
        count[i] = lst.count(i+1)
    print(count)
    n = len(lst)
    for c in count:
        result += ((n-c)*c)
        n -= c 
    return result 

print(bowling(3, [1,3,2,3,2]))