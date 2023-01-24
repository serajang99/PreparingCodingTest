import sys
input = sys.stdin.readline
# from itertools import combinations
# from math import gcd


def gcd(a, b):
    # 10, 20
    while 1:
        r = a % b
        if r == 0:
            return b
        a = b
        b = r


t = int(input())
for i in range(t):
    li = list(map(int, input().rstrip().split()))
    n = li[0]
    result = 0
    for i in range(1, n):
        for j in range(i+1, n+1):
            result += gcd(li[i], li[j])
    print(result)
