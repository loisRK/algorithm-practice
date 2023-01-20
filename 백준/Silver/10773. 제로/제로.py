n = int(input())
cnt = 0
li = []
while cnt < n:
  cnt += 1
  num = int(input())
  if num != 0:
    li.append(num)
    continue
  else:
    li.pop(len(li)-1)

print(sum(li))