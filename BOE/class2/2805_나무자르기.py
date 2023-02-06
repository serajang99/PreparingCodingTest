import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))

start, end = 1, max(li)

while start <= end:
    mid = (start+end)//2
    summ = 0
    for l in li:
        if l >= mid:
            summ += l - mid
    if summ >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
