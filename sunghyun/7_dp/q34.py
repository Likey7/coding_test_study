soldier = [15, 11, 4, 8, 5, 2, 4]

dp = [1] * len(soldier)

soldier.reverse()

max_length = 1
strongest = soldier[0]

for i in range (1, len(soldier)):
    if soldier[i] > strongest:
        max_length += 1
        strongest = soldier[i]

print(max_length)
