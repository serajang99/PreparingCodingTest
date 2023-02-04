import sys
input = sys.stdin.readline

m = int(input())
s = set()
for _ in range(m):
    cmd = input().rstrip()

    if cmd == 'all':
        s = set({i for i in range(1, 21)})
    elif cmd == 'empty':
        s = set()
    else:
        cmd, x = cmd.split()
        x = int(x)
        if cmd == 'add':
            if x not in s:
                s.add(x)
        elif cmd == 'remove':
            if x in s:
                s.remove(x)
        elif cmd == 'check':
            if x in s:
                print(1)
            else:
                print(0)
        elif cmd == 'toggle':
            if x in s:
                s.remove(x)
            else:
                s.add(x)
