# 파이썬 기본 재귀루프한도 1000 -> 넉넉하게 늘려주어 recursion에러 방지
import sys
sys.setrecursionlimit(10000)  
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[0]*n for _ in range(n)]   # 인접행렬만들기
for _ in range(m):
  a,b = map(lambda x : x-1, map(int, input().split()))  # 정점번호가 1부터 시작하므로 1을 빼줌
  adj[a][b] = adj[b][a] = 1

ans = 0   # 연결요소 갯수
chk = [False]*n   # check리스트 생성

def dfs(now):
  for nxt in range(n):
    # 한번 방문한곳은 가지 않게 하기 위해 조건을 걸어줌
    if adj[now][nxt] and not chk[nxt]:
      chk[nxt] = True
      dfs(nxt)

for i in range(n):
  if not chk[i]:
    ans += 1
    chk[i] = True
    dfs(i)

print(ans)