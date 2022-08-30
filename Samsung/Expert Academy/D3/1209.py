T = 10
for test_case in range(1, T + 1):
    t = input()
    arr = [[] for _ in range(100)]
    sums = []

    cols = [0 for _ in range(100)]
    for i in range(100):
        arr[i] = list(map(int, (input().split())))
        sums.append(sum(arr[i]))
        cols = [cols[j] + arr[i][j] for j in range(100)]
    sums.extend(cols)

    diagonal1 = 0
    diagonal2 = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                diagonal1 += arr[i][j]
            if i == 99-j:
                diagonal2 += arr[i][j]

    sums.append(diagonal1)
    sums.append(diagonal2)

    print("#"+t, max(sums))
