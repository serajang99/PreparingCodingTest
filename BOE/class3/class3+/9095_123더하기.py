import sys
input = sys.stdin.readline

# dp 문제 어려워잉
t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    else:
        li = [1, 2, 4]
        for i in range(3, n):
            li.append(li[i-3]+li[i-2]+li[i-1])
        print(li[-1])
