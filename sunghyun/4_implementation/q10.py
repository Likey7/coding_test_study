def rotate_a_matrix_by_90_degree(a):
    n = len(a) #행 길이
    m = len(a[0]) #열 길이
    result = [[0] * n for _ in range(m)] #결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

def check():

def solution(key, lock):
    n = len(lock)
    m = len(key)
    board_len = n + 2*m - 2
    board = [[0] * board_len for _ in range(board_len)]

    for i in range