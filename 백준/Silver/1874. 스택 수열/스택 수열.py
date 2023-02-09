from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

dq = deque()  # 수열 입력 스택택
ans = deque() # +,- 입력스택
cnt = 1
tmp = True    # 가능/불가능 판별 조건건

for i in range(n):
  num = int(input())
  while cnt <= num:
    dq.append(cnt)
    ans.append("+")
    cnt += 1
  if dq[-1] == num:
    dq.pop()
    ans.append("-")
  else:
    tmp = False

if tmp == True:
  for a in ans:
    print(a)
else:
  print("NO")