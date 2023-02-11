import sys
input = sys.stdin.readline

n = int(input())
li = []
for i in range(n):
    start, end = map(int, input().split())
    li.append((start, end))


li = sorted(li, key=lambda x: (x[1], x[0]))

end_time = 0
cnt = 0
for start, end in li:
    if start >= end_time:
        cnt += 1
        end_time = end
print(cnt)
