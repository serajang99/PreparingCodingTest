import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
dfs_results = []
bfs_results = []
for _ in range(m):
    v1, v2 = map(int, input().rstrip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(1, n+1):
    graph[i].sort()


def dfs(start_node):
    dfs_results.append(start_node)
    visited[start_node] = True
    nodes = graph[start_node]
    for n in nodes:
        if visited[n] == False:
            dfs(n)


def bfs(start_node):
    q = deque([start_node])
    while q:
        next = q.popleft()
        if visited[next] == False:
            bfs_results.append(next)
        visited[next] = True
        for n in graph[next]:
            if visited[n] == False:
                q.append(n)


dfs(v)
print(*dfs_results)
visited = [False for _ in range(n+1)]
bfs(v)
print(*bfs_results)
