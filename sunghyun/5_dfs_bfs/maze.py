from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

test = [[1,1,0],
        [0,1,0],
        [0,1,1]]

def maze_escape(maze):
    queue = deque()
    queue.append((1,1))
    destination = [len(maze) - 1, len(maze[0]) - 1]
    # print(queue)

    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx>=len(maze) or ny>=len(maze[0]) or maze[nx][ny] != 1:
                continue

            if maze[nx][ny] == 1:
                queue.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1
            
        print(queue)

    return maze[len(maze) -1][len(maze[0]) - 1]



print(maze_escape(test))