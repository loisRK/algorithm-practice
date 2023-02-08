from collections import deque

n = int(input())
lst = [input() for _ in range(n)]
cnt = 0

for w in lst:
  dq = deque()
  wq = deque(w)
  dq.append(wq.popleft())
  while wq:
    s = wq.popleft()
    if len(dq)==0 or dq[-1] != s:
      dq.append(s)
    else:
      dq.pop()
  if len(dq) == 0:
    cnt += 1

print(cnt)