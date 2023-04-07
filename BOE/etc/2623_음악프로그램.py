import sys
from collections import deque
input = sys.stdin.readline


def topology_sort():
    result = []
    q = deque()
    # 1. 진입차수가 0인 모든 노드를 큐에 넣는다.
    for i in range(n):
        if indegree[i] == 0:  # 처음은 진입차수가 0인 것부터. 진입차수 0이 시작하는 노드이기 때문
            q.append(i)
    # 2. 큐가 빌 때까지 아래 과정 반복한다.
    while q:
        # 2-1. 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거한다.
        now = q.popleft()
        result.append(now + 1)   # 결과 넣기
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:   # 2-2. 새롭게 진입차수가 0이된 노드를 큐에 넣는다.
                q.append(i)

    if sum(indegree) > 0:  # 순서 정하는 게 불가능한 경우
        print(0)
    else:
        [print(i) for i in result]


n, m = map(int, sys.stdin.readline().split())  # 가수의 수, 보조 pd 수
indegree = [0] * n
result = [1] * n
graph = [[] for i in range(n)]

for _ in range(m):
    list_ = list(map(int, sys.stdin.readline().split()))
    for a, b in zip(list_[1:], list_[2:]):
        graph[a - 1].append(b - 1)  # a > b
        indegree[b - 1] += 1    # 진입 차수

topology_sort()
sadfasd
