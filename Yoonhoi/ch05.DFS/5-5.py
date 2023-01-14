def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *=1
    return result

factorial_iterative(5)

def factorial_recursive(n):
    if n<=1:
        return 1
    return n*factorial_recursive(n-1)

factorial_recursive(5) 