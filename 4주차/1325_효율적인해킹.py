import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    v1, v2 = map(int, input().rstrip().split())
    graph[v2].append(v1)

# dfs 로 했을때 시간 초과 메모리 초과 오지게 남


def bfs(start_node):
    q = deque([start_node])
    while q:
        next = q.popleft()
        if visited[next] == False:
            visited[next] = True
            cnt[start_node] += 1
            for n in graph[next]:
                if visited[n] == False:
                    q.append(n)


cnt = [0 for _ in range(n+1)]
for i in range(1, n+1):
    visited = [False for _ in range(n+1)]
    bfs(i)

max_cnt = max(cnt)
print(max_cnt, cnt)
for i in range(1, n+1):
    if cnt[i] == max_cnt:
        print(i, end=" ")
