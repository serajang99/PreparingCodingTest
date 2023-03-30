from itertools import combinations
import sys
input = sys.stdin.readline
n, s = map(int, input().rstrip().split())
items = list(map(int, input().rstrip().split()))
items.sort()
cnt = 0
for i in range(1, n+1):
    for comb in combinations(items, i):
        if sum(comb) == s:
            cnt += 1
print(cnt)
