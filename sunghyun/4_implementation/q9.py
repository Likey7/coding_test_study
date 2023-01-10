def solution(s):
    repeat = len(s) // 2 + 1
    result = [len(s)] * repeat

    #i가 몇개 단위인지
    #unit은 i개로 이루어진 비교 단위
    #count는 unit이 몇 번 반복됐는지
    
    for i in range (1, repeat):
        unit = s[0:i]
        count = 1
        compressed = ""
        for j in range (i, len(s), i):
            if s[j:j+i] == unit:
                count += 1
            else:
                compressed += str(count) + unit if count >= 2 else unit
                unit = s[j:j+i]
                count = 1
        compressed += str(count) + unit if count >= 2 else unit
        print(compressed)
        result[i] = len(compressed)
    print(result)
    answer = min(result)
    return answer
    
print(solution("aaaaabbccc"))