import sys
input = sys.stdin.readline

s = list(input().strip())

i = 0
while i < len(s):
    if s[i] == '<':
        i += 1
        while s[i] != '>':
            i += 1
        i += 1
    elif s[i] != ' ':
        start = i
        while i < len(s) and s[i] not in [' ', '<', '>']:
            i += 1
        tmp = s[start:i][::-1]
        s[start:i] = tmp
    else:
        i += 1

print("".join(s))
