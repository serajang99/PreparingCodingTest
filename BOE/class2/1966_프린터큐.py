from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    li2 = deque([(i, li[i]) for i in range(len(li))])
    cnt = 0
    while li2:
        flag = 0
        for i in range(1, len(li2)):
            if li2[0][1] < li2[i][1]:
                li2.append(li2.popleft())
                flag = 1
                break
        if flag == 0:
            cnt += 1
            tmp = li2.popleft()
            if m == tmp[0]:
                break
    print(cnt)
