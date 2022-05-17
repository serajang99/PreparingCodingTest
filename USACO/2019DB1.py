from collections import defaultdict
import sys
input = sys.stdin.readline

with open("gymnastics.in", "r") as fin:
    k, n = [int(i) for i in fin.readline().split()]
    sessions = [list(map(int, line.split())) for line in fin]

cows = defaultdict()
cows2 = defaultdict()
for i in range(1, n):
    for j in range(i+1, n+1):
        cows[(i, j)] = 0
        cows2[(i, j)] = True

for i in range(k):
    if i == 0:
        for j in range(n - 1):
            for k in range(j + 1, n):
                if sessions[i][j] > sessions[i][k]:
                    cows[(sessions[i][k], sessions[i][j])] = 1
    else:
        for j in range(n - 1):
            for l in range(j + 1, n):
                if ((sessions[i][j] > sessions[i][l]) and (cows[(sessions[i][l], sessions[i][j])] == 1)) or ((sessions[i][j] < sessions[i][l]) and (cows[(sessions[i][j], sessions[i][l])] == 0)):
                    continue
                else:
                    if sessions[i][j] < sessions[i][l]:
                        cows2[(sessions[i][j], sessions[i][l])] = False
                    else:
                        cows2[(sessions[i][l], sessions[i][j])] = False

result = 0
for key, value in cows2.items():
    if value == True:
        result += 1

with open("gymnastics.out", "w+") as fout:
    print(result, file=fout)
