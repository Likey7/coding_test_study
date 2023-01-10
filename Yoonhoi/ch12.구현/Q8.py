s = input()
nums = '1234567890'
alpha = [x for x in s if x not in nums]
numbers = [int(x) for x in s if x  in nums]
total = sum(numbers)
print(''.join(sorted(alpha))+str(total))
