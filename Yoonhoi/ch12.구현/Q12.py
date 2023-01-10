
# 1. 바닥인가
# 2. 아래가 기둥인가
# 3. 왼쪽이 보인가
# + array 를벗어나지 않아야 함!
def col_check(arr, x, y):
    action=False
    if (y==0) :
        action=True
    elif (arr[x][y-1] ==0) : # y=!0 이니까 인덱스 벗어나지 않음
        action=True
    elif x>0 and (arr[x-1][y] ==1):
        action = True
    return action



# 1. 기둥 한족 끝/ 아래가 기둥
# 2. 왼쪽이 보 + 오른쪽이 보
# 3. 왼쪽이 보 + 오른쪽 아래가 기둥
def row_check(arr,x,y):
    
    action=False
    if y>0 and (arr[x][y-1]==0) :
        action=True
    elif (x>0 and x<(len(arr)-1)) and (arr[x-1][y]==1 and arr[x+1][y]==1) :
        action=True
    elif arr[x+1][y-1]==0 :
        action=True
    return action
    
    


def solution(n, build_frame):
    answer = []
    arr = [[-1 for col in range(n+1)] for row in range(n+1)]
    
    for frame in build_frame:
        # frame [x,y,a,b]
        x,y,a,b = frame[0], frame[1], frame[2], frame[3]
        flag=False
        
        
        if b==1: # 기둥/보 설치
            # 기둥 설치 가능할 때 
            if a==0:
                if col_check(arr,x,y):
                    flag=True
                    
            # 보 설치 가능할 때 
            else : # a==1
                if row_check(arr,x,y):
                    flag=True
                    
            if flag:
                arr[x][y] = a
                answer.append([x,y,a])
            
            # 가능하지 않은 경우는 무시된다. 
        else: # 기둥 보 삭제 
            # 기둥 삭제
            temp = arr[x][y]
            arr[x][y] = -1
            
            if a ==0:
                # 왼쪽위 보 / 위 기둥 / 위 보  존재 가능한지 확인 
                if row_check(arr,x-1,y+1) and col_check(arr,x, y+1) and row_check(arr,x,y+1):
                    flag = True
                
            # 보 삭제 
            else: # a==1
                # 왼쪽 보 / 오른쪽 보  /오른쪽 기둥 
                if row_check(arr,x-1,y) and row_check(arr,x+1,y) and col_check(arr,x+1,y):
                    flag = True
                    
            if flag :
                del answer[answer.index([x,y,a])]
            else:
                arr[x][y]=temp
            
    answer.sort()
    return answer