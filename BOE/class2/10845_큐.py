from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque([])
for i in range(n):
    cmd = input().rstrip()
    if cmd[:4] == 'push':
        _, num = cmd.split()
        num = int(num)
        q.append(num)
    elif cmd == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif cmd == 'size':
        print(len(q))
    elif cmd == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif cmd == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
