from collections import deque

n = int(input())
data_map = []
teacher = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(n):
  data_map.append(list(input().split()))
  teacher += data_map[i].count('T')


def search(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    while 0 <= nx < n and 0 <= ny < n and data_map[nx][ny] != 'O':
      if data_map[nx][ny] == 'S':
        #감시가능함
        return True
      else:
        nx += dx[i]
        ny += dy[i]

  return False    
    
 
def dfs(count):
  #만약 벽이 3개 세워진다면 선생님 감시범위 탐색시작
  if count == 3:
    teacher_f = 0

    for i in range(n):
      for j in range(n):
        if data_map[i][j] == 'T':
          if not search(i,j):
            teacher_f += 1
    if teacher_f == teacher:
      answer = True
    return

  for i in range(n):
    for j in range(n):
      if data_map[i][j] == 'X':
        data_map[i][j] = 'O'
        count += 1
        dfs(count)
        count -= 1
        data_map[i][j] = 'X'



answer = False
dfs(0)

if answer == True:
  print("YES")
else:
  print("NO")