N = int(input())

graph = []
student = []
for i in range(N):
    new = input().split()
    graph.append(new)

    for j in range(len(new)):
        if new[j] == 'S':
            student.append((i, j))

result = 0
while student:
    x, y = student.pop()

    for k in range(len(graph[x])):
        if graph[x][k] == 'T':
            result += 1
            graph[x][k] = 'X'

    for k in range(len(graph)):
        if graph[k][y] == 'T':
            result += 1
            graph[k][y] = 'X'

print(result)