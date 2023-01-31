import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())
n = 2**N
cnt = 0
while n > 1:
    n2 = n//2

    r2, c2 = 0, 0
    if r+1 > n2:
        r2 = 1
    if c+1 > n2:
        c2 = 1

    flag = 0
    if r2 == 0 and c2 == 0:
        flag = 0
    elif r2 == 0 and c2 == 1:
        flag = 1
        c -= n2
    elif r2 == 1 and c2 == 0:
        flag = 2
        r -= n2
    elif r2 == 1 and c2 == 1:
        flag = 3
        r -= n2
        c -= n2

    cnt += flag * n2 * n2
    n = n2

print(cnt)
