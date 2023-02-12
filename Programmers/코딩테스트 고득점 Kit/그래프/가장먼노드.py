from collections import deque


def solution(n, edge):
    answer = 0
    dic = {i: [] for i in range(1, n+1)}
    for e in edge:
        dic[e[0]].append(e[1])
        dic[e[1]].append(e[0])

    q = deque([(1, 0)])
    visited = {i: -1 for i in range(1, n+1)}
    while q:
        node, cnt = q.popleft()
        if visited[node] == -1:
            visited[node] = cnt
            for n in dic[node]:
                q.append((n, cnt+1))

    for i in visited.values():
        if i == max(visited.values()):
            answer += 1
    return answer


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))
