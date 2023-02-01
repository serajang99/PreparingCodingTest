import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    li = [(1, 0), (0, 1)]
    n = int(input())
    if n == 0:
        print(li[0][0], li[0][1])
    elif n == 1:
        print(li[1][0], li[1][1])
    else:
        for j in range(2, n+1):
            li.append((li[j-2][0]+li[j-1][0], li[j-2][1]+li[j-1][1]))
        print(li[-1][0], li[-1][1])
