import sys
input = sys.stdin.readline


def dfs(x, y, pMap, visited):
    global cnt, n, m

    visited[x][y] = 1
    di = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for d in di:
        nx = x+d[0]
        ny = y+d[1]

        if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
            continue
        if pMap[nx][ny] == 0:
            continue

        if not visited[nx][ny]:
            cnt += 1
            dfs(nx, ny, pMap, visited)


n, m = map(int, input().rstrip().split())
pMap = []
for i in range(n):
    pMap.append(list(map(int, input().rstrip())))

for i in range(n):
    print(pMap[i])

visited = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if pMap[i][j] == 1 and visited[i][j] == 0:
            cnt = 1
            dfs(i, j, pMap, visited)

print(cnt)
