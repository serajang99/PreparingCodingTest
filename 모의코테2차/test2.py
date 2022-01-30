from collections import deque
import sys
input = sys.stdin.readline

N, K, P, L = map(int, input().strip().split())
rotation = [[] for _ in range(K)]
numbers = deque([i for i in range(N, 0, -1)])

for i in range(K):
    rotation[i] = list(map(int, input().strip().split()))

winner = -1
for j in range(L):
    for i in range(K):
        # print(j+1, "round", i+1, "turn", rotation[i][j], "times")
        for k in range(rotation[i][j]):
            tmp = numbers.popleft()
            numbers.append(tmp)
        # print(numbers)
        if numbers[-1] == P:
            print(i+1, j+1)
            winner = i+1
            break
    if numbers[-1] == P:
        break

if winner == -1:
    print(-1)
