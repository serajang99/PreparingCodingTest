import sys
from collections import deque
input = sys.stdin.readline


def bfs(graph, start_node):
    q = deque([start_node])
    visit = [False for _ in range(len(graph))]
    cnt = [0 for _ in range(len(graph))]
    visit[start_node] = True
    while q:
        p = q.popleft()
        for child in graph[p]:
            if visit[child[0]] == False:
                q.append(child[0])
                visit[child[0]] = True
                cnt[child[0]] = cnt[p] + child[1]
    return cnt


n = int(input())
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    v1, v2, e = map(int, (input().rstrip().split()))
    graph[v2].append((v1, e))
    graph[v1].append((v2, e))

bfs1 = bfs(graph, 1)
max_idx = bfs1.index(max(bfs1))

print(max(bfs(graph, max_idx)))
'''
1  [(2,3), (3,2)]
2  [(1,3), (4,5)]
3  [(1,2), (5,11), (6,9)]
4  [(2,5), (7,1), (8,7)]
5  [(3,11), (9,15), (10,4)]
6  [(11,6), (12,10)]
7  [(4,1)]
8  [(4,7)]
9  [(5,15)]
10 [(5,4)]
11 [(6,6)]
12 [(6,10)]
'''
'''
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10
'''
