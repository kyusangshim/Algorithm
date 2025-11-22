N, M = map(int, input().split())

stack = []
visited = [False] * (N+1)

def dfs(threshold):
  if len(stack) == M:
    print(' '.join(map(str, stack)))
    return

  for i in range(1, N+1):
    if i < threshold:
      continue
    if not visited[i]:
      visited[i] = True
      stack.append(i)

      dfs(i+1)

      stack.pop()
      visited[i] = False
     
dfs(1)