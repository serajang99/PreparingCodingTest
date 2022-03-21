import sys
input = sys.stdin.readline

N = int(input())
li = []
for _ in range(N):
    x, y = map(int, input().strip().split())
    li.append((x, y))

li = sorted(li, key=lambda x: x[0])

# print(li)
sum = 0
for i in range(N-1):
    x0, y0 = li[i]
    x1, y1 = li[i+1]
    # print(x1-x0, y0, y1, (x1-x0)*(y0+y1)/2)
    sum += (x1-x0)*(y0+y1)/2

if sum.is_integer():
    print(int(sum))
else:
    print(sum)
