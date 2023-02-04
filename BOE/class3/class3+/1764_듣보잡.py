import sys
input = sys.stdin.readline

n, m = map(int, input().split())
listen = {}
for _ in range(n):
    name = input().rstrip()
    if name not in listen:
        listen[name] = 1

result = []
cnt = 0
for _ in range(m):
    name = input().rstrip()
    if name in listen:
        result.append(name)
        cnt += 1
print(cnt)
result.sort()
for r in result:
    print(r)
