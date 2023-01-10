def foo(n, k):
    count = 0
    while True:
        if n == 1:
            break
        elif n%k == 0:
            n //= k # n = n//k 
            count += 1
        else:
            n -= 1
            count += 1
    return count

print(foo(1000000000000, 23))