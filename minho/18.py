# () 개수가 같으면 균형잡힌 괄호문자열
# () 괄호의 짝도 모두 맞을 경우 올바른 괄호 문자열

def check_index(p):

    count = 0

    # 균형잡힌 문자열 체크 () 개수만 맞으면 됨
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

def checks(p):
    # 3. 올바른 문자열이면 체크 맞으면 v 1 단계 부터 다시 실행해야함
    count = 0

    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False

            count -= 1

    return True

def solution(p):
    answer = ''

    # 1. 빈 문자열이면 반환
    if p == '':
        return answer

    idx = check_index(p)

    # 2. 문자열 분열
    u = p[:idx+1] # 균형잡힌 문자열 idx
    v = p[idx+1:] # 그 뒤에 값들

    print(checks(u))

    if checks(u):
        answer = u + solution(v)
    else:
        # 4. 올바른 문자열 아닐 경우 진행
        answer = '('
        answer += solution(v)
        answer += ')'

        # 4-4 첫 번째 문자와 마지막 문자 제거 및 괄호 방향 뒤집기
        u = list(u[1:-1])

        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
            answer += ''.join(u)

    return answer

data = solution('()))((()')
print(data)