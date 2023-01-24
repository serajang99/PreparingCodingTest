import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    parent = [-1 for _ in range(n+1)]
    for j in range(n-1):
        v1, v2 = map(int, input().rstrip().split())
        parent[v2] = v1
    a, b = map(int, input().rstrip().split())

    a_parent, b_parent = [], []
    while a != -1:
        a_parent.append(a)
        a = parent[a]
    while b != -1:
        b_parent.append(b)
        b = parent[b]
    for a in a_parent:
        for b in b_parent:
            if a == b:
                break
        if a == b:
            break

    print(a)


'''
1
5
2 3
3 4
3 1
1 5
3 5
'''
