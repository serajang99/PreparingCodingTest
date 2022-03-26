import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    answer = 0
    n = int(input())
    n1, n2, n3, n4 = 0, 0, 0, 0
    arr = [[] for _ in range(n*2)]
    for y in range(n*2):
        arr[y] = list(input().rstrip())
        for x in range(n):
            if arr[y][x] == 'I' and y < n:
                n1 += 1
            elif arr[y][x] == 'I' and y >= n:
                n3 += 1

        for x in range(n, n*2):
            if arr[y][x] == 'I' and y < n:
                n2 += 1
            elif arr[y][x] == 'I' and y >= n:
                n4 += 1
    # print(n1, n2, n3, n4)
    # print(arr)
    answer += abs(n1-n4) + abs(n2-n3)
    print("Case #%d: %d" % (i+1, answer))
