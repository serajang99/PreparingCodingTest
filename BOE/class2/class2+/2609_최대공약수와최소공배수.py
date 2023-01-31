import sys
input = sys.stdin.readline


def gcd(a, b):
    while 1:
        r = a % b
        if r == 0:
            return b
        a = b
        b = r


a, b = map(int, input().rstrip().split())
gcd = gcd(a, b)
print(gcd)
print(a * b // gcd)
