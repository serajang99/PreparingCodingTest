import sys
input = sys.stdin.readline

N = int(input())
li = []
for _ in range(N):
    x, y = map(int, input().strip().split())
    li.append((x, y))

li = sorted(li, key=lambda x: x[0])
newli = []
cnt = 0
while cnt < N:
    max_y = li[cnt][1]
    while cnt != N-1 and li[cnt][0] == li[cnt+1][0]:
        max_y = max(max_y, li[cnt+1][1])
        # print("test", li[cnt][0], li[cnt][1], max_y)
        cnt += 1
        if cnt == N-1:
            break
    # print(li[cnt][0], max_y)
    newli.append((li[cnt][0], max_y))
    cnt += 1

# print(li)
# print(newli)
# print(li)
sum = 0
for i in range(len(newli)-1):
    x0, y0 = newli[i]
    x1, y1 = newli[i+1]
    # print(x1-x0, y0, y1, (x1-x0)*(y0+y1)/2)
    sum += (x1-x0)*(y0+y1)/2

if sum.is_integer():
    print(int(sum))
else:
    print(sum)
