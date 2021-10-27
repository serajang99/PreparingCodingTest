import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
p = [-1 for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().rstrip().split())
    if a == 1 and b != 1:
        p[b] = a
    elif a != 1 and b == 1:
        p[a] = b
    else:
        if p[a] == -1:
            p[a] = b
        if p[b] == -1:
            p[b] = a

for i in range(2, n+1):
    print(p[i])
