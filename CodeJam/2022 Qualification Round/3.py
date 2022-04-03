import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for j in range(t):
    answer = 1
    n = int(input())
    dices = deque(sorted(list(map(int, input().rstrip().split()))))
    while dices:
        dice = dices.popleft()
        if dice >= answer:
            answer += 1
        else:
            continue
    print("Case #%d: %d" % (j+1, answer-1))
