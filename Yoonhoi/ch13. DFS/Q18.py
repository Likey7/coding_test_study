# 입력
#w = input()
w = '(()())()'  # 인풋에서  ( ) 개수는 같음 


# 균형잡힌 괄호 문자열 개수 같음
# 올바른 괄호 문자열 짝 맞음 

# 1. 입력이 빈문자열이라면 빈 문자열 반환

# 2. 문자열 w 를 균향잡힌 괄호 문자열 u,v 로 분리 
# u 는 균형잡힌 괄호 문자열로 더 이상 분리할 수 없어야 하며 
# v 는 빈문자열일 수 있다. 


# 3. 수행한결과 문자열을 u에 이어 붙인 후 반환합니다. 
# 3-1 문자열 u 가 올바른 괄호 문자열 이라면 문자열 v 에 대해 1단계부터 다시 수행합니다. 


# 4.   문자열 u 가 올바론 괄호 문자열이 아니라면 
#  4-1 빈 문자열에 첫 번째 문자로 ( 를 붙인다. 

# 4-2  문자열 v 에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙인다. 
# 4-3 ) 를 다시 붙인다. 

# 4-4 u 의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙인다. 
# 4-5 생성된 문자열 반환 



w = ')('


def solution(w):
    
    u=''
    v=''
    if w=='':
        return ''
    
    if is_check(w):
        return w
    
    stack = []
    top = w[0]
    stack.append(top)

    for i,val in enumerate(w[1:]):
        if top!=val:
            stack.pop()
            if stack ==[]:
                u,v = w[:i+2], w[i+2:]
                break
        else:
            top = val
            stack.append(top)
    
    return change(u)+ solution(v) 


# 올바른 문자열인지 확인?
def is_check(ss):
    
    stack=[]
    for x in ss:
        if x=='(':
            stack.append(x)
        
        else : 
            if stack:
                stack.pop()
            else:
                return False
    return True
            

def reverse(x):
    if x=='(':
        return ')'
    else : 
        return '('

def change(u) :
    reversed = [] # 나머지 문자의 괄호 방향을 뒤집으면 
    for x in  u[1:-1]:
        reversed.append(reverse(x)) 
    
    new =  '(' +''.join(map(str, reversed)) + ')'
    return new


print(solution("()))((()"))