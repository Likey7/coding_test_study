stack = []

stack.append(5)
stack.append(2)
stack.append(7)
print(stack)
x= stack.pop()
print(stack)
print(x)
stack.append(1)
stack.append(2)

print(stack)
print(stack[::-1]) # 최상단 원소부터 출력 