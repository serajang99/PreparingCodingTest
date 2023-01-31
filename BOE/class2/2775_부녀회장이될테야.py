import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())  # k층
    n = int(input())  # n호

    li = [i for i in range(1, n+1)]
    for _ in range(k):
        for i in range(1, n):
            if i == 1:
                li[i] += 1
            else:
                li[i] += li[i-1]

    print(li[-1])
