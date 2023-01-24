import sys
input = sys.stdin.readline

li = list(map(int, input().split()))

result = 'ascending'
flag = li[0] < li[1]
for i in range(len(li)-1):
    cur = li[i] < li[i+1]
    if flag == cur:
        continue
    else:
        flag = 2
        result = 'mixed'
        break

if flag == False:
    result = 'descending'

print(result)
