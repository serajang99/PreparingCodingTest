import sys
from itertools import combinations
import math
input = sys.stdin.readline

n = int(input().strip())
s = []
b = []
for i in range(n):
    sin, bit = map(int, input().strip().split())
    s.append(sin)
    b.append(bit)

min_sb = math.inf
index = [i for i in range(n)]
for i in range(1, n+1):
    index_comb = list(combinations(index, i))
    for j in index_comb:
        s_sum, b_sum = 1, 0
        for k in j:
            s_sum *= s[k]
            b_sum += b[k]
        min_sb = min(min_sb, abs(s_sum-b_sum))

print(min_sb)
