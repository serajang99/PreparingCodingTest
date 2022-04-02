from collections import defaultdict
import sys
input = sys.stdin.readline


def dfs(start, maps, visited):
    global price
    visited[start] = True
    nodes = maps[start]
    for end, fee in nodes:
        print(end, fee, price)
        if visited[end] == False:
            price += fee
            dfs(end, maps, visited)


t = int(input())
for i in range(t):
    answer = 0
    n = int(input())
    maps = {}
    visited = {}
    for j in range(1, n+1):
        maps[j] = []
        visited[j] = False
    abc = []
    for j in range(n-1):
        a, b, c = map(int, input().rstrip().split())
        maps[a].append((b, c))
        maps[b].append((a, c))
        abc.append((a, b, c))
    abc = sorted(abc, key=lambda x: x[2], reverse=True)
    start = abc[0][0]
    # print(maps)
    for k, v in maps.items():
        # print(k, v)
        maps[k] = sorted(v, key=lambda x: x[1])
    print(maps)
    print(abc, start)

    price = 0
    dfs(start, maps, visited)
    print(price)

    print("Case #%d: %d" % (i+1, answer))
