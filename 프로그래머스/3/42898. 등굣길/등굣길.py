def solution(m, n, puddles):
    puddles = [[q,p] for [p,q] in puddles]
    map = [[0 for _ in range(m+1)] for _ in range(n+1)]
    map[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [i, j] in puddles:
                map[i][j] = 0
            else:
                map[i][j] = (map[i-1][j] + map[i][j-1]) % 1000000007

    return map[n][m] 