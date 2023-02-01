import sys
input = sys.stdin.readline

k = int(input())
li = []
for _ in range(k):
    n = int(input())
    if n != 0:
        li.append(n)
    else:
        li.pop()
print(sum(li))
