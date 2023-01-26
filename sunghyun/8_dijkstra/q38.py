n = 6
input = [[],
         [5],
         [],
         [4],
         [2,6],
         [2,4],
         []]
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n + 1):
    dest = input[i]
    for d in dest:
        graph[i][d] = 1


for i in range(n+1):
    graph[i][i] = 0


for k in range (1, n+1):
    for a in range (1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# for i in range(1, n+1):
#     print(graph[i][1:])

result = 0
for a in range (1, n+1):
    count = 0
    for b in range(1, n+1):
        if graph[a][b] != INF or graph[b][a] != INF:
            count += 1
            # print(str(count) + " count up!")
        if count == n:
            result += 1
            #여기서 a값이 어떤 학생이 비교 가능한지. result는 그런 학생이 총 몇 명
print(result)