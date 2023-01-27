from collections import deque

# dfs - 재귀함수
def dfs(now):
  chk[now] = True
  print(now+1, end=' ')
  for nxt in range(n):
    if adj[now][nxt] and not chk[nxt]:
      dfs(nxt)

# bfs - deque(큐)
def bfs(now):
  dq = deque([now])
  chk2[now] = True
  while dq:
    s = dq.popleft()
    print(s+1, end=' ')
    for nxt in range(n):
      if adj[s][nxt] and not chk2[nxt]:
        chk2[nxt] = True
        dq.append(nxt)

n, m, s = map(int, input().split())
adj = [[0]*n for _ in range(n)]
for _ in range(m):
  a,b = map(lambda x:x-1, map(int, input().split()))
  adj[a][b] = adj[b][a] = 1

chk = [False]*n   # dfs check list
chk2 = [False]*n  # bfs check list

dfs(s-1)
print()
bfs(s-1)