# https://medium.com/@dltkddud4403/2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EB%B8%94%EB%9D%BC%EC%9D%B8%EB%93%9C-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EA%B4%84%ED%98%B8-37ad7be7acd6
# 균형잡힌 괄호 문자열인지 체크하는 함수
def isbalanced(s):
	chk=0
	for c in s:
		if c=='(': chk+=1
		elif c==')': chk-=1

	if chk==0: return True
	else: return False

# 올바른 괄호 문자열인지 체크하는 함수
def iscorrect(s):
	stack=[]
	stack.append(s[0])
	for i in range(1,len(s)):
		if len(stack)==0 or stack[-1]==')' or (stack[-1]=='(' and s[i]=='('):
			stack.append(s[i])
		else:
			stack.pop()
	if len(stack)==0: return True
	else: return False


def solution(p):
	answer = ''
	u=""
	v=""
	#빈 문자열이나 올바른 괄호 문자열은 그대로 반환
	if len(p)==0 or iscorrect(p): return p

	#u가 균형잡힌 괄호 문자열이 될 때까지 2개씩 추가해서 u,v 나누기
	for i in range(2,len(p)+1,2):
		if isbalanced(p[0:i]):
			u=p[0:i]
			v=p[i:len(p)]
			break

	if iscorrect(u):
		#u가 올바른 괄호 문자열일 때
		answer+=u+solution(v)
	else:
		#u가 올바른 괄호 문자열이 아닐 때
		answer+='('+solution(v)+')'
		for c in u[1:-1]:
			if c=='(': answer+=')'
			else: answer+='('

	return answer