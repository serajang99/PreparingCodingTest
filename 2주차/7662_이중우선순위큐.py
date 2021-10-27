import sys
import heapq
input = sys.stdin.readline

t = int(input())
for i in range(t):
    minheap, maxheap = []
    n = int(input())
    for j in range(n):
        command = input().rstrip().split()
        if command[0] == 'I':
            heapq.heappush(minheap, int(command[1]))
            heapq.heappush(maxheap, int(-command[1]))
        elif command[0] == 'D':
            if len(minheap) == 0:
                continue
            if command[1] == '-1':
                heapq.heappop(minheap)
            elif command[1] == '1':
                heapq.heappop(maxheap)
        # print(heap)
    if len(minheap) == 0:
        print('EMPTY')
    else:
        print(minheap[-1], minheap[0])
'''
2
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1
9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333
'''
