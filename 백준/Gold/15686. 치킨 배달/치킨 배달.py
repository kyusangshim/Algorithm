N, M = map(int, input().split())

house = []
chicken = []

for r in range(N):
  row = list(map(int, input().split()))

  for c in range(N):
    if row[c] == 1:
      house.append((r, c))

    elif row[c] == 2:
      chicken.append((r, c))
    
min_city_chicken_distance = float('inf')
selected_chicken = []

def calculate_distance():
  total_distance = 0
  for h in house:
    min_dist = float('inf')

    for c in selected_chicken:
      dist = abs(h[0] - c[0]) + abs(h[1] - c[1])
      min_dist = min(min_dist, dist)

    total_distance += min_dist
  
  return total_distance


def dfs(start, count):
  global min_city_chicken_distance

  if count == M:
    min_city_chicken_distance = min(min_city_chicken_distance, calculate_distance())
    return

  for i in range(start, len(chicken)):
    selected_chicken.append(chicken[i])

    dfs(i+1, count+1)

    selected_chicken.pop()


dfs(0, 0)

print(min_city_chicken_distance)