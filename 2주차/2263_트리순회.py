import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def makepre(in_start, in_end, post_start, post_end):

    if (in_start > in_end) or (post_start > post_end):
        return

    parents = postorder[post_end]
    print(parents, end=" ")

    left = position[parents] - in_start
    right = in_end - position[parents]

    makepre(in_start, in_start+left-1, post_start, post_start+left-1)
    makepre(in_end-right+1, in_end, post_end-right, post_end-1)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

position = [0]*(n+1)
for i in range(n):
    position[inorder[i]] = i

makepre(0, n-1, 0, n-1)


# import sys
# input = sys.stdin.readline


# def makepre(inorder, postorder):

#     if len(inorder) <= 1:
#         return inorder
#     if len(postorder) <= 1:
#         return postorder

#     root = postorder[-1]
#     mid = inorder.index(root)
#     inleft = inorder[:mid]
#     inright = inorder[mid+1:]
#     postleft = postorder[:mid]
#     postright = postorder[mid:-1]

#     preleft = makepre(inleft, postleft)
#     preright = makepre(inright, postright)

#     return [root]+preleft+preright


# n = int(input())
# inorder = list(map(int, input().rstrip().split()))
# postorder = list(map(int, input().rstrip().split()))
# preorder = []
# preorder = makepre(inorder, postorder)
# print(*preorder)
