from collections import deque

data = [[],
        [2, 3], #1에서 갈 수 있는 곳
        [3, 4], #2에서 갈 수 있는 곳 
        [],
        []]

distance = [-1] * (len(data))

def find_city(n,m,k,x, data, distance):

    queue = deque()
    queue.append(x)
    print(queue)
    distance[x] = 0

    while queue:
        now = queue.popleft() 

        for next in data[now]:
            if distance[next] == -1:
                distance[next] = distance[now] + 1
                queue.append(next)
            

        print(queue)
        print(distance)

    for d in range(len(distance)):
        if distance[d] == k:
            print(distance)
            print("City "+ str(d) + " is reached")

find_city(4, 4, 2, 1, data, distance)





