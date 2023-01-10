# 내 풀이
location = input()
x = ord(location[0]) - ord("a") + 1
y = int(location[1])

levels = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

result = 0
for a, b in levels:
    nx = x + a
    ny = y + b

    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue

    result += 1

print(result)
