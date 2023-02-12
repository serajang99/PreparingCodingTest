from collections import deque


def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])

    q = deque([(0, 0)])
    di = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while q:
        x, y = q.popleft()
        for dx, dy in di:
            nx = x + dx
            ny = y + dy
            if 0 > nx or nx >= n or 0 > ny or ny >= m:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))

    return -1 if maps[-1][-1] == 1 else maps[-1][-1]


maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
    1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]

maps2 = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
    1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
print(solution(maps))
print(solution(maps2))
