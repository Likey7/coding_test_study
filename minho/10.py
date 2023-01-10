# NxN, MxM 정사각
# 열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수
# 0은 홈 1은 돌기

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
checkLock = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def rotated(a):
  n = len(a)
  m = len(a[0])
  
  result = [[0]* n for _ in range(m)]

  for i in range(n):
    for j in range(m):
      result[j][n-i-1] = a[i][j]
  return result

# 한번에 이동하는거인듯 key가 그냥 통이니까
lockLen = len(lock)
keyLen = len(key)

check = True

for _ in range(4):

    # 돌리는 중간에 한칸씩 이동해 봐야함
    key = rotated(key)
    print(key)
    print(lock)

    for o in range(lockLen):
        for p in range(lockLen):
            for i in range(keyLen):
                for j in range(keyLen):
                    
                    if o+i < len(str(keyLen)) | p+j < len(str(keyLen)):
                        if  lock[o][p] + key[o+i][p+j] != 1:
                            check = False
                            continue
                        else:
                            check = True
                if check == False:
                    break
            if check == False:
                break
        if check == False:
                break
    

lastStr = ''
if check == True:
    lastStr = 'true'
else:
    lastStr = 'false'            
print(lastStr)
