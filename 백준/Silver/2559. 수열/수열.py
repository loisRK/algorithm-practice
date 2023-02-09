n, m = map(int, input().split())
temp = list(map(int, input().split()))

temp_sum = [int(sum(temp[:m]))]

for i in range(0, n-m):
  temp_sum.append(temp_sum[-1] - temp[i] + temp[i+m])

print(max(temp_sum))