import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
moves = [list(map(int, input().split())) for _ in range(M)]

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

# 초기 구름 위치
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

# 메인 시뮬레이션
for d, s in moves:
    moved_clouds = []
    for x, y in clouds:
        nx = (x + dx[d] * s) % N
        ny = (y + dy[d] * s) % N
        board[nx][ny] += 1
        moved_clouds.append((nx, ny))
    
    visited = set(moved_clouds)

    for r, c in visited:
        count = 0
        for i in [2, 4, 6, 8]:
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] > 0:
                count += 1
        board[r][c] += count

    new_clouds = []
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and (i, j) not in visited:
                board[i][j] -= 2
                new_clouds.append((i, j))
    
    # 구름 갱신
    clouds = new_clouds

# 정답 출력
result = sum(sum(row) for row in board)
print(result)