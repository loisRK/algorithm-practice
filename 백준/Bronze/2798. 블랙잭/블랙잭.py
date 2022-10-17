n, m = input().split()
num = [int(a) for a in input().split()]
sum_n = 0
max_n = 0

for i in range(int(n)):
  for j in range(i+1,int(n)):
    for k in range(j+1,int(n)):
      sum_n = num[k] + num[j] + num[i]
      if(sum_n > int(m)):
        continue
      else:
        max_n = max(sum_n, max_n)
        
print(max_n)