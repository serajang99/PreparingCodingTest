import sys
input = sys.stdin.readline

lst = []
while True:
    temp = list(map(int, input().split()))
    if temp:
        if temp[-1] == -1 and temp[-2] == -1:
            break
        else:
            lst.extend(temp)

k = 0
for i in range(0, len(lst), 2):
    if lst[i] == 0 and lst[i+1] == 0:
        k += 1

test = [[] for _ in range(k)]
j = 0
for i in range(k):
    while lst[j] != 0 and lst[j+1] != 0:
        test[i].append((lst[j], lst[j+1]))
        j += 2
    j += 2

for i in range(k):
    print(test[i])
