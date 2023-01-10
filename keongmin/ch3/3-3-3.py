# 내 풀이
S = input()
nums = [int(s) for s in S]

result = [0, 0]

if nums[0] == 0:
    result[0] += 1
else:
    result[1] += 1

start = nums[0]

for i in range(1, len(nums)):
    if nums[i] != start:
        result[nums[i]] += 1
        start = nums[i]

print(min(result))

# 책 풀이
data = input()
count0 = 0
count1 = 1

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))