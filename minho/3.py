# 0, 1 문자열 S 모든 숫자를 같게 만들기 하나 이상의 숫자를 뒤집음 1을 0, 0을 1 최소값

S = input()

check_z = 0
check_o = 0

for i in range(0, len(S)):
    if i == 0:
        if S[i] == '0':
            check_z += 1
        else:
            check_o += 1
            
    if i < len(S)-1:
        if S[i+1] != S[i]: # 다를때만 체크

            if S[i+1] == '0':
                check_z += 1
            else:
                check_o += 1

print(min(check_z, check_o))