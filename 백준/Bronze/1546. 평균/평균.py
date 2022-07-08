sub = input()
test_sc = input().split(' ')

x = len(test_sc)
sum = 0

for i in range(x):
  test_sc[i] = int(test_sc[i])

m = int(max(test_sc))

for i in range(x):
  sum += (int(test_sc[i])/int(m)*100)

print(sum/x)