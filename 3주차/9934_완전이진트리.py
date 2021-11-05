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


for j in range(0, k):  # 0, 1, 2
    for i in range(2**j, len(inorder)+1, 2*(j+1)):  # 1 3 5 7  2 6   4
        level[k-(j+1)].append(inorder[i-1])
        # k-j 2 1 0

for lv in level:
    print(*lv)
