# original_food_times = food_times

# def solution(food_times, k):
    

#     original_food_times = food_times
#     cycle = k // len(food_times)
#     min_food = min(food_times)
#     answer = 0

#     if cycle < min_food:
#         if len(food_times) == 0:
#             answer = -1

#         original_food_times.sort(reverse = True)
#         answer = original_food_times[k+1]
#         return answer


#     else:
#         k -= cycle * len(food_times)
#         for food in range(len(food_times)):
#             food_times[food] = food_times[food] - min_food
#             food_times = list(filter(lambda x: x != 0, food_times))

#             return solution(food_times, k)





def solution(food_times, k):
    print(k)
    if not food_times:
        return -1
    
    cycle = k // len(food_times)
    min_food = min(food_times)
    time = 0
    for i in range(len(original_food_times)):
        time += original_food_times[i]


    if k > time:
        return -1

    if cycle >= min_food:
        print("cycle: " + str(cycle))
        k -= cycle * min_food
        food_times = [ft - min_food for ft in food_times]
        food_times = list(filter(lambda x: x != 0, food_times))
        print(food_times)
        print(k)
        return solution(food_times, k)
    
    else:
        print("k is " + str(k))
        sorted_food_times = sorted(original_food_times, reverse=True)
        index = k % cycle
        print(sorted_food_times[index])
        return original_food_times.index(sorted_food_times[index]) + 1

food_times = [8,6,4,24,18]
original_food_times = food_times
print(solution(food_times, 35))