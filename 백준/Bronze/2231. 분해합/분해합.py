n = str(input())

for i in range(1, int(n)+1):
  temp = sum(list(map(int, str(i))))
  result = i + temp
  if result == int(n):
    print(i)
    break
  
  if i == int(n):
    print(0)