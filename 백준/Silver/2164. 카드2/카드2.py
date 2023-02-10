from collections import deque

n = int(input())

card = [i for i in range(1, n+1)]
cd = deque(card)

while len(cd) > 1:
  cd.popleft()
  cd.append(cd.popleft())

print(cd[-1])