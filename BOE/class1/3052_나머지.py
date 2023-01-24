from collections import defaultdict
import sys
input = sys.stdin.readline

remainder = defaultdict(int)
for _ in range(10):
    n = int(input())
    remainder[n % 42] += 1

print(len(remainder))
