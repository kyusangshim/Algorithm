from collections import deque

N = int(input())
board = []
shark_x, shark_y = 0, 0

for i in range(N):
  row = list(map(int, input().split()))
  board.append(row)

  for j in range(N):
    if row[j] == 9:
      shark_x, shark_y = i, j
      board[i][j] = 0
        
shark_size = 2
eat_count = 0
time = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(start_x, start_y, size):
  dist = [[-1] * N for _ in range(N)]
  queue = deque([(start_x, start_y)])
  dist[start_x][start_y] = 0

  temp_fish = []

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < N:
        if dist[nx][ny] == -1 and board[nx][ny] <= size:
          dist[nx][ny] = dist[x][y] + 1
          queue.append((nx, ny))

          if 0 < board[nx][ny] < size:
            temp_fish.append((dist[nx][ny], nx, ny))
  
  temp_fish.sort(key=lambda x: (x[0], x[1], x[2]))

  return temp_fish

while True:
  fish_list = bfs(shark_x, shark_y, shark_size)

  if len(fish_list) == 0:
    break

  next_dist, next_x, next_y = fish_list[0]

  time += next_dist
  board[next_x][next_y] = 0
  shark_x, shark_y = next_x, next_y
  eat_count += 1

  if eat_count == shark_size:
    shark_size += 1
    eat_count = 0

print(time)
