import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
dq = deque([i for i in range(1, n+1)])

for i in range(n-1):
    dq.popleft()
    temp = dq.popleft()
    dq.append(temp)

print(dq[0])
