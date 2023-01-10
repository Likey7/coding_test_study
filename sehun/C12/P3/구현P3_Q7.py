n = input()

idx = int(len(n)/2)
front = list(map(int, n[:idx]))
back = list(map(int, n[idx:]))

if sum(front) == sum(back):
  print("LUCKY")
else:
  print("READY")