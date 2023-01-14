from collections import deque

queue = deque()

queue.append(2)
queue.append(3)
queue.append(4)
head = queue.popleft()
print(head)
print(queue)

queue.append(7)
queue.append(8)
print(queue)

queue = deque([1,2,3,4])
print(queue)
print(type(queue))
print(queue[3])
