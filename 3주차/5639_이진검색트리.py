import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def get_post(start, end):

    if start > end:
        return

    mid = end + 1
    for i in range(start+1, end+1):
        if preorder[i] > preorder[start]:
            mid = i
            break

    get_post(start+1, mid-1)
    get_post(mid, end)
    print(preorder[start])


preorder = []

while 1:
    try:
        preorder.append(int(input()))
    except:
        break

get_post(0, len(preorder)-1)
