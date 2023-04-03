import sys
input = sys.stdin.readline

n = int(input())
houses = []
for i in range(n):
    houses.append(list(map(int, input().rstrip().split())))

for i in range(1, n):
    houses[i][0] = min(houses[i-1][1], houses[i-1][2]) + houses[i][0]
    houses[i][1] = min(houses[i-1][0], houses[i-1][2]) + houses[i][1]
    houses[i][2] = min(houses[i-1][0], houses[i-1][1]) + houses[i][2]

    # print(houses)
print(min(houses[-1]))

# = 3 * 2 * 1 * 1
