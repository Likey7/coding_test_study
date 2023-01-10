# 문자열 뒤집기 
# 앞에서부터 보면서 0>1>0 으로 바뀌는 순간을 센다. 
# 바뀌는 순간/2 에서 소숫점 버림을 하면 답

S = list(map(int,list(input())))

check = S[0]
count =0

for x in S[1:]:
    print(x,check)
    if check==x:
        continue
    else:
        count+=1
        check=x
        
answer = int((count+1)/2)
print(answer)