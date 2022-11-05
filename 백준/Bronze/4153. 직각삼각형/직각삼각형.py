answer = []

while(True):
  temp = sorted(list(map(int, input().split())))
  if(temp[0] == 0):
    break
  else:
    if((temp[0]**2 + temp[1]**2) == temp[2]**2):
      answer.append("right")
    else:
      answer.append("wrong")

for a in answer:
  print(a, end="\n")