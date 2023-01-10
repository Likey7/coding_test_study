def stringparse(input):
    alphalist = [alpha for alpha in input if alpha.isalpha()]
    alphalist.sort()
    intlist = [i for i in input if i.isdigit()]
    result_str = "".join(alphalist + intlist)
    print(result_str)

stringparse("SADJ123SAF512")