import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(start_node):
    dfs_results.append(start_node)
    visited[start_node] = True
    nodes = li[start_node]
    for n in nodes:
        if visited[n] == False:
            dfs(n)


n, m = map(int, input().split())
li = [[] for _ in range(n)]
visited = [False for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    li[u-1].append(v-1)
    li[v-1].append(u-1)

cnt = 0
for i in range(n):
    dfs_results = []
    if visited[i] == False:
        dfs(i)
        cnt += 1
print(cnt)
