def big_num(lst, m, k):
    list_sorted = sorted(lst)
    print(list_sorted)
    fst = list_sorted[-1]
    snd = list_sorted[-2]
    fst_count = k*(m//(k+1)) + m%(k+1)
    snd_count = m - fst_count
    result = fst * fst_count + snd * snd_count


    # for i in range (m):
    #     if (i+1)%(k+1) == 0:
    #         result += snd
    #     else: 
    #         result += fst
    return result

print(big_num([1,5,6,8], 8, 3))
