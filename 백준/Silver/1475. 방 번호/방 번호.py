num = list(str(input()))
cnt = [0]*10

for i in range(len(num)):
  n = int(num[i])
  if n == 6 or n == 9:
    if cnt[6] <= cnt[9]:
      cnt[6] += 1
    else:
      cnt[9] += 1
  else:
    cnt[n] += 1

print(max(cnt))