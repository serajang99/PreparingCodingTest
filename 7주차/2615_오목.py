import sys
input = sys.stdin.readline

omok = [[] for _ in range(19)]
for i in range(19):
    omok[i] = list(map(int, input().strip().split()))

di = [(-1, 1), (0, 1), (1, 0), (1, 1)]


def check(y, x):
    if x < 0 or x >= 19 or y < 0 or y >= 19:
        return False
    return True


def count(y, x, val):

    for dy, dx in di:
        # print("dy dx:", dy, dx)
        ny, nx = y, x
        cnt = 1
        for _ in range(4):
            nx += dx
            ny += dy
            # print(ny, nx, cnt)
            if check(ny, nx) == True and omok[ny][nx] == val:
                # print(ny, nx, cnt, omok[ny][nx])
                cnt += 1
                if cnt == 5:
                    # 육목 확인1
                    if 0 <= nx+dx < 19 and 0 <= ny+dy < 19 and omok[ny+dy][nx+dx] == val:
                        cnt += 1
                        break
                    # 육목 확인2
                    if 0 <= x-dx < 19 and 0 <= y-dy < 19 and omok[y-dy][x-dx] == val:
                        cnt += 1
                        break
                    return y, x, cnt
            else:
                break

    return y, x, cnt


y, x, cnt = -1, -1, 0
flag = 0
for i in range(19):
    for j in range(19):
        if omok[i][j] == 1 or omok[i][j] == 2:
            val = omok[i][j]
            y, x, cnt = count(i, j, val)
            # print("result:", y, x, val, cnt)
            if cnt == 5:
                print(val)
                print(y+1, x+1)
                flag = 1
                break
        else:
            continue
    if flag == 1:
        break

if flag == 0:
    print(0)
