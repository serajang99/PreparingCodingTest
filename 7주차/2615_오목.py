import sys
input = sys.stdin.readline

omok = [[] for _ in range(19)]
for i in range(19):
    omok[i] = list(map(int, input().strip().split()))

di = [(-1, 1), (0, 1), (1, 0), (1, 1)]


def check(y, x):
    for dy, dx in di:
        nx = x+dx
        ny = y+dy
        if nx < 0 or nx >= 19 or ny < 0 or ny >= 19:
            return False
    return True


def dfs(y, x, cnt):
    global answer
    if cnt == 5:
        answer = x, cnt
        return
    for i in range(x, 19):
        for j in range(1, 19):
            if check(i, j):
                dfs(i, j, cnt+1)


answer = -1
for i in range(19):
    for j in range(19):
        if omok[i][j] == 1 or omok[i][j] == 2:
            val = omok[i][j]
            cnt = 1
            if check(i, j) == True:
                result = dfs(i, j, cnt)
                print(result)
        else:
            continue
