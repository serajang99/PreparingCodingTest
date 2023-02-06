import sys
import heapq
input = sys.stdin.readline

n = int(input())
maxheap = []
for _ in range(n):
    cmd = int(input())
    if cmd == 0:
        if len(maxheap) == 0:
            print(0)
        else:
            print(-heapq.heappop(maxheap))
    else:
        heapq.heappush(maxheap, -cmd)
