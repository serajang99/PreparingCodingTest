from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque([])
for i in range(n):
    cmd = input().rstrip()
    if cmd[:6] == 'push_f':
        _, num = cmd.split()
        num = int(num)
        q.appendleft(num)
    elif cmd[:6] == 'push_b':
        _, num = cmd.split()
        num = int(num)
        q.append(num)
    elif cmd == 'pop_front':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif cmd == 'pop_back':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
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
