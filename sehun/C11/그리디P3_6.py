def solution(food_times, k):
    answer = 0
    i = 0
    while True:
        #남은 시간이 없다면 종료
        if 0 == k:
            break

        #음식이 있다면 섭취후 시간1빼기    
        if food_times[i] != 0:
            food_times[i] -= 1
            k -= 1
        
        #음식의 인덱스 증가 코드
        i += 1
        if len(food_times) <= i:
            i = 0
 
    #남은 음식이 없을경우 -1반환        
    if sum(food_times) == 0:
      answer = -1
    #먹어야할 음식의 번호 저장
    else:
      answer = i+1
    
    return answer


food_times = list(map(int, input().split()))
k = int(input())

print(solution(food_times, k))