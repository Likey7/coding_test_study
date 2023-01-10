# 내 풀이
N = int(input())
nums = list(map(int, input().split()))
nums.sort()

cnt = nums[-1]
result = 0
while nums and cnt <= len(nums):
    if cnt == 0:
        result += 1
        cnt = nums[-1]
    else:
        cnt -= 1
        nums.pop()

print(result)

# 책 풀이
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)