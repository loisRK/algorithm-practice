num = [1, 1, 2, 2, 2, 8]
chk = list(map(int, input().split()))

for i in range(len(num)):
    ans = num[i] - chk[i]
    print(ans, end=' ')