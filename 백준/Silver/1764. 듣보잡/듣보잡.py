n, m = map(int, input().split())
dList = set([input() for _ in range(n)])
tList = set([input() for _ in range(m)])

answer = list(dList&tList)

answer.sort()
print(len(answer))
for a in answer:
  print(a, end="\n")