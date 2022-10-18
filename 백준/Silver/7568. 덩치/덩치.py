N = int(input())
li = []

for i in range(N):
    w, h = map(int, input().split())
    li.append([w, h])

for i in range(N):
    rank = 1
    for j in range(N):
        if (li[i][0] < li[j][0]) and (li[i][1] <  li[j][1]):
            rank += 1 
    print(rank, end = ' ')