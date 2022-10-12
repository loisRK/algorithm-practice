n = int(input())

if(n == 0):
  print(0)
elif(n == 1):
  print(1)
else:
  F = [0]*n
  F[0] = 0
  F[1] = 1
  for i in range(2, n):
    F[i] = F[i-1] + F[i-2]
  print(F[n-1]+F[n-2])