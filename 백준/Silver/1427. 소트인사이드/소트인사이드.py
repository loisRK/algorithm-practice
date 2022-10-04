import sys

arr = [a for a in str(sys.stdin.readline())]
arr.sort(reverse=True)
ans = ""
for a in arr:
  ans += a

sys.stdout.write(ans)