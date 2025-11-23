import copy

N, M = map(int, input().split())
board = []
cctv = [] 

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(M):
        if 1 <= row[j] <= 5:
            cctv.append((i, j, row[j]))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

mode = [
    [],
    [[0], [1], [2], [3]], 
    [[0, 2], [1, 3]],     
    [[0, 1], [1, 2], [2, 3], [3, 0]], 
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], 
    [[0, 1, 2, 3]]        
]

min_count = float('inf')

def simulation(directions):
    temp_board = copy.deepcopy(board)
    
    for i in range(len(cctv)):
        x, y, _ = cctv[i]
        cur_dirs = directions[i]
        
        for d in cur_dirs:
            nx, ny = x, y
            while True:
                nx += dx[d]
                ny += dy[d]
                
                if not (0 <= nx < N and 0 <= ny < M) or temp_board[nx][ny] == 6:
                    break
                
                if temp_board[nx][ny] == 0:
                    temp_board[nx][ny] = '#'
                    
    cnt = 0
    for row in temp_board:
        cnt += row.count(0)
    return cnt

def dfs(idx, directions):
    global min_count
    
    if idx == len(cctv):
        min_count = min(min_count, simulation(directions))
        return

    cctv_type = cctv[idx][2]
    
    for m in mode[cctv_type]:
        directions.append(m)
        dfs(idx + 1, directions)
        directions.pop()

dfs(0, [])
print(min_count)