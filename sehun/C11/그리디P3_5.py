n, m = map(int, input().split())
ball_list = list(map(int, input().split()))

count = 0

for i in range(len(ball_list)):
  for ball in ball_list[i+1:]:
    if ball != ball_list[i]:
      count += 1

print(count)

