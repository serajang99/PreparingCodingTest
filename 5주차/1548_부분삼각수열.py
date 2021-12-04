import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().rstrip().split()))
a = sorted(a)

result = 2
if n < 3:
    print(n)
else:
    for i in range(n):
        for j in range(i+2, n):
            x, y, z = a[i], a[i+1], a[j]
            cnt = 0
            if z < x+y:
                cnt += 1
            if cnt == 1:
                result = max(result, j-i+1)
    print(result)

# https://isukorea.com/group/morgorithm/board/b/8
