# 답지 힙큐사용
# heapq : priority queue 를 구현한 것. 
# 정렬 된 형태로 저장이 된다. 
# 구조는 같으나 이 자료구조를 사용하는 것만으로도 문제 해결 ㅋㅋ

# 기존 코드보고 수정
import heapq
import sys
f = sys.stdin.readline
n = int(f())

#heap = [int(f()) for _ in range(n)]
#heapq.heapify(heap) 
heap = []
for _ in range(n):
    val = int(f())
    heapq.heappush(heap,val)

answer = 0

while len(heap)!=1:
    val = (heapq.heappop(heap) +heapq.heappop(heap))
    heapq.heappush(heap,val)
    answer+=val
   
print(answer)