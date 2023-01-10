def rotate90(key):
    m = len(key[0])
    rot_key = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            rot_key[j][m-i-1] = key[i][j]
    return rot_key

def try_unlock(key, lock, m, n, j, k):
    lock_c = [[0 for a in range(n*3)] for b in range(n*3)]
    for i in range (j, j+m):
        for h in range(k, k+m):
            lock_c[i][h] += key[i-j][h-k]
    for i in range(n, n*2):
        for h in range(n, n*2):
            if lock_c[i][h] != 1:
                return False
    return True
    
def solution(key, lock):
    answer = False
    m,n = len(key), len(lock)
    lock_ex = [[0 for i in range(n*3)] for j in range(n*3)]
    
    for  i in range(n, n*2):
        for j in range(n, n*2):
            lock_ex[i][j] = lock[i-n][j-m]
            
    for i in range(4): #키 찍어보고 안되면 90도 회전 4회반복(360도)
        key = rotate90(key)
        for j in range(n-m+1, n*2):
            for k in range(n-m+1, n*2):
                answer = try_unlock(key, lock_ex, m, n, j, k)
                if answer == True:
                    return answer
    return answer