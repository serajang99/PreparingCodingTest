import sys
from collections import deque
input = sys.stdin.readline


def bfs(start_nodes, pMap):
    global cnt, n, m

    di = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    lst = deque([])
    for y, x in start_nodes:
        lst.append((y, x, cnt))
    # print("first", lst)

    while True:
        i, j, c = lst.popleft()

        # print(i, j, c)
        for dy, dx in di:
            nx = j+dx
            ny = i+dy

            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                continue
            if pMap[ny][nx] == 1 or pMap[ny][nx] == -1:
                continue

            # for k in range(m):
            #     print(pMap[k])

            pMap[ny][nx] = 1
            lst.append((ny, nx, c+1))

        if len(lst) == 0:
            break

    cnt = c
    for i in range(m):
        if 0 in pMap[i]:
            cnt = -1
    return


n, m = map(int, input().rstrip().split())
pMap = []
for i in range(m):
    pMap.append(list(map(int, input().rstrip().split())))

# for i in range(m):
#     print(pMap[i])

cnt = 0
start_nodes = []
for i in range(m):
    for j in range(n):
        if pMap[i][j] == 1:
            start_nodes.append((i, j))

# start_nodes가 비어있는 경우
if len(start_nodes) == 0:
    for i in range(m):
        if 0 in pMap[i]:
            cnt = -1

else:
    bfs(start_nodes, pMap)

# for i in range(m):
#     print(pMap[i])

print(cnt)
