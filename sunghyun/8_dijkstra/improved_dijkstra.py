import heapq

graph = [[],
         [(2,5), (4,3), (3,1)],
         [(4,1), (5,1)],
         [(2,2), (4,2)],
         [(5,4)],
         []]

INF = int(1e9)

dist = [INF] *  len(graph)

heap = []

def dijkstra(start):
    heapq.heappush(heap, (0, start)) 

    while heap:
        print(heap)
        d, now = heapq.heappop(heap)
        dist[start] = 0
        if dist[now] < d:
            continue
        for node, dst  in graph[now]:
            cost = dst + d 
            print("cost is " + str(cost))
            print(dist)
            if cost < dist[node]:
                dist[node] = cost
                heapq.heappush(heap, (cost, node))
                print("this is pushed into the heap")
                print(heap)

dijkstra(1)

print(dist)