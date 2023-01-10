# 내 풀이
def solution(s):
    result = 1000
    for i in range(1, (len(s) // 2) + 1):
        start = s[:i]

        now = ''
        cnt = 1
        for j in range(i, len(s), i):
            if s[j: j + i] == start:
                cnt += 1
            else:
                if cnt == 1:
                    now += start
                else:
                    now += str(cnt) + start

                cnt = 1
                start = s[j: j + i]

        if cnt == 1:
            now += start
        else:
            now += str(cnt) + start

        result = min(result, len(now))

    return result if result != 1000 else 1