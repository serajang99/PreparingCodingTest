import sys
input = sys.stdin.readline

n = int(input())
summ = 1
cnt = 1
for i in range(6, 1000000000, 6):
    if summ >= n:
        break
    summ += i
    cnt += 1
print(cnt)
