import sys
import heapq
input = sys.stdin.readline

n = int(input())
minheap = []
for _ in range(n):
    cmd = int(input())
    if cmd == 0:
        if len(minheap) == 0:
            print(0)
        else:
            print(heapq.heappop(minheap))
    else:
        heapq.heappush(minheap, cmd)
