n = int(input())
ppl=[(0,0)]
for i in range(n):
    ppl.append(list(map(int,input().split())))
    


dp = [0]*(n+1)

# dp[1=]
# dp[i] = max(dp[1]~ dp[i-1])

for i, (t,p) in enumerate(ppl):
    #print()
    #print(i,t,p)
        # 만약 상담이 끝나는 일에  근무일 마지막보다 같거나 작은 경우 에만 상담 진행 가능
    if i+t <= n :
        today = p
    else : 
        today =0
        
    # 앞선 상담비용중 가장 높은 비용 찾기, 단 일자가 넘어오지 않는 선에서 
    max_value = 0 
    for j in range(1,i):
        if today ==0: # 오늘 진료를 안본다면 
            if j+ppl[j][0]<=i+1: # 오늘 날짜 이하 
                if max_value<dp[j]:
                    max_value = dp[j]
                    
                    #print('X j,ppl[j][0], i : ',j,ppl[j][0],i)
        else: #오늘 진료를 분다면 
            if j+ppl[j][0]<=i: # 오늘 날짜 안넘어오는 선에서 2+6<3
                if max_value<dp[j]:
                    max_value = dp[j]
                    #print('O j,ppl[j][0], i : ',j,ppl[j][0],i)
    

    #print(i,max_value,today)
    dp[i] = max_value + today # dp[1] 부터 dp[i-1] 중 최댓값. 이랑 현위치 더한다. 

print(max(dp))
#print(dp)
