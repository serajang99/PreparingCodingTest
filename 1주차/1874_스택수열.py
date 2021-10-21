import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
s = [1]  # stack
li = [i for i in range(1, n+1)]
cnt = 1  # li의 top
result = ['+']
error = 0
# s[-1] is stack top
for i in range(n):
    data = int(input())
    if not s:
        s.append(-1)

    if s[-1] <= data:
        for i in range(cnt, data):
            s.append(li[i])
            result.append('+')
            cnt += 1

        if s[-1] == data:
            result.append('-')
            s.pop()

    elif s[-1] > data:
        error = 1
        break

if error:
    print("NO")
else:
    for i in result:
        print(i)
