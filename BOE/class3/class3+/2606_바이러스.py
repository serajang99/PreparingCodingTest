import sys
input = sys.stdin.readline

v = int(input().rstrip())  # 컴퓨터 수
e = int(input().rstrip())  # edge

graph = [[] for _ in range(v+1)]

for _ in range(e):
    v1, v2 = map(int, input().rstrip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False for _ in range(v+1)]


def dfs(start_node):
    visited[start_node] = True
    next = graph[start_node]
    for n in next:
        if n and visited[n] == False:
            dfs(n)


dfs(1)
cnt = 0
for v in visited:
    if v == True:
        cnt += 1

print(cnt-1)

'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''
