import sys
input = sys.stdin.readline
# runtime error 중 recursion error 발생 -> python이 정한 최대 재귀 깊이는 sys.getrecursionlimit()를 이용해 확인할 수 있으며, BOJ의 채점 서버에서 이 값은 1,000으로 설정되어있다. 해결 방법으로는 sys.setrecursionlimit()을 사용하는 것이 있다. 이 함수를 사용하면, Python이 정한 최대 재귀 갚이를 변경할 수 있다. 최대 재귀 깊이를 1,000,000 정도로 크게 설정하면 런타임 에러 없이 실행 된다.
sys.setrecursionlimit(10**9)

# dfs로 구현하였다.


def dfs(graph, start_node, parent):
    for child in graph[start_node]:
        if parent[child] == -1:
            parent[child] = start_node
            dfs(graph, child, parent)


n = int(input())
graph = [[] for _ in range(n+1)]
parent = [-1 for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, 1, parent)

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
