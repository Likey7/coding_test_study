# 같은 문자가 반복되면 2~~로 써줌 남는건 붙여줌 단어 한개가 아닌 여러개도 가능 가장 짧은 것 구하기

s = input()

lastCnt = []

for i in range(len(s)):

    total = len(s)
    
    # i+1은 현재 몇개씩 체크할건지
    nowLen = i+1
    nowStr = ''
    checkCnt = 1

    #data는 데이터의 맨 앞글자 수 +1 씩 처음엔 a aa이런식
    data = s[0:i+1]
    jch = ''
    
    for j in range(nowLen, len(s)+i+1, nowLen): #len()은 s의 nowLen 자리부터 +nowLen씩 끝까지 마지막 한번 더 돌려야됨
        jch += str(j)
        
        if data == s[j:j+nowLen]:
            checkCnt += 1
            
        else:
            if checkCnt > 1:
                nowStr += str(checkCnt)+data
            else:
                nowStr += data
                
            # print(data)
            # print(j)
            checkCnt = 1
            data = s[j:j+nowLen]

    # print(jch)
    print(nowStr)#aabbaccc
    lastCnt.append(len(nowStr))

print(min(lastCnt))
