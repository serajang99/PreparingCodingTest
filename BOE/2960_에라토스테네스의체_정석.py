import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

# [0, 1, 2, 3, 4, 5, 6, 7]
che = [False for _ in range(n+1)]
cnt = 0

for i in range(2, n+1):
    if che[i] == False:
        for j in range(i, n+1, i):
            if che[j] == False:
                che[j] = True
                cnt += 1
                if cnt == k:
                    print(j)
                    break
        if cnt == k:
            break
