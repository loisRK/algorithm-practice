a = int(input())
num = []
for i in range(a):
  num.append(int(input()))

num.sort()

for i in range(len(num)):
  print(num[i])