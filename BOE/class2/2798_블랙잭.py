from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
li = list(map(int, input().rstrip().split()))


maxx = 0
for i in combinations(li, 3):
    if sum(i) <= m:
        maxx = max(maxx, sum(i))
print(maxx)
