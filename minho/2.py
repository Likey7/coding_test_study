# 0~9 문자열 S *, + 연산자를 넣어 가장 큰 수

S = input()

total = 0
for i in S:
    if int(i) <= 1 or total <= 1:
        total += int(i)
    else:
        total *= int(i)
print(total)