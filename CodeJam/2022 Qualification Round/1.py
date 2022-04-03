import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):

    r, c = map(int, input().rstrip().split())
    answer = [[] for _ in range(2*r+1)]
    for j in range(r):
        answer[j*2] = list('+-'*c+'+')
        answer[j*2+1] = list('|.'*c+'|')
    answer[-1] = list('+-'*c+'+')

    answer[0][0], answer[0][1], answer[1][0], answer[1][1] = ".", ".", ".", "."

    print("Case #%d: " % (i+1))
    for i in range(len(answer)):
        print("".join(map(str, answer[i])))
