N = int(input())

# 바닥을 채우는 모든 경우의 수 
d = [0] *1001

d[1]=1
d[2]=3
for i in range(3,N+1):
    d[i]= (d[i-1] + 2*d[i-2]) % 796796
    
    
print(d[N])