# 내 풀이
S = input()
nums = [int(s) for s in S]

result = nums[0]

for i in range(1, len(nums)):
    if result in (0, 1):
        result += nums[i]
    elif nums[i] in (0, 1):
        result += nums[i]
    else:
        result *= nums[i]

print(result)

# 책 풀이
data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])

    if num <= 1 or result <= 1:
        result += num
    else:
        result *- num

print(result)