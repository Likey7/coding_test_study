import heapq

INF = int(1e9)
n = 3

dist = [[INF] * n for _ in range(n) ]

map = [[5, 5, 4],
       [3, 9, 1],
       [3, 2, 7]]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dijkstra():
    heap = []
    heapq.heappush(heap, (map[0][0], (0, 0)))
    dist[0][0] = map[0][0]

    while heap:
        energy_use, (now_x, now_y) = heapq.heappop(heap)
        
        if dist[now_x][now_y] < energy_use:
            continue

        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]
            
            if next_x < 0 or next_x > 2 or next_y < 0 or next_y > 2:
                continue

            energy_sum = energy_use + map[next_x][next_y]
            # print(energy_sum)
            if energy_sum < dist[next_x][next_y]:
                dist[next_x][next_y] = energy_sum
                heapq.heappush(heap, (energy_sum, (next_x, next_y)))

dijkstra()
print(dist[n-1][n-1] )