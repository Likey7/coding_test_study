n = int(input())
a = list(map(int, input().split()))
a.sort()

# 중간값(median)을 출력
print(a[(n - 1) // 2])


# n = int(input())
# house_loc = list(map(int, input().split()))

# answer = [0 for _ in range(n)]

# for i in range(n):
#   sum = 0
#   for j in range(n):
#     sum += abs(house_loc[i] - house_loc[j])
#   answer[i] = sum

# a= house_loc[answer.index(min(answer))]
# print(a)

