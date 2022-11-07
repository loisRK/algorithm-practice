n = int(input())
x = []
y = []
axis = 0;

for i in range(6):
  temp = list(map(int, input().split()))
  if(i==0):
    if (temp[0] == 1 or temp[0] == 2):
      axis = 0
    else:
      axis = 1
  if(temp[0] == 1 or temp[0] == 2):
    x.append(temp[1])
  else:
    y.append(temp[1])

Xidx = x.index(max(x))
Yidx = y.index(max(y))

if axis == 0:
  miniY = abs(y[Xidx%3]-y[(Xidx-1)%3])
  miniX = abs(x[Yidx%3]-x[(Yidx+1)%3])
else:
  miniY = abs(y[Xidx%3]-y[(Xidx+1)%3])
  miniX = abs(x[Yidx%3]-x[(Yidx-1)%3])

print((max(x)*max(y) - miniX*miniY)*n)