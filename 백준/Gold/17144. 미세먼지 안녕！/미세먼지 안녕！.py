R, C, T = map(int, input().split())

cleaner_idx = []
board = []

for i in range(R):
  row = list(map(int, input().split()))
  board.append(row)

  if row[0] == -1:
    if not cleaner_idx:
      cleaner_idx.append((i, 0))
      cleaner_idx.append((i+1, 0))
        
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def diffusion(board):
  diffused_board = [row[:] for row in board]

  for i in range(R):
    for j in range(C):
      # 미세먼지가 있는 경우
      if board[i][j] > 0:
        # 우선, 확산되는 양 구하기 
        val = board[i][j] // 5

        # 몇가지 방향으로 확산되는지 구하고 확산시키기
        count = 0
        for k in range(4):
          ni = i + di[k]
          nj = j + dj[k]

          if 0 <= ni < R and 0 <= nj < C:
            if diffused_board[ni][nj] != -1:
              diffused_board[ni][nj] += val
              count += 1

        # 확산한만큼 본인 양 줄이기
        diffused_board[i][j] -= (val * count)

  return diffused_board

def clean(board):
    top = cleaner_idx[0][0]
    bottom = cleaner_idx[1][0]

    for i in range(top - 1, 0, -1):
        board[i][0] = board[i-1][0]
        
    for i in range(C - 1):
        board[0][i] = board[0][i+1]
        
    for i in range(top):
        board[i][C-1] = board[i+1][C-1]
        
    for i in range(C - 1, 1, -1):
        board[top][i] = board[top][i-1]
        
    board[top][1] = 0


    for i in range(bottom + 1, R - 1):
        board[i][0] = board[i+1][0]
        
    for i in range(C - 1):
        board[R-1][i] = board[R-1][i+1]
        
    for i in range(R - 1, bottom, -1):
        board[i][C-1] = board[i-1][C-1]
        
    for i in range(C - 1, 1, -1):
        board[bottom][i] = board[bottom][i-1]
        
    board[bottom][1] = 0
    
    return board


# 메인 로직
# T만큼 순회
while T:
  # 미세먼지 확산
  board = diffusion(board)

  # 공기청정기 작동
  board = clean(board)

  # 1초 감소
  T -= 1
    
total = 0
for i in range(R):
  for j in range(C):
    total += board[i][j]
    
print(total+2)

