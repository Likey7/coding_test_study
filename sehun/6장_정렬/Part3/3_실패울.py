def solution(n, stages):
    answer = [0  for _ in range(n+1)]
    stages.sort()
    temp = []
    
    for i in range(len(stages)):
      for idx in range(stages[i]):
        answer[idx] +=1

    for i in range(1,len(answer)):
      temp.append([i, (answer[i-1]-answer[i]) / answer[i]])

    temp.sort(key = lambda x:(-float(x[1])) )
    
    abc = [temp[i][0] for i in range(len(temp))]
    return abc





n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(n, stages))