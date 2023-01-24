import sys
input = sys.stdin.readline

a, b, c, d, e = map(int, input().rstrip().split())
print((a*a+b*b+c*c+d*d+e*e) % 10)
