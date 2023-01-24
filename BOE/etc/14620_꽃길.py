import math
import sys
input = sys.stdin.readline

n = int(input())
garden = [list(map(int, input().rstrip().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
di = [(1, 0), (0, 1), (0, 0), (-1, 0), (0, -1)]
answer = math.inf


def calc_one_flower(y, x):
    result = 0
    for dy, dx in di:
        nx = x+dx
        ny = y+dy
        result += garden[ny][nx]
    return result


def check(y, x):
    global n
    for dy, dx in di:
        nx = x+dx
        ny = y+dy
        if visited[ny][nx]:
            return False
    return True


def dfs(x, cost, cnt):
    global answer
    if cnt == 3:
        answer = min(answer, cost)
        return
    for i in range(x, n-1):
        for j in range(1, n-1):
            if check(i, j):
                # print(cnt, i, j)
                for dy, dx in di:
                    visited[i+dy][j+dx] = True
                dfs(i, cost+calc_one_flower(i, j), cnt+1)
                for dy, dx in di:
                    visited[i+dy][j+dx] = False


dfs(1, 0, 0)
print(answer)
