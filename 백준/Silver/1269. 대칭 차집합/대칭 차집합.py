
n, m = map(int, input().split())
nList = set(map(int, input().split()))
mList = set(map(int, input().split()))


print(len(list(nList-mList)+list(mList-nList))) 