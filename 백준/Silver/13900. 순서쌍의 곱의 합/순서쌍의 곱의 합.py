n = int(input())
num = list(map(int, input().split()))

num_sum = sum(num)
total = 0

for i in num:
  total += i*(num_sum-i)

print(total//2)