import sys
input = sys.stdin.readline

n = int(input())
li = []
result = []
for i in range(n):
    weight, height = map(int, input().split())
    li.append((weight, height))

for i in range(n):
    cnt = 1
    for j in range(n):
        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            cnt += 1
    result.append(cnt)

for r in result:
    print(r, end=' ')
