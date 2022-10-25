import sys

n = int(input())
nList = list(map(int, sys.stdin.readline().split()))
m = int(input())
mList = list(map(int, sys.stdin.readline().split()))

nList.sort()

def binary_search(array, target, start, end):
  while(start<=end):
    mid = (start + end)//2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid-1
    else:
      start = mid+1
  return None

for i in range(m):
  if binary_search(nList, mList[i], 0, n-1) is not None:
    print(1, end=" ")
  else:
    print(0, end=" ")