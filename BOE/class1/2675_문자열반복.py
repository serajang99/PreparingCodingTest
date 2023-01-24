import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    li = input().split()
    n = int(li[0])
    for i in li[1]:
        print(i*n, end='')
    print()
