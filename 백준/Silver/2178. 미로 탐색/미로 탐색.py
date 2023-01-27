from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

n, m = map(int, input().split())
board = [input() for _ in range(n)]

def is_valid_coord(y, x):
  return 0 <= y < n and 0 <= x < m

def bfs():
  # 모든 경로를 탐색해야하므로 보드판과 같은 사이즈의 체크 판 생성
  chk = [[False] * m for _ in range(n)]   
  chk[0][0] = True
  dq = deque()
  dq.append((0,0,1))    # 시작 위치 y, x와 카운트를 세기 위한 1
  while dq:
    y,x,d = dq.popleft()

    if y == n-1 and x == m-1:
      return d

    nd = d + 1
    for k in range(4):
      ny = y + dy[k]
      nx = x + dx[k]
      if is_valid_coord(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
        chk[ny][nx] = True
        dq.append((ny, nx, nd))

print(bfs())