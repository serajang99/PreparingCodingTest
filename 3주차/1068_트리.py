import sys
input = sys.stdin.readline


def dfs(graph, start_node, leaf):

    if not graph[start_node]:
        leaf += 1

    else:
        for child in graph[start_node]:
            leaf = dfs(graph, child, leaf)

    return leaf


n = int(input())
parent = list(map(int, input().rstrip().split()))
d = int(input())

graph = [[] for _ in range(n)]
root = -1

for i in range(n):
    if parent[i] == -1:
        root = i
    elif i == d:
        continue
    else:
        graph[parent[i]].append(i)

visited = [False for _ in range(n)]
if d == root:
    print(0)
else:
    leaf = dfs(graph, root, 0)
    print(leaf)
