# 입력
import sys
input = sys.stdin.readline


n, k = map(int, input().split())
q = [i for i in range(1, n+1)]
result = []
num = k-1

while len(q) > 0:
    result.append(str(q.pop(num)))
    if len(q) == 0:
        break
    num += k-1
    if num > len(q)-1:
        num %= len(q)

print('<'+', '.join(result)+'>')
