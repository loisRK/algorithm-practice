from collections import deque

dq = deque()
answer = []

n, k = map(int, input().split())

for i in range(1, n+1):
  dq.append(i)

while dq:
  for _ in range(k-1):
    dq.append(dq.popleft())
  answer.append(dq.popleft())

print("<", end="")
for i in range(n-1):
  print("%a, "%answer[i], end="")
print("%a>"%answer[-1])