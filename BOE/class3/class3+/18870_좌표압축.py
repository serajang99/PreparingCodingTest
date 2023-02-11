import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

li2 = sorted(li)
dic = {}
cnt = 0
for i, item in enumerate(li2):
    if item not in dic:
        dic[item] = cnt
        cnt += 1

# print(dic)
# print(li)
# print(li2)
for i in li:
    print(dic[i], end=' ')
