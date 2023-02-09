import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
li = []
for i in range(n):
    li.append(int(input()))

li.sort()
print(round(sum(li)/len(li)))
if len(li) == 1:
    print(li[0])
else:
    print(li[len(li)//2])

dic = defaultdict(int)
for i in li:
    dic[i] += 1
li2 = sorted(dic.items(), key=lambda x: x[1], reverse=True)
# print(li2)
if len(li2) == 1:
    print(li2[0][0])
elif li2[0][1] == li2[1][1]:
    print(li2[1][0])
else:
    print(li2[0][0])

print(li[-1]-li[0])
