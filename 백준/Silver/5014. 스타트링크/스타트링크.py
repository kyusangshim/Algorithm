from collections import deque

F, S, G, U, D = map(int, input().split())

visit = [0] * (F+1)
count = 0

def bfs(start):
  # 큐 설정
  queue = deque()
  queue.append((start, 0))

  # 방문 처리
  visit[start] = 1

  # 레벨 순회
  while queue:
    current, count = queue.popleft()

    # 종료 조건
    if current == G:
      return count

    for next in [current + U, current - D]:
      if 1 <= next <= F and not visit[next]:
        # 방문 처리
        visit[next] = 1
        queue.append((next, count + 1))

  return "use the stairs"

print(bfs(S))