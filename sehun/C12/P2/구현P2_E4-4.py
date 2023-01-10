#일반적으로 방향을 설정해서 이동하는 문제는 dx, dy라는 별도의 리스트를 만들어 방향을 정하는 것이 효과적이다.
n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1 #현재 좌표 방문처리

#전체 맵 정보를 입력받기
array = []
for i in range(n):
  array.append(list(map(int, input().split())))

#북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#왼쪽으로 회전
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

#시뮬레이션 시작
count = 1
turn_time = 0
while True:
  #왼쪽 회전
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  #회전 후 정면에 안가본칸 존재시 이동
  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  else:
    turn_time += 1
  
  #네 방향 모두 갈 수 없는 경우
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    #뒤로갈수 있으면 가기
    if array[nx][ny] == 0:
      x = nx
      y = ny
    #뒤가 바다로 막혀있는 경우
    else:
      break
    turn_time = 0

print(count)

