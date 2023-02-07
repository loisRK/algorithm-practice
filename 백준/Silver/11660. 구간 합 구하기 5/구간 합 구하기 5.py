import sys

n,m = map(int, input().split())
input = sys.stdin.readline

gen_list = [list(map(int, input().split())) for _ in range(n)]
prefix_sum = [[0]*(n+1) for _ in range(n+1)]
sum = 0

for i in range(1,n+1):
  for j in range(1,n+1):
    prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + gen_list[i-1][j-1]

for _ in range(m):
  a, b, x, y = map(int, input().split()) 
  print(prefix_sum[x][y] - prefix_sum[x][b-1] - prefix_sum[a-1][y] + prefix_sum[a-1][b-1])