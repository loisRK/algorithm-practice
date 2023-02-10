n = int(input())

for _ in range(n):
  s = input()
  stack = 0
  
  for i in s:
    if i == "(":
      stack += 1
    else:
      stack -= 1
    
    if stack < 0:
      print("NO")
      break

  if stack == 0:
    print("YES")
  elif stack >= 0:
    print("NO")