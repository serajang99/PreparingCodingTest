import sys
input = sys.stdin.readline

preorder = []  # p l r
postorder = []  # l r p

while 1:
    try:
        preorder.append(int(input()))
    except:
        break

n = len(preorder)
position = [0]*(n+1)
for i in range(n):
    position[preorder[i]] = i


def makepost(in_start, in_end, post_start, post_end):

    if (in_start > in_end) or (post_start > post_end):
        return

    parents = postorder[post_end]
    print(parents, end=" ")

    left = position[parents] - in_start
    right = in_end - position[parents]

    makepost(in_start, in_start+left-1, post_start, post_start+left-1)
    makepost(in_end-right+1, in_end, post_end-right, post_end-1)


makepost(0, n-1, 0, n-1)
