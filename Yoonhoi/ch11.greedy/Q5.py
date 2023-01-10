
from itertools import combinations
# 조합(combination 을 만들어주는 라이브러리 사용)
N, M =map(int,input().split())
balls = list(map(int,input().split()))

# 1부터 M (1<=M<=10) 까지의 개수를 세서 저장하는 리스트 만든다. 
count = [0]*11

for K in balls:
    count[K] +=1
    
# manyballs 2개 이상중복한 공이 있는 것들만 따로 뺀다
manyballs=[]
for check in count:
    if check>=2:
        manyballs.append(check)


# nC2 - { aC2 +bC2 + ... kC2}
total =  len(list(combinations(range(N), 2)))
for x in manyballs:
    a = len(list(combinations(range(x), 2)))
    total -=a

print(total)