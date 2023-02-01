import sys
import math
input = sys.stdin.readline

start, end = map(int, input().split())
for i in range(start, end+1):

    flag = 0
    if i == 1:
        continue

    if i == 2 or i == 3:
        print(i)
        continue

    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            flag = 1
            break

    if flag == 0:
        print(i)
