N = int(input())

board = [[0] * (N) for _ in range(N)]

x = [0] * N
result = []

def canPlace(k, col):
  for i in range(k):
    if x[i] == col or abs(i-k) == abs(x[i]-col):
      return False
  return True


def NQueens(k):
  if k > N-1:
    result.append(x)
    return

  for col in range(N):
    if canPlace(k, col):
      x[k] = col
      NQueens(k+1)  
        
 
NQueens(0)
print(len(result))
