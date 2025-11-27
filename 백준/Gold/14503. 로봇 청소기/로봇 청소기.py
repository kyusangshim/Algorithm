# 1. 입력 및 자료구조 정리

# N, M 입력 받기
N, M = map(int, input().split())

# 현재 위치 및 방향(d) 입력 받기
r, c, d = map(int, input().split())

# 로봇 청소기가 다닐 맵(board) 입력 받기
board = []
for i in range(N):
  row = list(map(int, input().split()))
  board.append(row)

# 이동하는 dx, dy 벡터 정의
vector_dict = {
    0: {
        'dx': [-1],
        'dy': [0],
        'dx_back': [1],
        'dy_back': [0]
    },
    1: {
        'dx': [0],
        'dy': [1],
        'dx_back': [0],
        'dy_back': [-1]
    },
    2: {
        'dx': [1],
        'dy': [0],
        'dx_back': [-1],
        'dy_back': [0]
    },
    3: {
        'dx': [0],
        'dy': [-1],
        'dx_back': [0],
        'dy_back': [1]
    },
}


# 청소할 구역 세는 count 변수 선언
count = 0

# 현재 청소한 칸인지 정의하는 visit 배열 정의
visited = [[False] * M for _ in range(N)]


def scan(r, c, d):
  next_d = d
  for i in range(4):
    if next_d == 0:
      next_d = 3
    else:
      next_d -= 1

    # 앞, 반시계 ..., 총 4번 확인
    next_r = r + vector_dict[next_d]['dx'][0]
    next_c = c + vector_dict[next_d]['dy'][0]

    if not visited[next_r][next_c] and board[next_r][next_c] == 0:
      return True, next_d

  back_r = r + vector_dict[d]['dx_back'][0]
  back_c = c + vector_dict[d]['dy_back'][0]

  if board[back_r][back_c] == 0:
    return True, -1

  return False, -1


# 2. 핵심 로직의 흐름 정리

# 이동 로직 
def dfs(r, c, d):
  global count

  # 방문 체크 및 청소
  if not visited[r][c] and board[r][c] == 0:
    visited[r][c] = True
    count += 1

  # 종결문 -> 더이상 갈 곳이 없으면 종결
  res, next_d = scan(r, c, d)
  if not res:
    return 

  # 순회 코드
  if next_d != -1:
    next_r = r + vector_dict[next_d]['dx'][0]
    next_c = c + vector_dict[next_d]['dy'][0]

    dfs(next_r, next_c, next_d)

  else:
    next_r = r + vector_dict[d]['dx_back'][0]
    next_c = c + vector_dict[d]['dy_back'][0]
    
    dfs(next_r, next_c, d)
    
    
    
# 로직 실행
dfs(r, c, d)

# count 출력
print(count)


