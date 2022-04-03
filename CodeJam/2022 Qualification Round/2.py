import sys
input = sys.stdin.readline

t = int(input())
for j in range(t):
    # answer = []
    c, m, y, k = [], [], [], []
    for i in range(3):
        ci, mi, yi, ki = map(int, input().split())
        c.append(ci)
        m.append(mi)
        y.append(yi)
        k.append(ki)
    minc = min(c)
    minm = min(m)
    miny = min(y)
    mink = min(k)
    summ = minc + minm + miny + mink
    if summ >= 1000000:
        answer = [minc, minm, miny, mink]
        diff = summ - 1000000
        for i in range(len(answer)):
            # print(answer, diff)
            if answer[i] > diff:
                answer[i] -= diff
                break
            else:
                diff = diff - answer[i]
                answer[i] = 0

    else:
        answer = "IMPOSSIBLE"
    print("Case #%d:" % (j+1), end=" ")
    if type(answer) == list:
        print(*answer)
    else:
        print(answer)
