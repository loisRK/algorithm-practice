n = int(input())
d = {}
sorted_d = {}
for _ in range(n):
  word = input()
  if word not in d:
    d[word] = 1
  else:
    d[word] += 1

sorted_d = sorted(d.items(), key=lambda x : x[1], reverse=True)
answer = [k for k, v in sorted_d if v == sorted_d[0][1]]
answer.sort()

print(answer[0])