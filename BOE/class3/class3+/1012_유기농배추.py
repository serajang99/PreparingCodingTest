from collections import deque
import sys
input = sys.stdin.readline


def bfs(board, i, j):
    q = deque([(i, j)])
    di = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while q:
        x, y = q.popleft()

        for dx, dy in di:
            nx = x+dx
            ny = y+dy

            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                continue
            if board[nx][ny] == 1:
                board[nx][ny] = 0
                q.append((nx, ny))


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1

    jirunge = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                bfs(board, i, j)
                jirunge += 1

    print(jirunge)
