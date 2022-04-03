import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for j in range(t):
    answer = 1
    n = int(input())
    funs = list(map(int, input().rstrip().split()))
    parents = list(map(int, input().rstrip().split()))
    maxp = max(parents)
    childs = list(set([i for i in range(n+1)]) - set(parents))
    print(parents, childs, maxp)
    graph = {}
    for i in range(maxp+1):
        graph[i] = []
    for i, node in enumerate(parents):
        print(i, node)
        graph[node].append(i+1)

    print("funs: ", funs)
    for i in range(maxp, 0, -1):

        child_funs = [funs[g-1] for g in graph[i]]
        print(funs[i-1], graph[i], child_funs)
        if funs[i-1] < min(child_funs):
            funs[i-1] = min(child_funs)
    print("funs: ", funs)
    print("graph: ", graph)

    print("Case #%d: %d" % (j+1, answer-1))
