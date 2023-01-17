def solution(N, stages):
    answer = []
    total_user = len(stages) #전체 사람 수
    

    for i in range(1, N + 1):
        
        user = stages.count(i)
        passed_user = total_user

        if passed_user == 0:
            fail = 0
        else:
            fail = user / passed_user
        
        answer.append((i, fail))
        passed_user -= user

    answer = sorted(answer, key = lambda x: x[1], reverse = True)

    answer = [i[0] for i in answer]

    return answer




