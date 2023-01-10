import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    previous = 0

    while q:
        nums, idx = q[0]
        now = (nums - previous) * len(q)

        if now < k:
            k -= now

        else:
            q.sort(key=lambda x: x[1])
            return q[(k % len(q))][1]

        previous = heapq.heappop(q)[0]