import sys
input = sys.stdin.readline

n, m = map(int, input().split())
chess = []
result = []

for _ in range(n):
    chess.append(input())

for i in range(n-7):
    for j in range(m-7):

        b, w = 0, 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if chess[k][l] != 'B':
                        b += 1
                    elif chess[k][l] != 'W':
                        w += 1
                elif (k+l) % 2 == 1:
                    if chess[k][l] != 'B':
                        w += 1
                    elif chess[k][l] != 'W':
                        b += 1
        # print(b, w)
        result.append(min(b, w))
print(min(result))
