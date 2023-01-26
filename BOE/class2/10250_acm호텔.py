import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    h, w, n = map(int, input().rstrip().split())
    floor = n % h
    no = n // h + 1 if floor != 0 else n // h
    if floor == 0:
        floor = h

    floor_str = str(floor)
    no_str = "0"+str(no) if no < 10 else str(no)

    room_no = floor_str + no_str
    print(room_no)
