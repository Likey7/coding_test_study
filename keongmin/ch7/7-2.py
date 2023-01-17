N = int(input())
N_nums = list(map(int, input().split()))
M = int(input())
M_nums = list(map(int, input().split()))

N_nums.sort()

def binary(num, N_nums):
    start = 0
    end = len(N_nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if N_nums[mid] < num:
            start = mid + 1
        elif N_nums[mid] > num:
            end = mid - 1
        else:
            return True

    return False

for m in M_nums:
    if binary(m, N_nums):
        print('yes', end=" ")
    else:
        print('no', end=" ")

