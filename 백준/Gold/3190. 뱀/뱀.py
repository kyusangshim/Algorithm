from collections import deque

# 1. 입력 받기 및 자료구조 정의
N = int(input())

# board 정의 (보드판)
board = [[0]*(N+2) for _ in range(N+2)]

# 보드판 채우기
for i in range(N+2):
  board[0][i] = 1
  board[i][0] = 1
  board[i][-1] = 1
  board[-1][i] = 1

K = int(input())

for _ in range(K):
  x, y = map(int, input().split())
  board[x][y] = 2

L = int(input())
snake_dir = deque()
for _ in range(L):
  X, C = input().split()
  snake_dir.append([int(X), C])
    
    
# 이동 벡터
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 방향, 시간 등 변수 정의
dir = 1
T = 0
x, y = 1, 1
board[x][y] = 3
tail = deque([(x, y)])
bumped = False



# 2. 메인로직
while not bumped:
  # 다음 방향 찾기
  if snake_dir:
    X, C = snake_dir.popleft()

    # 앞으로 이동
    while X != T:
      # 시간 증가
      T += 1

      # 앞으로 이동
      x += dx[dir]
      y += dy[dir]

      if 0 <= x < N+2 and 0 <= y < N+2:
        if board[x][y] == 1 or board[x][y] == 3:
          bumped = True
          break

        elif board[x][y] == 2:
          board[x][y] = 3
          tail.append((x, y))

        else:
          board[x][y] = 3
          tail.append((x, y))
          tail_x, tail_y = tail.popleft()
          board[tail_x][tail_y] = 0
    
    if not bumped:
      # 방향 전환
      if C == 'D':
        dir = (dir+1) % 4
      else:
        dir = (dir-1) % 4

  else:
    # 앞으로 이동
    while True:
      # 시간 증가
      T += 1

      # 앞으로 이동
      x += dx[dir]
      y += dy[dir]

      if 0 <= x < N+2 and 0 <= y < N+2:
        if board[x][y] == 1 or board[x][y] == 3:
          bumped = True
          break

        elif board[x][y] == 2:
          board[x][y] = 3
          tail.append((x, y))

        else:
          board[x][y] = 3
          tail.append((x, y))
          tail_x, tail_y = tail.popleft()
          board[tail_x][tail_y] = 0
            
            
print(T)
