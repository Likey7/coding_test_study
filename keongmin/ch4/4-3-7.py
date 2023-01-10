# 내 풀이
N = input()
nums = [int(i) for i in N]
mid = len(N) // 2

sumNum = sum(nums)

if sum(nums[mid:]) == sum(nums[:mid]):
    print("LUCKY")
else:
    print("READY")
