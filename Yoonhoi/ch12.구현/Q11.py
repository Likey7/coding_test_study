# 입력 받는 부분
N = int(input())
K = int(input())
K_list = []
for _ in range(K):
    K_list.append(list(map(int,input().split())))
L = int(input())
time_list = []
turn_list = []
for _ in range(L):
    time,turn = input().split()
    time_list.append(int(time))
    turn_list.append(turn)
'''
print(N)
print(K)
print(K_list)
print(L)
print(time_list)
print(turn_list)
'''
############################################
    
# 2차원 배열 초기화
arr = [[1 for col in range(N+2)] for row in range(N+2)]

# 패딩 벽 0
for i in range(N+2):
    for j in range(N+2):
        if (i in [0,N+1] )or (j in [0,N+1]) : 
            arr[i][j]=0

# 사과 3 -> 
for (x,y) in K_list:
    arr[x][y] = 3
 

# 뱀의 몸이 차지하고 있는 곳  = 2   
arr[1][1] = 2

now = 0

# head, tail 을 리스로 만들면 수정했을 때 기존에 snake에 올린 리스트가 수정되어서 기록이 안됨
#head = [1,1]
head_x=1
head_y=1
#tail = [1,1]
tail_x=1
tail_y=1
side = 0 # 0 right, 90 up, 180 left, 270 down
is_apple = 0 # head 가 위치한 곳에 사과가 있으면 1 없으면 0
#length = 1

snake_queue = []
snake_queue.append([head_x,head_y])

timing = time_list[0]
time_list = time_list[1:]
timing_side = turn_list[0]
turn_list = turn_list[1:]
'''
for row in arr:
    print(row)
''' 
###############################################

while True :
    # 시작하면서 시간 증가!
    now +=1
    # print('now')
    # print(now)
    
    # 방향에 따라 헤드 위치 이동 
    if side==0: 
        head_y = head_y+1
    elif side ==90:
        head_x = head_x-1
    elif side == 180 : 
        head_y = head_y-1
    elif side ==270 : 
        head_x = head_x+1
    
    # print('head')
    # print([head_x,head_y])
    
    # 스네이크 큐에 헤드 올림
    snake_queue.append([head_x,head_y])
    
    # head 가 이동한 위치가 벽인가? 몸인가? 확인 
    if arr[head_x][head_y]==0 or arr[head_x][head_y]==2:
        break
        
    # head 가 이동한 위치에 사과가 있는지 확인 
    if arr[head_x][head_y]==3: # 사과가 있으면 
        is_apple =1
        arr[head_x][head_y]=2 # 사과 먹음 -> 몸이 위에 있음
        # length+=1
        # 꼬리 위치 그대로 (snake 변동 없음 )
        
    else : # 사과가 없으면 
        is_apple = 0
        arr[head_x][head_y]=2 # 사과는 안먹었지만 땅을 먹음
        
        tail_x, tail_y= snake_queue[0][0], snake_queue[0][1] # 꼬리 리스트에서 지움
        snake_queue = snake_queue[1:]
        
        arr[tail_x][tail_y]=1 # 땅 원래대로 1로 변경 
        

    # print('snake_queue')
    # print(snake_queue)
    
    # 마지막에 초가 끝난 후 확인해야 할 것은 방향 전환 time 이 되었는가 이다
    if now == timing:
        # timing 이라면, 헤드 방향에 따라 전환
        if timing_side=='L':
            side = (side+90)%360            
        else :#timing_side =='D'
            side = (side+270)%360
            
           
        if len(time_list):
            timing = time_list[0]
            time_list = time_list[1:]
            timing_side = turn_list[0]
            turn_list = turn_list[1:]
        else:
            timing = -1
            timing_side = 0
    
    # print('timing')
    # print(timing)
    
    # print('*********************************')

print(now)