import heapq

heap = []
N = int(input())

for _ in range(N):
  heapq.heappush(heap, int(input()))

total_cost = 0

while heap:
  if len(heap) == 1:
    break
    
  new_num = heapq.heappop(heap) + heapq.heappop(heap)
  total_cost += new_num

  heapq.heappush(heap, new_num)


print(total_cost)