n = int(input())
work = [list(map(int, input().split())) for _ in range(n)]
d = [0] * (n+1)
answer = 0

for i in range(n-1, -1, -1):
  
  #초과하지 않는 날짜범위라면? ㄱㄱ
  if work[i][0] + i < n+1:
    #i일의 일당 + d[i날일의일양+i날], 답
    d[i] = max(work[i][1] + d[work[i][0] + i], answer)
    answer = d[i]
  else:
    d[i] = answer

print(answer)