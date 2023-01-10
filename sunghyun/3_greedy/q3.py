def string_invert(input):
    lst = list(map(int, input))
    group0 = 0
    group1 = 0

    is0 = False

    for i in lst:
        if lst[i] == 0:
            if not is0:
                is0 = True
                group0 += 1
        
        else:
            if is0:
                is0 = False
                group1 += 1

    return max(group0, group1)

print(string_invert("0001100"))