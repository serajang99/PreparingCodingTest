import sys
input = sys.stdin.readline

n = input().rstrip()

flag = 0
for i in range(int(n)-len(n)*9, int(n)):
    # print(i)
    if i < 1:
        continue
    nl = list(str(i))
    nl.append(str(i))
    nl = list(map(int, nl))
    if sum(nl) == int(n):
        print(i)
        flag = 1
        break
if flag == 0:
    print(0)
