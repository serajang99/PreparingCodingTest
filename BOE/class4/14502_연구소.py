import copy
from itertools import combinations
import sys
from collections import deque
input = sys.stdin.readline


def bfs(start_nodes, newMap):
    global n, m

    di = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    lst = deque([])
    for y, x in start_nodes:
        lst.append((y, x))

    while True:
        i, j = lst.popleft()

        for dy, dx in di:
            nx = j+dx
            ny = i+dy

            if nx < 0 or ny < 0 or nx > m-1 or ny > n-1:
                continue
            if newMap[ny][nx] == 1 or newMap[ny][nx] == 2:
                continue

            newMap[ny][nx] = 2
            lst.append((ny, nx))

        if len(lst) == 0:
            return


n, m = map(int, input().rstrip().split())
pMap = []
for i in range(n):
    pMap.append(list(map(int, input().rstrip().split())))

cnt = 0
start_nodes, empty_nodes = [], []
for i in range(n):
    for j in range(m):
        if pMap[i][j] == 2:
            start_nodes.append((i, j))
        elif pMap[i][j] == 0:
            empty_nodes.append((i, j))


empty_nodes = list(combinations(empty_nodes, 3))
result = -1


for i, j, k in empty_nodes:
    newMap = copy.deepcopy(pMap)
    newMap[i[0]][i[1]] = 1
    newMap[j[0]][j[1]] = 1
    newMap[k[0]][k[1]] = 1

    bfs(start_nodes, newMap)

    cnt = 0
    for y in range(n):
        for x in range(m):
            if newMap[y][x] == 0:
                cnt += 1

    result = max(result, cnt)

print(result)
