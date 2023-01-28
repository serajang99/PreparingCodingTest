import sys
input = sys.stdin.readline


def factorial(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret


n, k = map(int, input().split())
if k < 0 or k > n:
    print(0)
else:
    print(int(factorial(n)/(factorial(k) * factorial(n-k))))
