import sys
input=sys.stdin.readline # 이거 넣으면시간 10배정도 빠름 
N = int(input())
table = []
for _ in range(N):
    line  = input().split()
    name,korean, english, math = line[0], int(line[1]), (100-int(line[2])),int(line[3])
    ascii_name = [-x for x in list(map(ord,list(name)))]
    new = [korean, english, math]+ ascii_name +[0]*(10-(len(ascii_name))) +[name]
    table.append(new)
    
table = sorted(table,reverse = True)#sort 함수의 경우 
for line in table:
    print(line[-1])

print(*map(lambda x:x[-1], sorted(table,reverse = True)))
# 여기서 * 은 map 함수로 패킹된 것을 풀어주는 역할? 
# 시간이 엄청 아껴지는것은 아닌 것으로 보임 ㅋㅋ