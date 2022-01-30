import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
li = [[] for _ in range(N)]
for i in range(N):
    L, R = map(int, input().strip().split())
    li[i].append(L-1)
    li[i].append(R-1)

visited = [False]*N


def dfs(start):
    visited[start] = True
    for node in li[start]:
        if visited[node] == False:
            dfs(node)


dfs(K-1)

sum = 0
for v in visited:
    if v == False:
        sum += 1

print(sum)
