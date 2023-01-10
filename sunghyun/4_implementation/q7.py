def luckystrike(score):
    digits = [int(d) for d in str(score)]
    half = len(digits)//2
    fst = 0
    snd = 0
    for i in range(half):
        fst += digits[i]
        snd += digits[half+i]
    if fst == snd:
        print("LUCKY")
    else:
        print("READY")

luckystrike(123402)