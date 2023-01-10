s = list(input())
s_s = [] #문자 담아놓을 변수
s_n = [] #숫자 담아놓을 변수

for i in s:
  num = ord(i) #아스키코드로 변환
  
  #만약 문자일경우
  if 64 < num and num < 91:
    s_s.append(num)
  #숫자일 경우
  else:
    s_n.append(num)

s_s.sort()
s_n.sort()
answer = ''.join(chr(i) for i in s_s + s_n)

print(answer)



