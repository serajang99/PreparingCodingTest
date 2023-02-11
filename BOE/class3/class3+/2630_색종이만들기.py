import sys
input = sys.stdin.readline

n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

result = []


def divide(x, y, n):
    n2 = n//2
    color = board[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if board[i][j] != color:
                divide(x, y, n2)
                divide(x, y+n2, n2)
                divide(x+n2, y, n2)
                divide(x+n2, y+n2, n2)
                return
    result.append(color)


divide(0, 0, n)
print(result.count(0))
print(result.count(1))
