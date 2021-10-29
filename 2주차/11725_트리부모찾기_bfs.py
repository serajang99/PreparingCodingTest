import sys
from collections import deque
input = sys.stdin.readline

# bfs로 구현하였다.
# bfs 실행속도가 dfs보다 빨랐다.


def bfs(graph, start_node, parent):
    q = deque([start_node])
    while q:
        p = q.popleft()
        for child in graph[p]:
            if parent[child] == -1:
                parent[child] = p
                q.append(child)


n = int(input())
graph = [[] for _ in range(n+1)]
parent = [-1 for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(graph, 1, parent)

for i in range(2, n+1):
    print(parent[i])


'''
7
1 6
6 3
3 5
4 1
2 4
4 7
'''
