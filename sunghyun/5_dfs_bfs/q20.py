import itertools
from collections import deque
import copy

board = [['X', 'S', 'X', 'X', 'T'],
         ['T', 'X', 'S', 'X', 'X'],
         ['X', 'X', 'X', 'X', 'X'],
         ['X', 'T', 'X', 'X', 'X'],
         ['X', 'X', 'T', 'X', 'X']]
n = len(board)
teacher = list()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
succeed = False

for i in range(n):
    for j in range(n):
        if board[i][j] == 'T':
            teacher.append((i,j))



def deploy_obstruct(count):
    if count == 3:

        print(board)
        print("count 3")
        print("this is check " + str(check()))
        check()
        if succeed:
            return "YES"
        else: 

            for i in range(n):
                for j in range(n):
                    print("this is count " + str(count))

                    if board[i][j] =='X':
                        board[i][j] = 'O'
                        count += 1
                        deploy_obstruct(count)
                        board[i][j] = 'X'
                        count -= 1
    return "NO"
                


def check():
    global succeed
    print(board)
    for t in teacher:
        print("this is t " + str(t))
        if not check_student(t): #학생 찾음 -> 못 피함
            succeed = False
        if check_student(t):
            print("못 찾음!")
            print(board)
            succeed = True
    return succeed

def check_student(teacher):
    print("check student" + str(teacher))
    for i in range(len(dx)):
        for j in range(1, n+1):
            nx = teacher[0] + j * dx[i]
            ny = teacher[1] + j * dy[i]
            print(str(nx) +"  "+ str(ny))
            if nx >= n or nx < 0 or ny >= n or ny < 0:
                print("out of the board")
                break
            if board[nx][ny] == 'S':
                print("잡았다 요놈")
                return True
            if board[nx][ny] == 'O':
                print("벽에 부딪")
                break
            if board[nx][ny] == 'X':
                continue
    print("못 참음 ㄷㄷ;;" + str(board))
    return False #not found
print(teacher)
print(deploy_obstruct(0))
# print(check())