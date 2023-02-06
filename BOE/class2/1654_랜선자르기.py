import sys
input = sys.stdin.readline

k, n = map(int, input().split())

li = []
for _ in range(k):
    li.append(int(input()))

start, end = 1, max(li)

while start <= end:
    mid = (start+end)//2
    summ = 0
    for l in li:
        summ += l//mid
    if summ >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)
