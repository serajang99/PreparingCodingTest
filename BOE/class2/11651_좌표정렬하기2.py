import sys
input = sys.stdin.readline

n = int(input())
coordinates = []
for _ in range(n):
    x, y = map(int, input().rstrip().split())
    coordinates.append((x, y))
coordinates.sort(key=lambda x: x[0])
coordinates.sort(key=lambda x: x[1])


for x, y in coordinates:
    print(x, y)
