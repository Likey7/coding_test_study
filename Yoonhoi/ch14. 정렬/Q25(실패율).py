def solution(N, stages):
    answer = []
    numbers = [[x,0,0,0] for x in range(N+1)]
    numbers[0][2] = len(stages)
    for i in stages:
        if i<=N:
            numbers[i][1]+=1
    
    for i in range(N):
        numbers[i+1][2] = numbers[i][2]-numbers[i][1]
        if numbers[i+1][2] ==0: # 0으로 나눌 때의 케이스 분리 
            numbers[i+1][3] =0
        else:
            numbers[i+1][3] = numbers[i+1][1]/numbers[i+1][2] # 실패율인 경우 
    
    return  [x[0] for x in sorted(numbers[1:],key = lambda x : x[3], reverse = True )]

solution(5,[2, 1, 2, 6, 2, 4, 3, 3])
