import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

len_s = len(s)
len_t = len(t)

result = False


def dfs(t, cnt):
    global result
    if cnt == len_t-len_s:
        if t == s:
            return True
        else:
            return False

    left, right = False, False

    if t[0] == 'B':
        left = dfs((t[1:])[::-1], cnt+1)
    if t[-1] == 'A':
        right = dfs(t[:len(t)-1], cnt+1)

    if left == True or right == True:
        return True


if dfs(t, 0) == True:
    print(1)
else:
    print(0)
