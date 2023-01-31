import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().rstrip().split()))
new = list(enumerate(li))
new.sort(key=lambda x: x[1])

summ = 0
new_value = 0
for index, value in new:
    new_value += value
    summ = summ + new_value
print(summ)
