N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visit = [0] * (N+1)
visit[1] = 1

dfs_result = []

def dfs(start):
  if start != 1:
    dfs_result.append(start)

  for next in graph[start]:
    if not visit[next]:
      visit[next] = 1
      dfs(next)

dfs(1)
print(len(dfs_result))