n =  int(input())

cnt = 0

for i in range(n):
  word = input()

  if list(word) == sorted(word, key=word.find):
    cnt += 1

print(cnt)