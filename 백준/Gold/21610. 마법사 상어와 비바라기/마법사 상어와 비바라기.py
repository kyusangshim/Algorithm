# 1. 입력 정의
N, M = map(int, input().split())

board = []
for i in range(N):
  board.append(list(map(int, input().split())))

move_info = []
for i in range(M):
  d, s = map(int, input().split())
  move_info.append((d, s))
    
    
# 2. 자료구조 정의
move_directions = [
    [],
    [0, -1],
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1]
]

# 구름 초기화
clouds = [
    (N-1, 0),
    (N-1, 1),
    (N-2, 0),
    (N-2, 1)
]


# 4. 함수 정의
def simulation(move, clouds):
  # 이동 정의
  d, s = move
  cur_dir = move_directions[d]

  # (1) 구름 이동
  for i in range(s):
    for j in range(len(clouds)):
      x, y = clouds[j]
      x += cur_dir[0]
      y += cur_dir[1]

      if x == -1: 
        x = N-1
      if x == N: 
        x = 0
      if y == -1: 
        y = N-1
      if y == N: 
        y = 0

      clouds[j] = (x, y)

  # (2) 양 증가
  for r, c in clouds:
    board[r][c] += 1

  # (3) 물복사 버그
  for r, c in clouds:
    count = 0
    for number in [2, 4, 6, 8]:
      nr, nc = r, c
      nr += move_directions[number][0]
      nc += move_directions[number][1]

      if 0 <= nr < N and 0 <= nc < N:
        if 0 < board[nr][nc]:
          count += 1
    board[r][c] += count

  # (4) 2 이상인 모든 칸에 구름 생성 
  new_clouds = []
  for i in range(N):
    for j in range(N):
      if (i, j) not in clouds:
        if 2 <= board[i][j]:
          new_clouds.append((i, j))
          board[i][j] -= 2

  clouds = new_clouds
  return clouds
  
    
    
# 3. 메인 로직 정의
for move in move_info:
  clouds = simulation(move, clouds)


# 5. 출력
result = 0
for row in board:
  result += sum(row)

print(result)
