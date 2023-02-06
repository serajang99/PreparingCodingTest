from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
if n == 1 or n == 2:
    print(n)
else:
    q = [1, 2]
    for i in range(2, n):
        q.append(q[i-2] + q[i-1])
    print(q[-1] % 10007)
