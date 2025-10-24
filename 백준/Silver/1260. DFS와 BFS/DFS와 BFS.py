from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, len(graph)):
  graph[i].sort()

def dfs(v):
  visited_dfs[v] = True
  dfs_result.append(v)

  for next_v in graph[v]:
    if not visited_dfs[next_v]:
      dfs(next_v)

def bfs(v):
  queue = deque([v])
  visited_bfs[v] = True
  
  while queue:
    v = queue.popleft()
    bfs_result.append(v)

    for next_v in graph[v]:
      if not visited_bfs[next_v]:
        visited_bfs[next_v] = True
        queue.append(next_v)


visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

dfs_result = []
bfs_result = []


dfs(V)
bfs(V)

print(" ".join(map(str, dfs_result)))    
print(" ".join(map(str, bfs_result)))  