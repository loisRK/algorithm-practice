n, m = map(int, input().split())
pocketmon = {i+1:input() for i in range(n)}
quest = [input() for _ in range(m)]
re_pocket = dict(map(reversed,pocketmon.items()))

for q in quest:
  if q.isdigit():
    print(pocketmon[int(q)])
  else:
    print(re_pocket[q])