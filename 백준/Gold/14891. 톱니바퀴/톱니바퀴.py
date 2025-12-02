# 1. 입력 받기 및 자료구조 정의
from collections import deque

cog_wheel = [[]]

# queue 이용 -> 1~4번 모두 queue에 삽입
for i in range(4):
  cog_wheel.append(deque(map(int, input().strip())))

# 또한, 회전 정보도 queue에 삽입
k = int(input())

rotate_queue = deque()
for _ in range(k):
  row = list(map(int, input().split()))
  rotate_queue.append(row)
    

# 2. 회전 로직
def rotate_cog_wheel(num, direction):
  # 현재 왼쪽값, 오른쪽 값 저장 (회전 전)
  left, right = cog_wheel[num][-2], cog_wheel[num][2]
  dir_left, dir_right = direction, direction

  # 자기 자신 회전
  cog_wheel[num].rotate(direction)

  # 왼쪽 회전
  for i in range(num-1, 0, -1):
    # 회전하지 않으면 나머지 왼쪽도 회전 X
    if left == cog_wheel[i][2]:
      break
    else:
      left = cog_wheel[i][-2]
      cog_wheel[i].rotate(-dir_left)
      dir_left = -dir_left

  # 오른쪽 회전
  for i in range(num+1, len(cog_wheel)):
    # 회전하지 않으면 나머지 오른쪽도 회전 X
    if right == cog_wheel[i][-2]:
      break
    else:
      right = cog_wheel[i][2]
      cog_wheel[i].rotate(-dir_right)
      dir_right = -dir_right
        
        
        
# 3. 메인 로직
# queue가 빌때까지 회전
while rotate_queue:
  # queue에서 하나 꺼내기
  num, direction = rotate_queue.popleft()

  # 회전시키기
  rotate_cog_wheel(num, direction)
    
    
# total 구하기
total = 0

for i in range(1, 5):
  if cog_wheel[i][0] == 0:
    continue
  else:
    if i == 1:
      total += 1
    elif i == 2:
      total += 2
    elif i == 3:
      total += 4
    else:
      total += 8
    
    
print(total)