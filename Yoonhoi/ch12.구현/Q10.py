
def get_rotate_key(M,key):
    rotate_key = [[0]*M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            rotate_key[i][j] = key[M-1-j][i]
    
    return rotate_key

def initialize_pad_lock(lock,pad_size,N,M):
    pad_together = [[-1 for col in range(pad_size)] for row in range(pad_size)]
    for a in range(N):
        for b in range(N):
            pad_together[a+M-1][b+M-1] = lock[a][b]
    return pad_together

def solution(key, lock):
    M = len(key)
    N = len(lock)
    pad_size = N+2*(M-1)
    
    # key 정방향인 것을 순서대로 더한다.     # key 1234 존재    # 90 도 회전 
    key2 = get_rotate_key(M,key)
    key3 = get_rotate_key(M,key2)
    key4 = get_rotate_key(M,key3)
    
    # 전체 순회 
    # i,j 는 왼쪽 위 기준점 
    for i in range(N+M-1):
        for j in range(N+M-1):
            for test_key in [key,key2,key3,key4]:
                
                # pad together 초기화                 
                pad_together = initialize_pad_lock(lock,pad_size,N,M)
                
                # together =  lock + key 자물쇠 + 키 맞춰보기 
                for k in range(M):
                    for l in range(M):
                        pad_together[i+k][j+l] = pad_together[i+k][j+l] +test_key[k][l]
                # i, j 기준으로 key 를 한번 꽂아본 상태
                
                # 자물쇠 전체 탐색 하나라도 1이 아니면 답이 아님 
                answer= True
                for a in range(N):
                    for b in range(N):
                        if pad_together[a+M-1][b+M-1]!=1:
                            answer=False
                            break
                
                # lock_zero와 lock_one 을 모두 확인했는데도 flag == True 라면 return answer 
                if answer:
                    return answer
                    
        
    return answer