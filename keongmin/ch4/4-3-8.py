# 내 풀이
S = input()

char = []
nums = 0

for s in S:
    if s.isdigit():
        nums += int(s)
    else:
        char.append(s)

char.sort()
result = ''.join(char)

if not nums:
    print(result + str(nums))
else:
    print(result)
