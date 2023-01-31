import sys
input = sys.stdin.readline

L = int(input())
strr = input().rstrip()
summ = 0
for i, w in enumerate(strr):
    summ += int(ord(w)-96) * (31 ** i)
print(summ % 1234567891)
