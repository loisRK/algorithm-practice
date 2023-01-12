n = int(input())
l = list(map(int,input().split()))
p = list(map(int,input().split()))
cost = 0
m = p[0]
for i in range(n-1):
  if p[i] < m:
    m = p[i]
  cost += m*l[i]

print(cost)