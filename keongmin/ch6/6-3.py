N = int(input())
scores = []

for _ in range(N):
    new = input().split()
    scores.append((new[1], new[0]))

scores.sort()

for score in scores:
    print(score[1], end=" ")