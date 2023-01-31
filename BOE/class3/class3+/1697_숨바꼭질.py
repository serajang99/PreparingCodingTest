import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

count = 0
li = deque([(n, count)])
visited = [0 for _ in range(100001)]

if n == k:
    print(0)
while n != k:
    n, cnt = li.popleft()

    if visited[n] == 0:
        visited[n] = 1
    else:
        continue

    if n-1 == k or n+1 == k or n*2 == k:
        print(cnt+1)
        break

    if n-1 >= 0 and n-1 <= 100000:
        li.append((n-1, cnt+1))
    if n+1 >= 0 and n+1 <= 100000:
        li.append((n+1, cnt+1))
    if n*2 >= 0 and n*2 <= 100000:
        li.append((n*2, cnt+1))
