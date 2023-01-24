import sys
input = sys.stdin.readline


def GCD(a, b):
    while 1:
        r = a % b
        if r == 0:
            return b
        a = b
        b = r


n = int(input())
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    gcd = GCD(a, b)
    result = gcd * (a/gcd) * (b/gcd)
    # if a < b:
    #     num = a
    # else:
    #     num = b
    # result = 1
    # for i in range(1, num+1):
    #     if a % i == 0 and b % i == 0:
    #         result *= i
    #         a /= i
    #         b /= i
    # result *= a*b

    print(int(result))
