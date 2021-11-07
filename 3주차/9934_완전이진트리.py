import sys
input = sys.stdin.readline

'''
2
2 1 3
'''
k = int(input())
inorder = list(map(int, input().rstrip().split()))
n = len(inorder)
level = [[] for _ in range(k)]


# for j in range(0, k):  # 0, 1, 2
#     for i in range(2**j, len(inorder)+1, 2*(j+1)):  # 1 3 5 7  2 6   4
#         level[k-(j+1)].append(inorder[i-1])
#         # k-j 2 1 0

def get_level(inorder, lv):
    if len(inorder) == 1:
        level[lv].append(inorder[0])
        return inorder[0]

    mid = len(inorder) // 2
    left = get_level(inorder[:mid], lv+1)
    right = get_level(inorder[mid+1:], lv+1)

    level[lv].append(inorder[mid])
    return left+inorder[mid]+right


get_level(inorder, 0)

for lv in level:
    print(*lv)
