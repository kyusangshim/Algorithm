# 0. 필요한 라이브러리 정의
from collections import deque

# 1. 입력 정의
T = int(input())

all_cases = []
for i in range(T):
  M, N, K = map(int, input().split())
  all_cases.append([M, N, K])
  temp = []
  for _ in range(K):
    X, Y = map(int, input().split())
    temp.append((X, Y))

  all_cases[i].append(temp)

# 2. 자료구조 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 3. 메인 로직
def bfs(M, N, worms):
  # 방문여부 및 존재여부
  visited = [[False] * N for _ in range(M)]
  existed = set(worms)

  # 큐, count 변수 정의
  queue = deque()
  count = 0

  # 순회문
  for r, c in worms:
    if not visited[r][c]:
      queue.append((r, c))
      visited[r][c] = True

      while queue:
        x, y = queue.popleft()

        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]

          if 0 <= nx < M and 0 <= ny < N:
            if (nx, ny) in existed and not visited[nx][ny]:
              queue.append((nx, ny))
              visited[nx][ny] = True

      count += 1

  return count


# 5. 코드 실행
for i in range(len(all_cases)):
  M, N = all_cases[i][0], all_cases[i][1]
  worms = all_cases[i][3]
  print(bfs(M, N, worms))