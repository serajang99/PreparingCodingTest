import sys
input = sys.stdin.readline

n = int(input())
budget = sorted(list(map(int, input().strip().split())))
m = int(input())

start = 1
end = budget[-1]

total_budget = 0
while start <= end or total_budget > m:
    total_budget = 0
    mid = (start+end)//2

    for i in range(n):
        if budget[i] <= mid:
            total_budget += budget[i]
        else:
            total_budget += mid

    if total_budget <= m:
        start = mid+1
    else:
        end = mid-1

print(mid)
