from collections import deque

F, S, G, U, D = map(int, input().split())

visit = [0] * (F+1)

def bfs(start):
  # 큐 선언
  queue = deque()
  queue.append((start, 0))
  visit[start] = 1

  # 반복 순회 
  while queue:
    stair, count = queue.popleft()

    if stair == G:
        return count
    
    for next in [stair+U, stair-D]:
      if 1 <= next <= F and visit[next] == 0:
        visit[next] = 1
        queue.append((next, count+1))
  
  return "use the stairs"


print(bfs(S))