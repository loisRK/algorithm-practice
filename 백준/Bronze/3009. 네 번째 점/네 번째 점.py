a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

x = sorted([a[0], b[0], c[0]])
y = sorted([a[1], b[1], c[1]])

if(x.count(x[0]) == 1):
  X = x[0]
else:
  X = x[2]

if(y.count(y[0]) == 1):
  Y = y[0]
else:
  Y = y[2]

print(X, Y)