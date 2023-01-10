def add_or_multiply(input):
    """
    Parameter
    """
    lst = list(map(int, input))

    fst = lst[0]
    snd = lst[1]

    if fst == 0 or snd == 0:
        result = fst + snd
    else:
        result = fst * snd

    for i in range(2, len(lst)):
        if lst[i] != 0:
            result *= lst[i]

    return result

print(add_or_multiply("14203"))