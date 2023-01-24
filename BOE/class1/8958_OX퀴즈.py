import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    ox = input()
    cnt = 0
    total = 0
    for j in ox:
        if j == 'O':
            cnt += 1
        else:
            cnt = 0
        total += cnt
        # print(cnt, total)
    print(total)
