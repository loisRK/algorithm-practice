x, y, n, m = map(int, input().split())

answer = [x, y, n-x, m-y]
print(min(answer))