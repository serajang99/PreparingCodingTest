import sys
import heapq
input = sys.stdin.readline

n = int(input())
li = []


# for i in range(n):
#     li.append(list(map(int, input().rstrip().split())))

# q = sorted(map(lambda x: -x, li[n-1]))
# nbig = q[-1]

# for i in range(n-2, -1, -1):
#     for j in range(n):
#         if -li[i][j] < nbig:
#             q.append(-li[i][j])
#             q = sorted(q)
#             q.pop()
#             nbig = q[-1]

# print(-q[-1])

'''
5
12 7 9 15 5
13 8 11 19 6
21 10 26 31 16
48 14 28 35 25
52 20 32 41 49
'''
