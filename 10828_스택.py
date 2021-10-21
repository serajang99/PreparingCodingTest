import sys
input = sys.stdin.readline

n = int(input())
s = []  # stack

for i in range(n):
    # command(cmd)를 list로 받는다.
    cmd = input().rstrip().split()

    # push 연산
    if cmd[0] == 'push':
        s.append(cmd[1])

    # pop 연산
    elif cmd[0] == 'pop':
        if len(s) > 0:
            print(s.pop())
        else:
            print(-1)

    # top 연산
    elif cmd[0] == 'top':
        if len(s) > 0:
            print(s[-1])
        else:
            print(-1)

    # size 연산
    elif cmd[0] == 'size':
        print(len(s))

    # empty 연산
    elif cmd[0] == 'empty':
        if len(s) == 0:
            print(1)
        else:
            print(0)
