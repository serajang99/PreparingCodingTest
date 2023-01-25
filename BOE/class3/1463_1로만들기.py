import sys
from collections import deque
input = sys.stdin.readline

num = int(input())
count = 0
li = deque([(num, count)])
while num != 1:
    n, cnt = li.popleft()
    if n % 3 == 0:
        li.append((n/3, cnt+1))
        if n / 3 == 1:
            break

    if n % 2 == 0:
        li.append((n/2, cnt+1))
        if n / 2 == 1:
            break

    li.append((n-1, cnt+1))
    if n - 1 == 1:
        break
    # print(li)
print(li[-1][1])
