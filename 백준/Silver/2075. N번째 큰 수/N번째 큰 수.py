import heapq

n = int(input())
heap = []

for i in range(n):
  for j in map(int, input().split()):
    heapq.heappush(heap, j)
    if len(heap) > n:
      heapq.heappop(heap)

print(heap[0])