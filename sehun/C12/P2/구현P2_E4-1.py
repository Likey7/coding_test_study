N = int(input())
CMD = list(input().split())
X, Y = 1, 1

for i in CMD:
  if i == 'R' and Y < N:
    Y+=1
  elif i == 'L' and Y > 1:
    Y-=1
  elif i == 'U' and X > 1:
    X-=1
  elif i == 'D' and X < N:
    X+=1

print(X,Y)
