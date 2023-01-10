def solution(s):
    answer = len(s)
    max_len = len(s)//2
    
    for i in range(1, max_len + 1):
        temp = ''
        search = s[:i]
        num = 1
        
        for j in range(i,len(s),i):
            if search == s[j:j+i]:#만약 문자열이 같다면 +1
                num+=1
            else: #문자열이 다르다면
                temp+=str(num)+search if 2 <= num else search
                search = s[j:j+i]
                num = 1
        
        #뒤에 문자열 저장
        temp+=str(num) + search if 2<=num else search
        answer = min(answer, len(temp))
            
    return answer

s = input()
print(solution(s))