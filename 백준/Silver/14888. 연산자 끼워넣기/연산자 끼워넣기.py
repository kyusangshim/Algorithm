N = int(input())

numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

stack = []
result = []
count = [0] * len(operators)

def initialize_prefix():
  value = 0
  if stack[0] == 'a':
    value = numbers[0] + numbers[1]
  elif stack[0] == 's':
    value = numbers[0] - numbers[1]
  elif stack[0] == 'm':
    value = numbers[0] * numbers[1]
  else:
    value = int(numbers[0] / numbers[1])

  return value

def calculate():
  prefix = []
  prefix.append(initialize_prefix())

  idx = 2
  while idx < len(numbers):
    if stack[idx-1] == 'a':
      prefix[0] += numbers[idx]
    elif stack[idx-1] == 's':
      prefix[0] -= numbers[idx]
    elif stack[idx-1] == 'm':
      prefix[0] *= numbers[idx]
    else:
      prefix[0] = int(prefix[0] / numbers[idx])

    idx += 1

  return prefix[0]

def dfs():
  if sum(count) == (N-1):
    result.append(calculate())
    return

  for i in range(len(operators)):
    if operators[i] > 0 and count[i] != operators[i]:
      count[i] += 1

      if i == 0:
        stack.append('a')
      elif i == 1:
        stack.append('s')
      elif i == 2:
        stack.append('m')
      else:
        stack.append('d')

      dfs()

      stack.pop()
      count[i] -= 1

    
dfs()
print(max(result))
print(min(result))