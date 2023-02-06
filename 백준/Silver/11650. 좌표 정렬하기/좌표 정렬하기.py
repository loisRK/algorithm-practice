n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
num.sort(key = lambda x:(x[0], x[1]))

for i in range(n):
    print(num[i][0], num[i][1])