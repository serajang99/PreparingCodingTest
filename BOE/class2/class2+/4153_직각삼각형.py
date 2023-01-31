import sys
input = sys.stdin.readline

while True:
    sides = list(map(int, input().rstrip().split()))
    sides.sort()
    if sides[0] == sides[1] == sides[2] == 0:
        break
    if sides[0]*sides[0] + sides[1]*sides[1] == sides[2]*sides[2]:
        print("right")
    else:
        print("wrong")
