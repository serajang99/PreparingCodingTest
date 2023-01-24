import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

abc = str(a*b*c)

number = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0,
          '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
for w in abc:
    number[w] += 1

for i in number.values():
    print(i)
