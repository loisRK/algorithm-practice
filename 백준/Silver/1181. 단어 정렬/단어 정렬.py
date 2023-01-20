import sys

n = int(sys.stdin.readline())
lst = [sys.stdin.readline().strip() for _ in range(n)]

set_lst = set(lst)
lst = list(set_lst)

lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)