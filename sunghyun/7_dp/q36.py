a = "sunday".split()
b = "saturday".split()

dp = [0] * len(a)

for i in range(len(b)):
    if not a[i] == b[1]:
        