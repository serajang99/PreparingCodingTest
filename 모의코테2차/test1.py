import sys
input = sys.stdin.readline

N, h = map(int, input().strip().split())
li = []
for _ in range(N):
    x, s, k = map(int, input().strip().split())
    li.append((x, s, k))

li = sorted(li, key=lambda x: x[0])

hole = 0
pos = -1
for x, s, k in li:
    if s > h:
        if k == 1:
            hole += 1
            continue
        elif k == 3:
            pos = x
            break

print(pos, hole)
