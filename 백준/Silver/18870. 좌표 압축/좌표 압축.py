a = int(input())
arr = [int(a) for a in list(input().split())]
ans = sorted(list(set(arr)))

dic = {ans[i]:i for i in range(len(ans))}

for i in arr:
    print(dic[i], end=' ')