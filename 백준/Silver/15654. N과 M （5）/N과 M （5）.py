N, M = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort()

visited = [False] * (N+1)
stack = []

def dfs():
  if len(stack) == M:
    print(' '.join(map(str, stack)))
    return

  for i in range(N):
    if not visited[i]:
      visited[i] = True
      stack.append(numbers[i])

      dfs()

      stack.pop()
      visited[i] = False
    
dfs()