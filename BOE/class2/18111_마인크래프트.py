import sys
import math
input = sys.stdin.readline

n, m, b = map(int, input().split())
li = []
for i in range(n):
    li.append(list(map(int, input().rstrip().split())))

height_r = 0
result = math.inf
for height in range(257):
    use_block = 0
    take_block = 0
    for i in range(n):
        for j in range(m):
            if li[i][j] < height:
                use_block += height-li[i][j]
            else:
                take_block += li[i][j]-height

    if use_block - take_block > b:
        continue

    if result >= take_block * 2 + use_block:
        result = take_block * 2 + use_block
        height_r = height

print(result, height_r)
