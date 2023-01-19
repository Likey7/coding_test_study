import heapq

n = int(input())

heap =[]
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

total = 0

while len(heap) <= 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    sum = one + two

    total += sum
    heapq.heappush(heap, sum)

print(total)