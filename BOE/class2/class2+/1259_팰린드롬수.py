import sys
input = sys.stdin.readline

while True:
    n = input().rstrip()
    if n == "0":
        break
    if n == n[::-1]:
        print("yes")
    else:
        print("no")
