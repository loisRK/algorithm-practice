n = int(input())
m = int(input())
adj = [[0]*n for _ in range(n)]
for _ in range(m):
  a,b = map(lambda x:x-1, map(int, input().split()))
  adj[a][b] = adj[b][a] = 1

ans = 0   # 1번노드에 연결된 노드 수 count
chk = [False]*n

def dfs(now):
  chk[now] = True
  for nxt in range(n):
    if adj[now][nxt] and not chk[nxt]:
      global ans 
      ans += 1
      dfs(nxt)

dfs(0)    # 1번노드부터 시작 -> 인덱스 0으로 변환환

print(ans)