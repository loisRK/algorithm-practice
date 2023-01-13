word = list(str(input()).upper()) # 입력받은 단어
word_t = list(set(word))  # 알파벳 중복 제거

cnt = [0]*len(word_t)

for i in range(len(word_t)):
  cnt[i] = word.count(word_t[i])

max_cnt = max(cnt)
if cnt.count(max_cnt) > 1:
  print("?")
else:
  print(word_t[cnt.index(max_cnt)])