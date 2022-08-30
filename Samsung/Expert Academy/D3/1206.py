T = 10
for test_case in range(1, T + 1):
    n = int(input())
    left, right = [], []
    buildings = list(map(int, input().rstrip().split()))
    cnt = 0
    for i in range(n):
        if i == 0:
            left = [0, 0]
        elif i == 1:
            left = [0, buildings[i-1]]
        else:
            left = [buildings[i-2], buildings[i-1]]

        if i == n-1:
            right = [0, 0]
        elif i == n-2:
            right = [buildings[i+1], 0]
        else:
            right = [buildings[i+1], buildings[i+2]]

        if (buildings[i] > left[0] and buildings[i] > left[1]) and (buildings[i] > right[0] and buildings[i] > right[1]):
            cnt += buildings[i] - max(left[0], left[1], right[0], right[1])
    print("#"+str(test_case), cnt)
