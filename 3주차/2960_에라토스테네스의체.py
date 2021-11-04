import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

# [2, 3, 4, 5, 6, 7]
p = 0
cnt = 0
che = [i for i in range(2, n+1)]


def find_p():
    tmp = 0
    for c in che:  # [2, 3, 4, 5, 6, 7]
        for i in range(1, c):  # [1~1, 1~2, 1~3, 1~4, 1~5, 1~6]
            if c % i == 0:
                tmp += 1
            if i == c-1:
                if tmp <= 1:
                    return c


while len(che) > 0:
    p = find_p()
    che.remove(p)
    cnt += 1
    if cnt == k:
        print(p)
        break
    for c in che:
        if c % p == 0:
            che.remove(c)
            cnt += 1
            if cnt == k:
                print(c)
                break
    if cnt == k:
        break
