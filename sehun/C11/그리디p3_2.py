num_list = list(map(int, input()))

print(num_list)
sum = 0

for i in num_list:
  if sum != 0 and i != 0:
    sum *= i
  else:
    sum += i

print(sum)

