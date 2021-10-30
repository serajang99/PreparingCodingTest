import sys
import math
input = sys.stdin.readline

n = int(input())
p = [math.inf for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    v1, v2, e = input().rstrip().split()
    p[v2] = v1
    graph[v2].append(v1)
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
