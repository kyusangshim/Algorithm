N, M = map(int, input().split())
x = [0] * M

def isSafe(k, n):
  for i in range(k):
    if x[i] == str(n):
      return False
  return True

def back_tracking(k):
  if k > M-1:
    print(' '.join(x))
    return

  for n in range(1, N+1):
    if isSafe(k, n):
      x[k] = str(n)
      back_tracking(k+1)
        
back_tracking(0)
